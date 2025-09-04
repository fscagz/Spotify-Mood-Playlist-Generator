# core/semantic_nlp.py
from sentence_transformers import SentenceTransformer, util
from core.nlp import MOOD_TO_GENRES

# Small embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute embeddings for all moods in MOOD_TO_GENRES
mood_texts = list(MOOD_TO_GENRES.keys())
mood_embeddings = model.encode(mood_texts, convert_to_tensor=True)

def match_semantic_genres(user_input: str, top_k: int = 3):
    """
    Returns top genres based on semantic similarity between user_input and known moods.
    """
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    
    # Compute cosine similarity
    similarities = util.cos_sim(input_embedding, mood_embeddings)[0]
    
    top_indices = similarities.topk(top_k).indices.tolist()
    
    matched_genres = set()
    for idx in top_indices:
        mood = mood_texts[idx]
        matched_genres.update(MOOD_TO_GENRES[mood])
    
    return list(matched_genres)
