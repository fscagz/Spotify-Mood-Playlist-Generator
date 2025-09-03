import os
from dotenv import load_dotenv, find_dotenv
from core.nlp import match_genres
from core.playlist_logic import generate_playlist
from services.spotify_client import SpotifyClient

# Load environment variables
load_dotenv(find_dotenv())

def main():
    # Initialize Spotify client
    spotify = SpotifyClient()

    # Get mood/keywords from command line argument or input
    import sys
    if len(sys.argv) > 1:
        mood_input = " ".join(sys.argv[1:])
    else:
        mood_input = input("Enter a mood or keywords: ")

    print(f"[INPUT] Mood/keywords: {mood_input}")

    # Step 1: Match genres (placeholder NLP)
    genres = match_genres(mood_input)

    # Step 2: Generate playlist tracks (hardcoded)
    playlist_tracks = generate_playlist(genres, limit=20)

    if not playlist_tracks:
        print("[ERROR] No tracks found, cannot create playlist.")
        return

    # Step 3: Create playlist in Spotify
    playlist_name = f"AI Mood Playlist - {mood_input}"
    playlist_url = spotify.create_playlist(playlist_name, playlist_tracks)

    print(f"[SUCCESS] Playlist created: {playlist_url}")


if __name__ == "__main__":
    main()