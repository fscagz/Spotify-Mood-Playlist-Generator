# app.py
import os
from dotenv import load_dotenv
from services.spotify_client import SpotifyClient
from core.playlist_logic import generate_playlist

load_dotenv()

def main():
    mood = input("Enter a mood or keywords: ").strip()
    print(f"[INPUT] Mood/keywords: {mood}")

    playlist_tracks = generate_playlist(mood_keywords=mood, limit=20)

    if not playlist_tracks:
        print("[ERROR] No tracks could be generated.")
        return

    spotify = SpotifyClient()
    playlist_name = f"Mood: {mood}"
    user = spotify.sp.current_user()
    user_id = user['id']

    playlist = spotify.sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=True,
        description=f"Dynamic playlist for mood: {mood}"
    )

    track_uris = [t['uri'] for t in playlist_tracks]
    for i in range(0, len(track_uris), 100):
        spotify.sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris[i:i+100])

    print(f"[SUCCESS] Playlist '{playlist_name}' created! Listen here: {playlist['external_urls']['spotify']}")

    print("\nPlaylist tracks:")
    for t in playlist_tracks:
        print(f"{t['name']} - {t['artist']}")

if __name__ == "__main__":
    main()
