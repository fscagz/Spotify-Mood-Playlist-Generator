# core/genres.py

# Default fallback genres
DEFAULT_GENRES = ["pop", "rock", "hip-hop"]

# Spotify-valid recommendation seeds
VALID_SPOTIFY_SEEDS = [
    "acoustic","afrobeat","alt-rock","ambient","classical","country",
    "dance","deep-house","disco","drum-and-bass","dubstep","edm",
    "electro","folk","funk","hip-hop","house","indie","jazz",
    "metal","pop","punk","r-n-b","reggae","rock","soul","techno",
    "trance","trip-hop","world-music"
]

# Only use strings from VALID_SPOTIFY_SEEDS
MOOD_TO_SEED = {
    # Energetic / Workout
    "workout": "edm",
    "gym": "edm",
    "energetic": "dance",
    "intense": "alt-rock",
    "angry": "metal",
    "pump-up": "alt-rock",
    
    # Calm / Relaxed
    "chill": "ambient",
    "relax": "ambient",
    "calm": "ambient",
    "study": "ambient",
    "focus": "ambient",
    
    # Popular / mainstream
    "pop": "pop",
    "hits": "pop",
    "trending": "pop",
    
    # Rock & Alternative
    "rock": "alt-rock",
    "alternative": "alt-rock",
    "alt-rock": "alt-rock",
    "indie": "indie",
    
    # Hip-hop / R&B
    "hip hop": "hip-hop",
    "rap": "hip-hop",
    "r&b": "r-n-b",
    "soul": "soul",
    
    # Dance / Electronic
    "edm": "edm",
    "electronic": "electro",
    "dance": "dance",
    "trance": "trance",
    "house": "house",
    "deep house": "deep-house",
    "dubstep": "dubstep",
    "drum and bass": "drum-and-bass",
    
    # Latin & World
    "latin": "world-music",
    "reggaeton": "world-music",
    "reggae": "reggae",
    "k-pop": "pop",           # safe fallback
    
    # Classical / Jazz / Blues / Folk
    "classical": "classical",
    "jazz": "jazz",
    "blues": "funk",           # safe fallback
    "folk": "folk",
    "funk": "funk",
    
    # Metal / Hard Rock / Punk
    "metal": "metal",
    "heavy metal": "metal",
    "hard rock": "alt-rock",
    "punk": "punk",
    
    # Misc / fallback
    "ambient": "ambient",
    "lofi": "ambient",
    "lo-fi": "ambient",
    "sleep": "ambient",
    "rainy": "ambient",
    "morning": "acoustic",
    "happy": "pop",
    "sad": "ambient"
}

# Hard-coded fallback tracks 
FALLBACK_TRACKS = {
    "pop": [
        {"name": "Blinding Lights", "artist": "The Weeknd", "uri": "spotify:track:0VjIjW4GlUZAMYd2vXMi3b"},
        {"name": "Levitating", "artist": "Dua Lipa", "uri": "spotify:track:463CkQjx2Zk1yXoBuierM9"},
    ],
    "rock": [
        {"name": "Bohemian Rhapsody", "artist": "Queen", "uri": "spotify:track:7tFiyTwD0nx5a1eklYtX2J"},
        {"name": "Smells Like Teen Spirit", "artist": "Nirvana", "uri": "spotify:track:5ghIJDpPoe3CfHMGu71E6T"},
    ],
    "hip-hop": [
        {"name": "Sicko Mode", "artist": "Travis Scott", "uri": "spotify:track:2xLMifQCjDGFmkHkpNLD9h"},
        {"name": "God's Plan", "artist": "Drake", "uri": "spotify:track:6DCZcSspjsKoFjzjrWoCdn"},
    ],
    "metal": [
        {"name": "Master of Puppets", "artist": "Metallica", "uri": "spotify:track:2Kh43m04B1UkVcpcRa1Zc1"},
        {"name": "Painkiller", "artist": "Judas Priest", "uri": "spotify:track:6z1dT5N0b8B5FyGJxzZ7kw"},
    ],
    "alt-rock": [
        {"name": "Seven Nation Army", "artist": "The White Stripes", "uri": "spotify:track:3fMbdgg4jU18AjLCKBhRSm"},
        {"name": "Take Me Out", "artist": "Franz Ferdinand", "uri": "spotify:track:6lnmKkbD8c0oXu80l5t3tY"},
    ],
    "ambient": [
        {"name": "Weightless", "artist": "Marconi Union", "uri": "spotify:track:4K6cB8K6n3Xq9ktkxyDHK4"},
        {"name": "Ambient 1: Music for Airports", "artist": "Brian Eno", "uri": "spotify:track:0G0RA1yKHxUmg35e0Zywh3"},
    ]
}
