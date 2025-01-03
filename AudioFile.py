from PyQt5.QtWidgets import QFileDialog
import librosa
import os
import numpy as np


class AudioFile:
    def __init__(self):
        self.file_path = None
        self.audio_data = None
        self.sampling_rate = 22050
        self.time_data = None
        self.duration: int = 30
        self.song_name = "Song"
    
    def load_song(self, path: str = None):
        if path is None:
            file_path, _ = QFileDialog.getOpenFileName(
                None,  "Open File", "Task 5 Data", "Audio (*.wav *.mp3)"
            )
            self.file_path = file_path
            
        else: self.file_path = path

        if self.file_path:
            self.audio_data, self.sampling_rate = librosa.load(self.file_path, duration = self.duration, sr= self.sampling_rate)
            self.song_name =  (os.path.splitext(os.path.basename(self.file_path))[0])

            self.audio_data = np.pad(self.audio_data,
                                (0, self.duration * self.sampling_rate - len(self.audio_data)), "symmetric")
            
            self.time_data = np.linspace(0, len(self.audio_data)/ self.sampling_rate, len(self.audio_data))
