import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv

# Automatically find and load .env from project root
dotenv_path = find_dotenv()
if not dotenv_path:
    raise FileNotFoundError("Could not find a .env file in the project root.")
load_dotenv(dotenv_path)

class SpotifyClient:
    def __init__(self):
        # Read credentials from environment
        client_id = os.getenv("SPOTIPY_CLIENT_ID")
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

        # Fail early if missing
        if not client_id or not client_secret or not redirect_uri:
            raise ValueError(
                "Missing Spotify credentials. Make sure .env has SPOTIPY_CLIENT_ID, "
                "SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI."
            )

        # Optional debug
        print(f"[DEBUG] CLIENT_ID loaded: {client_id[:5]}...")  # first 5 chars
        print(f"[DEBUG] REDIRECT_URI loaded: {redirect_uri}")

        # Initialize Spotify client
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=[
                "playlist-modify-public",
                "playlist-modify-private",
                "user-read-private"
            ]
        ))

    def get_recommendations(self, seed_genres, limit=20):
        return self.sp.recommendations(seed_genres=seed_genres, limit=limit)

    def create_playlist(self, name, tracks):
        user_id = self.sp.current_user()["id"]
        playlist = self.sp.user_playlist_create(user=user_id, name=name, public=True)

        # Make sure tracks are URIs
        uris = [t["uri"] if isinstance(t, dict) else t for t in tracks]
        if uris:
            self.sp.playlist_add_items(playlist["id"], uris)

        return playlist["external_urls"]["spotify"]
