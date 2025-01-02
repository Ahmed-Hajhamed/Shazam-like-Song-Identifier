from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QLabel, QGridLayout, QFrame, QSlider, QTableWidget, QWidget, QSizePolicy)

import Graph

STYLESHEET = """
QLabel {
    font-size: 17px;
}
QTableWidget { font-size: 16px; }

"""

class Ui_MainWindow(object):
    def setup_UI(self, MainWindow):
        MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 766)
        MainWindow.setStyleSheet(STYLESHEET)
        self.centralwidget = QWidget()

        self.song_1_graph = Graph.Graph(MainWindow, self.centralwidget)
        self.song_2_graph = Graph.Graph(MainWindow, self.centralwidget)

        self.song_1_graph.media_player.set_other_players([self.song_2_graph.media_player])
        self.song_2_graph.media_player.set_other_players([self.song_1_graph.media_player])

        self.main_layout =  QGridLayout()
        self.table_layout = QGridLayout()
        self.sliders_layout = QGridLayout()
        self.controls_layout = QGridLayout()

        self.weights_slider = QSlider()
        self.weights_slider.setOrientation(Qt.Horizontal)
        self.weights_slider.setMaximum(100)
        self.weights_slider.setValue(50)
        self.weights_slider.valueChanged.connect(self.update_weights_label)

        self.table_label =  QLabel("Matches Table")
        self.song_1_weight_label = QLabel(f"Song 1 {self.weights_slider.value()}%")
        self.song_2_weight_label = QLabel(f"{100 - self.weights_slider.value()}% Song 2")
        self.slider_weight_label = QLabel("Weights:")

        self.table_Widget = QTableWidget()
        self.table_Widget.setRowCount(10)
        self.table_Widget.setColumnCount(2)
        self.table_Widget.setHorizontalHeaderLabels(["Songs", "Similarity %"])
        self.table_Widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.line_1 =  create_line(horizontal= True)
        self.line_2 =  create_line()
        self.line_3 = create_line(horizontal= True)

        self.table_layout.addWidget(self.table_label, 0, 0)
        self.table_layout.addWidget(self.table_Widget, 1, 0)

        self.sliders_layout.addWidget(self.song_2_weight_label, 1, 2, 1, 1)
        self.sliders_layout.addWidget(self.weights_slider, 1, 1, 1, 1)
        self.sliders_layout.addWidget(self.song_1_weight_label, 1, 0, 1, 1)
        self.sliders_layout.addWidget(self.slider_weight_label, 0, 0, 1, 3)

        self.main_layout.addLayout(self.sliders_layout, 0, 0, 1, 3)
        self.main_layout.addWidget(self.line_1, 1, 0, 1, 3)
        self.main_layout.addWidget(self.line_2, 2, 1, 3, 1)
        self.main_layout.addWidget(self.line_3, 3, 2, 1, 1)
        self.main_layout.addLayout(self.table_layout, 2, 0, 3, 1)
        self.main_layout.addLayout(self.song_1_graph.layout, 2, 2, 1, 1)
        self.main_layout.addLayout(self.song_2_graph.layout, 4, 2, 1, 1)

        self.centralwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.centralwidget)

    def update_weights_label(self, value):
        self.song_1_weight_label.setText(f"{self.song_1_graph.audio_file.song_name} {value}%")
        self.song_2_weight_label.setText(f"{100 - value}% {self.song_2_graph.audio_file.song_name}")

def create_line(horizontal = False, thick = True):
        line = QFrame() 
        line.setFrameShape(QFrame.HLine) if horizontal else line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        if thick: line.setStyleSheet("border: 1px solid purple;")
        return line
