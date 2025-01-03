from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
import UI
from qt_material import apply_stylesheet
import csv
from FeatureExtraction import extract_fratures
from imagehash import hex_to_hash


class Main(UI.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_UI(self)
        self.mixed_audio = None
        self.number_of_songs: int = 0
        self.weights_slider.sliderReleased.connect(self.identify_song)
        self.load_database()

    def load_database(self):
        self.song_names, self.mel_spectrograms, self.mfcc_features, self.chroma_stft_features = [], [], [], []

        songs_data = csv.reader(open('Database/Songs_database.csv', 'r'), delimiter=",")

        for coloumn in songs_data:
            self.song_names.append(coloumn[0])
            self.mel_spectrograms.append(coloumn[1])
            self.mfcc_features.append(coloumn[2])
            self.chroma_stft_features.append(coloumn[3])

    def mix_songs(self):
        if self.song_1_graph.audio_file.audio_data is None and self.song_2_graph.audio_file.audio_data is not None:
            self.mixed_audio =  self.song_2_graph.audio_file.audio_data
            self.weights_slider.setValue(0)
            self.weights_slider.setDisabled(True)
            self.number_of_songs = 1

        elif  self.song_2_graph.audio_file.audio_data is None and self.song_1_graph.audio_file.audio_data is not None:
            self.mixed_audio =  self.song_1_graph.audio_file.audio_data
            self.weights_slider.setValue(100)
            self.weights_slider.setDisabled(True)
            self.number_of_songs = 1

        elif self.song_1_graph.audio_file.audio_data is not None and self.song_2_graph.audio_file.audio_data is not None:
            self.weights_slider.setEnabled(True)
            if self.number_of_songs == 1:
                self.weights_slider.setValue(50)
                self.number_of_songs = 2

            self.mixed_audio = self.song_1_graph.audio_file.audio_data * self.weights_slider.value()/ 100.0 + \
                                        self.song_2_graph.audio_file.audio_data * (1 - self.weights_slider.value()/ 100.0)

    def identify_song(self):
        self.mix_songs()

        if self.mixed_audio is not None:
            similarity_indices = []
            mixed_song_mel_spectrogram, mixed_song_mfcc_feature, mixed_song_chroma_stft_feature =\
                                                        extract_fratures(audio= self.mixed_audio)
                
            for i in range(len(self.song_names)):
                mel_spectrogram_difference = hex_to_hash(self.mel_spectrograms[i]) - hex_to_hash(mixed_song_mel_spectrogram)
                mfcc_feature_difference = hex_to_hash(self.mfcc_features[i]) - hex_to_hash(mixed_song_mfcc_feature)
                chroma_stft_feature_difference = hex_to_hash(self.chroma_stft_features[i]) - hex_to_hash(mixed_song_chroma_stft_feature)

                average_difference = ((mel_spectrogram_difference + mfcc_feature_difference + chroma_stft_feature_difference)/3)

                similarity_index = (1 - average_difference/255) * 100
                similarity_indices.append([self.song_names[i] , similarity_index])

            similarity_indices.sort(key=lambda x:x[1])
            self.similarity_indices = list(reversed(similarity_indices))
            self.show_results()

    def show_results(self):
            for row in range(10):
                self.table_Widget.setItem(row, 0, QTableWidgetItem(self.similarity_indices[row][0]))
                self.table_Widget.setItem(row, 1, QTableWidgetItem(str(round(self.similarity_indices[row][1], 2)) + "%"))
                self.table_Widget.verticalHeader().setSectionResizeMode(row, QHeaderView.Stretch)

            for coloumn in range(2):
                self.table_Widget.horizontalHeader().setSectionResizeMode(coloumn, QHeaderView.Stretch)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, "dark_purple.xml")
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
