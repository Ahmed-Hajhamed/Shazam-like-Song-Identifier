from PyQt5.QtWidgets import QFileDialog
import librosa
import os
import numpy as np


class AudioFile:
    def __init__(self):
        self.file_path = None
        self.audio = None
        self.sampling_rate = None
        self.time_data = None
        self.song_name = "Song"
    
    def load_song(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,  "Open File", "", "All Files (*.*);;Text Files (*.txt);;Images (*.wav *.mp3)"
        )
        self.file_path = file_path
        if self.file_path:
            self.audio, self.sampling_rate = librosa.load(self.file_path, duration= 30)
            self.song_name =  (os.path.splitext(os.path.basename(self.file_path))[0])
            self.time_data = np.linspace(0, len(self.audio)/ self.sampling_rate, len(self.audio))
