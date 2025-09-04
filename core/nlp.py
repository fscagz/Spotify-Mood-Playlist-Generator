# core/nlp.py

# Map basic keywords to one or more possible genres
MOOD_TO_GENRES = {
    "rainy": ["chill", "ambient", "acoustic"],
    "morning": ["acoustic", "pop", "classical"],
    "sad": ["ambient", "jazz", "blues"],
    "happy": ["pop", "electronic", "dance"],
    "angry": ["rock", "metal", "hip hop"],
    "party": ["dance", "electronic", "pop", "hip hop"],
    "relax": ["chill", "jazz", "classical"],
    "focus": ["classical", "electronic", "ambient"],
    "workout": ["electronic", "hip hop", "pop", "rock"],
    "love": ["pop", "rnb", "acoustic"],
    "sleep": ["ambient", "classical", "chill"]
}

def match_genres(keywords):
    """
    Returns a list of genres matching the given mood/keywords.
    Matches multiple genres per keyword to improve playlist diversity.
    """
    keywords = keywords.lower().split()
    matched_genres = set()

    for word in keywords:
        if word in MOOD_TO_GENRES:
            matched_genres.update(MOOD_TO_GENRES[word])

    return list(matched_genres)
