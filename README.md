# Spotify-Mood-Playlist-Generator
Create a playlist based on your mood!

PHASE 1: Basic Command Line infrastructure now in place.
```
ai_playlist_generator/
│── app.py                 # Main entry point (CLI or Flask/FastAPI server)
│
├── config/
│   └── settings.py        # API keys, environment variables, config loader
│
├── services/
│   ├── spotify_client.py  # Wrapper around Spotify Web API (auth, search, create playlist)
│   └── nlp_model.py       # Loads DistilBERT (HuggingFace) and processes mood/keywords
│
├── core/
│   ├── playlist_logic.py  # Algorithm to map mood → genres/tracks using NLP + Spotify
│   └── utils.py           # Helpers (logging, error handling, formatting)
│
├── routes/  (optional if web app)
│   └── api.py             # Endpoints for generating playlists, saving, sharing
│
├── data/
│   └── genre_map.json     # Map moods/keywords → Spotify genres (seed data for NLP)
│
├── tests/
│   ├── test_spotify.py    # Unit tests for Spotify API wrapper
│   ├── test_nlp.py        # Tests for NLP mood → genre mapping
│   └── test_playlist.py   # Tests for playlist generation logic
│
├── requirements.txt       # Dependencies (spotipy, transformers, flask/fastapi, etc.)
├── README.md              # Project setup + usage guide
└── .env                   # API keys (Spotify Client ID/Secret)
```
