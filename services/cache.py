# services/cache.py
import json
import os

CACHE_FILE = "data/lastfm_cache.json"

def load_cache() -> dict:
    """Load the cache from disk."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache: dict):
    """Save the cache to disk."""
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

def get_cached_tracks(mood: str):
    cache = load_cache()
    return cache.get(mood.lower(), [])

def set_cached_tracks(mood: str, tracks: list):
    cache = load_cache()
    cache[mood.lower()] = tracks
    save_cache(cache)
