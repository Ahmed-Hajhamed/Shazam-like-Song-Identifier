from PyQt5.QtWidgets import QFileDialog
import librosa
import os
import numpy as np


class AudioFile:
    def __init__(self):
        self.audio = None
        self.sampling_rate = None
        self.song_name = "Song"
    
    def load_song(self):
        song_path, _ = QFileDialog.getOpenFileName(
            None,  "Open File", "", "All Files (*.*);;Text Files (*.txt);;Images (*.wav *.mp3)"
        )
        if song_path:
            self.audio, self.sampling_rate = librosa.load(song_path, duration= 30)
            self.song_name =  (os.path.splitext(os.path.basename(song_path))[0])
            self.time_data = np.linspace(0, len(self.audio)/ self.sampling_rate, len(self.audio))