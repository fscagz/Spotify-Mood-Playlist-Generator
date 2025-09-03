# services/nlp_model.py
'''
Keywords -> Spotify Genres
'''
import json
import re
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "genre_map.json")

with open(DATA_PATH, "r") as f:
    GENRE_MAP = json.load(f)

def clean_text(text: str) -> str:
    return re.sub(r"[^a-zA-Z\s]", "", text.lower())

def analyze_mood(mood: str, top_n: int = 3):
    # For now, uses simple keyword lookup; later add Distillibert
    mood = clean_text(mood)
    genres = []

    for word in mood.split():
        if word in GENRE_MAP:
            genres.extend(GENRE_MAP[word])

    if not genres:
        genres = ["pop"]

    return list(dict.fromkeys(genres))[:top_n]