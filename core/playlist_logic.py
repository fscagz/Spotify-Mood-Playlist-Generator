# core/playlist_logic.py
from services.spotify_client import SpotifyClient
from core.genres import VALID_GENRES

spotify = SpotifyClient()

# Minimal track mapping (hardcoded sample tracks per genre)
GENRE_SAMPLE_TRACKS = {
    "pop": [
        "3KkXRkHbMCARz0aVfEt68P",  # e.g., "Blinding Lights" - The Weeknd
        "6rqhFgbbKwnb9MLmUQDhG6"
    ],
    "rock": [
        "7ouMYWpwJ422jRcDASZB7P",  # e.g., "Bohemian Rhapsody"
        "1AhDOtG9vPSOmsWgNW0BEY"
    ],
    "hip hop": [
        "2QjOHCTQkX96fk3yhd9qkf",
        "6rPO02ozF3bM7NnOV4h6s2"
    ],
}

DEFAULT_GENRES = ["pop", "rock", "hip hop"]

def generate_playlist(seed_genres, limit=20):
    # normalize & filter
    cleaned = [g.lower().replace("-", " ").strip() for g in seed_genres]
    filtered = [g for g in cleaned if g in VALID_GENRES]

    if not filtered:
        print("[WARN] Not enough valid genres matched. Falling back to defaults.")
        filtered = DEFAULT_GENRES

    print(f"[LOGIC] Using seed genres: {filtered}")

    # Get tracks from hardcoded mapping
    playlist_tracks = []
    for genre in filtered:
        playlist_tracks.extend(GENRE_SAMPLE_TRACKS.get(genre, []))

    # Limit total tracks
    return playlist_tracks[:limit]
