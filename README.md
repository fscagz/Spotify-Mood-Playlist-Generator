# Spotify Mood Playlist Generator

Generate Spotify playlists automatically based on a mood or set of keywords.
This project works with a **Spotify Free account** by using fallback tracks and **Last.fm recommendations** for dynamic variety. With a **Spotify Premium account**, you can unlock live Spotify recommendations (with some modifications).

It includes both a **command-line app** and a **PyQt5 desktop GUI**.

---

## Features

* Input a mood or keywords (e.g., *"rainy morning"*, *"angry gym session"*).
* NLP-powered genre matching (using **DistilBERT embeddings**) for smarter mood interpretation.
* Dynamic track sourcing:

  * **Last.fm API** for free users (fresh recommendations).
  * **Spotify API** for Premium users (recommendations + playlist creation).
* Fallback tracks ensure playlists are *always* generated.
* Playlist automatically created in your Spotify account.
* Simple **PyQt5 GUI** (no terminal required).

---

## 📂 Project Structure

```
Spotify-Mood-Playlist-Generator/
│── app.py                  # CLI entry point
│── ui_app_pyqt5_simple.py  # PyQt5 desktop app
│── requirements.txt        # Python dependencies
│── .env                    # Your Spotify + Last.fm credentials
│
├── core/
│   ├── playlist_logic.py   # Main playlist generation logic
│   ├── nlp.py              # Simple Mood/genre matching
│   ├── semantic_nlp.py     # Uses small embedding model for enhanced mood/genre matching
│   ├── genres.py           # Genre mappings + fallbacks
│
├── services/
│   ├── spotify_client.py   # Spotify API wrapper
│   ├── lastfm_client.py    # Last.fm API wrapper
│   ├── cache.py            # Cache for Last.fm API
│
└── data/
    └── genre_map.json      # Optional custom mappings
    ├── lastfm_cache.json   # Cache to reduce Last.fm API calls
```

---

## Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/Spotify-Mood-Playlist-Generator.git
   cd Spotify-Mood-Playlist-Generator
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Add environment variables**
   Create a `.env` file in the root directory:

   ```ini
   # Spotify API (from https://developer.spotify.com/dashboard)
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

   # Last.fm API (from https://www.last.fm/api)
   LASTFM_API_KEY=your_lastfm_api_key
   LASTFM_SECRET=your_lastfm_secret_key
   ```

4. **Run the CLI version**

   ```bash
   python3 app.py "rainy morning"
   ```

5. **Run the PyQt5 desktop app**

   ```bash
   python3 ui_app_pyqt5_simple.py
   ```

---

## Usage

### Example CLI run:

```bash
python3 app.py "angry gym session"
```

Output:

```
[INPUT] Mood/keywords: angry gym session
[LOGIC] Matched genres: ['hip hop', 'metal', 'rock']
[SUCCESS] Playlist 'Mood: angry gym session' created! Listen here: https://open.spotify.com/playlist/066eJvHMHkTaIEaptc27m1
```

### Example GUI run:

1. Launch `ui_app_pyqt5_simple.py`.
2. Enter a mood → *rainy morning*.
3. Click **Generate Playlist**.
4. View the tracks + working playlist link.

---

## Roadmap for future development

* [ ] Smarter NLP mood-to-genre matching.
* [ ] More curated fallback tracks.
* [ ] User settings: private vs public playlists.
* [ ] Save playlists locally as `.m3u` or `.csv`.
* [ ] Add support for YouTube Music or Apple Music.
