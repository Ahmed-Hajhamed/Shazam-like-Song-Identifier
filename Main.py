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
        self.start_button.clicked.connect(self.detect_song)

    def mix_songs(self):
        self.mixed_audio = self.song_1_graph.audio.audio * self.weights_slider.value()/ 100.0 + \
                                        self.song_2_graph.audio.audio * (1 - self.weights_slider.value()/ 100.0)

    def detect_song(self):
        similarity_indices = []
        mixed_song_mel_spectrogram, mixed_song_mfcc_feature, mixed_song_chroma_stft_feature =\
                                                     extract_fratures(audio= self.mixed_audio)
        
        song_names, mel_spectrograms, mfcc_features, chroma_stft_features = [], [], [], []

        songs_data = csv.reader(open('Database/Songs_database.csv', 'r'), delimiter=",")

        for coloumn in songs_data:
            song_names.append(coloumn[0])
            mel_spectrograms.append(coloumn[1])
            mfcc_features.append(coloumn[2])
            chroma_stft_features.append(coloumn[3])
        
        for i in range(len(song_names)):
            mel_spectrogram_difference = hex_to_hash(mel_spectrograms[i]) - hex_to_hash(mixed_song_mel_spectrogram)
            mfcc_feature_difference = hex_to_hash(mfcc_features[i]) - hex_to_hash(mixed_song_mfcc_feature)
            chroma_stft_feature_difference = hex_to_hash(chroma_stft_features[i]) - hex_to_hash(mixed_song_chroma_stft_feature)

            average_difference = ((mel_spectrogram_difference + mfcc_feature_difference + chroma_stft_feature_difference)/3)

            similarity_index = (1 - average_difference/255)*100
            similarity_indices.append([song_names[i] , similarity_index])

        similarity_indices.sort(key=lambda x:x[1])
        self.similarity_indices = list(reversed(similarity_indices))

    def show_results(self):
            for row in range(10):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(self.similarity_indices[row][0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(round(self.similarity_indices[row][1], 2)) + "%"))
                self.tableWidget.verticalHeader().setSectionResizeMode(row, QHeaderView.Stretch)

            self.tableWidget.setHorizontalHeaderLabels(["Found Matches", "Percentage"])

            for col in range(2):
                self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, "dark_purple.xml")
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
