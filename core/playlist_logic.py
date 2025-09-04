# core/playlist_logic.py
from services.spotify_client import SpotifyClient
from services.lastfm_client import LastFMClient
from services.cache import get_cached_tracks, set_cached_tracks
from core.genres import DEFAULT_GENRES, FALLBACK_TRACKS
from core.semantic_nlp import match_semantic_genres
import os
from dotenv import load_dotenv
import random

load_dotenv()

spotify = SpotifyClient()
lastfm = LastFMClient(api_key=os.getenv("LASTFM_API_KEY"), api_secret=os.getenv("LASTFM_SECRET"))


def generate_playlist(mood_keywords: str, limit: int = 20) -> list[dict]:
    """
    Generates a Spotify playlist based on mood/keywords.
    Steps:
      1. Check cache
      2. Semantic mood-to-genre matching
      3. Fetch tracks dynamically from Last.fm
      4. Search Spotify for playable track URIs
      5. Fill in with fallback tracks if needed
      6. Shuffle and limit
      7. Cache results
    """
    # Check cache first
    cached = get_cached_tracks(mood_keywords)
    if cached:
        print(f"[CACHE] Using cached tracks for mood '{mood_keywords}'")
        return cached[:limit]

    matched_genres = match_semantic_genres(mood_keywords)
    if not matched_genres:
        print("[WARN] No genres matched, using defaults.")
        matched_genres = DEFAULT_GENRES.copy()

    print(f"[LOGIC] Matched genres: {matched_genres}")

    playlist_tracks = []

    # Last.fm integration if no Spotify premium
    for genre in matched_genres:
        try:
            lastfm_tracks = lastfm.get_similar_tracks(artist_name=genre, limit=3)
            for name, artist in lastfm_tracks:
                # Search Spotify for the track URI
                results = spotify.sp.search(q=f"{name} {artist}", type="track", limit=1)
                if results['tracks']['items']:
                    track_info = results['tracks']['items'][0]
                    playlist_tracks.append({
                        'name': track_info['name'],
                        'artist': track_info['artists'][0]['name'],
                        'uri': track_info['uri']
                    })
        except Exception as e:
            print(f"[ERROR] Last.fm/Spotify fetch failed for genre '{genre}': {e}")
            playlist_tracks.extend(FALLBACK_TRACKS.get(genre, []))

    # Fill in with fallback tracks if playlist is too short
    if len(playlist_tracks) < limit:
        for genre in matched_genres:
            playlist_tracks.extend(FALLBACK_TRACKS.get(genre, []))

    random.shuffle(playlist_tracks)
    final_tracks = playlist_tracks[:limit]

    set_cached_tracks(mood_keywords, final_tracks)

    return final_tracks
