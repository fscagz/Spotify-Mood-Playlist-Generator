# core/nlp.py
from core.genres import VALID_GENRES

def match_genres(user_input: str):
    """
    Map mood/keywords to Spotify genres.
    - Splits the input into words
    - Normalizes to lowercase
    - Matches against the official VALID_GENRES
    - Returns a filtered list or empty if nothing matches
    """
    tokens = [word.lower().strip() for word in user_input.split()]

    matched = [t for t in tokens if t in VALID_GENRES]

    if matched:
        print(f"[NLP] Matched genres: {matched}")
        return matched
    else:
        print("[NLP] No direct genre match.")
        return []
