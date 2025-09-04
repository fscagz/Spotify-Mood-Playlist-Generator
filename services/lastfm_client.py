# services/lastfm_client.py
import pylast

class LastFMClient:
    def __init__(self, api_key: str, api_secret: str):
        self.network = pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret)

    def get_similar_tracks(self, artist_name: str, limit: int = 5):
        """
        Fetches top tracks from artists similar to the given artist.
        Returns a list of (track_name, artist_name).
        """
        try:
            artist = self.network.get_artist(artist_name)
            similar_artists = artist.get_similar(limit=limit)
            tracks = []
            for sim_artist, _ in similar_artists:
                top_tracks = sim_artist.get_top_tracks(limit=3)
                for t, _ in top_tracks:
                    tracks.append((t.title, sim_artist.name))
            return tracks
        except Exception as e:
            print(f"[ERROR] Last.fm request failed: {e}")
            return []
