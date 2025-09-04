import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from core.genres import FALLBACK_TRACKS

load_dotenv()

VALID_SEED_GENRES = [
    "acoustic","afrobeat","alt-rock","ambient","classical","country",
    "dance","deep-house","disco","drum-and-bass","dubstep","edm",
    "electro","folk","funk","hip-hop","house","indie","jazz",
    "metal","pop","punk","r-n-b","reggae","rock","soul","techno",
    "trance","trip-hop","world-music"
]

GENRE_MAP = {
    "rock": "rock",
    "hip hop": "hip-hop",
    "metal": "metal",
    "pop": "pop",
    "edm": "edm",
    "chill": "ambient",
    "ambient": "ambient",
    "classical": "classical",
    "jazz": "jazz",
    "folk": "folk",
    "punk": "punk",
    "r&b": "r-n-b",
    "soul": "soul",
    "dance": "dance",
    "trance": "trance",
    "house": "house",
    "deep house": "deep-house",
    "dubstep": "dubstep",
    "drum and bass": "drum-and-bass"
}


class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope="playlist-modify-public playlist-modify-private"
        ))

    def get_recommendations(self, seed_genres: list[str], limit: int = 20) -> list[dict]:
        seeds = [GENRE_MAP[g] for g in seed_genres if g in GENRE_MAP and GENRE_MAP[g] in VALID_SEED_GENRES]
        if not seeds:
            raise ValueError("No valid Spotify seed genres for recommendations.")

        try:
            results = self.sp.recommendations(seed_genres=seeds[:5], limit=limit)
            tracks = []
            for t in results['tracks']:
                tracks.append({
                    "name": t['name'],
                    "artist": t['artists'][0]['name'],
                    "uri": t['uri']
                })
            return tracks
        except Exception as e:
            raise RuntimeError(f"Spotify API request failed: {e}")

    def create_playlist(self, playlist_name: str, tracks: list[dict], public: bool = True) -> str:
        user_id = self.sp.current_user()['id']
        playlist = self.sp.user_playlist_create(user_id, playlist_name, public=public)
        uris = [track['uri'] for track in tracks]
        for i in range(0, len(uris), 100):
            self.sp.playlist_add_items(playlist['id'], uris[i:i+100])
        return playlist['external_urls']['spotify']

    def get_fallback_tracks(self, genre: str) -> list[dict]:
        return FALLBACK_TRACKS.get(genre, [])
