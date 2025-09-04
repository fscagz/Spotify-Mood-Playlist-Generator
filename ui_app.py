# ui_app_pyqt5.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QSpinBox,
    QTextEdit, QVBoxLayout, QHBoxLayout, QProgressBar, QMessageBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from core.playlist_logic import generate_playlist
from services.spotify_client import SpotifyClient  # For creation of playlist

class PlaylistWorker(QThread):
    finished = pyqtSignal(list, str)  # tracks, playlist_url
    error = pyqtSignal(str)
    
    def __init__(self, mood, limit):
        super().__init__()
        self.mood = mood
        self.limit = limit

    def run(self):
        try:
            # Generate tracks
            tracks = generate_playlist(self.mood, limit=self.limit)
            if not tracks:
                self.finished.emit([], "")
                return

            # Create Spotify playlist and add items
            spotify = SpotifyClient()
            user = spotify.sp.current_user()
            user_id = user["id"]

            playlist = spotify.sp.user_playlist_create(
                user=user_id,
                name=f"Mood: {self.mood}",
                public=True,
                description=f"Dynamic playlist for mood: {self.mood}"
            )

            uris = [t["uri"] for t in tracks if t.get("uri")]
            # Add in chunks of 100
            for i in range(0, len(uris), 100):
                spotify.sp.playlist_add_items(playlist_id=playlist["id"], items=uris[i:i+100])

            playlist_url = playlist["external_urls"]["spotify"]

            self.finished.emit(tracks, playlist_url)
        except Exception as e:
            self.error.emit(str(e))

class PlaylistApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotify Mood Playlist Generator")
        self.setGeometry(200, 200, 700, 500)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        
        input_layout = QHBoxLayout()
        self.mood_label = QLabel("Mood / Keywords:")
        self.mood_input = QLineEdit()
        self.limit_label = QLabel("Number of tracks:")
        self.limit_spin = QSpinBox()
        self.limit_spin.setRange(5, 30)
        self.limit_spin.setValue(20)
        self.generate_btn = QPushButton("Generate Playlist")
        self.generate_btn.clicked.connect(self.start_generation)
        input_layout.addWidget(self.mood_label)
        input_layout.addWidget(self.mood_input)
        input_layout.addWidget(self.limit_label)
        input_layout.addWidget(self.limit_spin)
        input_layout.addWidget(self.generate_btn)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)

        self.tracks_display = QTextEdit()
        self.tracks_display.setReadOnly(True)
        
        link_layout = QHBoxLayout()
        self.link_label = QLabel("Playlist link:")
        self.link_link = QLabel("")
        self.link_link.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.link_link.setOpenExternalLinks(True)
        link_layout.addWidget(self.link_label)
        link_layout.addWidget(self.link_link)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.tracks_display)
        main_layout.addLayout(link_layout)

        self.setLayout(main_layout)

    def start_generation(self):
        mood = self.mood_input.text().strip()
        limit = self.limit_spin.value()
        if not mood:
            QMessageBox.warning(self, "Input Error", "Please enter a mood or keywords.")
            return

        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(50)
        self.generate_btn.setEnabled(False)
        self.tracks_display.clear()
        self.link_link.clear()

        self.worker = PlaylistWorker(mood, limit)
        self.worker.finished.connect(self.display_playlist)
        self.worker.error.connect(self.show_error)
        self.worker.start()

    def display_playlist(self, tracks, playlist_url):
        self.progress_bar.setValue(100)
        self.generate_btn.setEnabled(True)

        if not tracks:
            self.tracks_display.setPlainText("No tracks found.")
            self.progress_bar.setVisible(False)
            return

        track_text = "\n".join([f"{t['name']} - {t['artist']}" for t in tracks])
        self.tracks_display.setPlainText(track_text)

        # Real playlist URL returned by Spotify API
        self.link_link.setText(f"<a href='{playlist_url}'>{playlist_url}</a>")

        self.progress_bar.setVisible(False)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", f"Error generating playlist: {message}")
        self.generate_btn.setEnabled(True)
        self.progress_bar.setVisible(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlaylistApp()
    window.show()
    sys.exit(app.exec_())
