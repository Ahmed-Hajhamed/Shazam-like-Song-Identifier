from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QLabel, QGridLayout, QFrame, QSlider,
                             QPushButton, QTableWidget, QWidget)
import Graph

class Ui_MainWindow(object):
    def setup_UI(self, MainWindow):
        MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 766)
        self.centralwidget = QWidget()

        self.song_1_graph = Graph.Graph(self.centralwidget)
        self.song_2_graph = Graph.Graph(self.centralwidget)

        self.song_1_play_button = QPushButton("Play")
        self.song_1_reset_button_2 = QPushButton("Reset")
        self.song_2_play_button = QPushButton("Play")
        self.song_2_reset_button = QPushButton("Reset")
        self.start_button = QPushButton("Start")

        self.main_layout =  QGridLayout()
        self.table_layout = QGridLayout()
        self.sliders_layout = QGridLayout()
        self.song_2_layout = QGridLayout()
        self.controls_layout = QGridLayout()
        self.song_1_layout = QGridLayout()

        self.table_label =  QLabel("Matches Table")
        self.song_1_weight_label = QLabel("Song 1 100%")
        self.song_2_weight_label = QLabel("0% Song 2")
        self.slider_weight_label = QLabel("Weights")
        self.song_1_label = QLabel("Song 1")
        self.song_2_label = QLabel("Song 2")
        
        self.song_1_label.setFixedHeight(30)
        self.song_2_label.setFixedHeight(30)

        self.weights_slider = QSlider()
        self.weights_slider.setOrientation(Qt.Horizontal)
        self.weights_slider.setMaximum(100)
        self.weights_slider.setValue(50)
        self.weights_slider.valueChanged.connect(self.update_weights_label)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Songs", "Similarity Percentage"])

        self.line_1 =  create_line(horizontal= True)
        self.line_2 =  create_line()
        self.line_3 = create_line()
        self.line_4 = create_line(horizontal= True)
        self.line_5 = create_line(horizontal= True)

        self.table_layout.addWidget(self.table_label, 0, 0)
        self.table_layout.addWidget(self.tableWidget, 1, 0)

        self.sliders_layout.addWidget(self.song_2_weight_label, 1, 2, 1, 1)
        self.sliders_layout.addWidget(self.weights_slider, 1, 1, 1, 1)
        self.sliders_layout.addWidget(self.song_1_weight_label, 1, 0, 1, 1)
        self.sliders_layout.addWidget(self.slider_weight_label, 0, 0, 1, 3)

        self.song_1_layout.addWidget(self.song_1_reset_button_2, 3, 1, 1, 1)
        self.song_1_layout.addWidget(self.song_1_graph.plot_widget, 2, 0, 2, 1)
        self.song_1_layout.addWidget(self.song_1_play_button, 2, 1, 1, 1)
        self.song_1_layout.addWidget(self.song_1_label, 0, 0, 1, 2)

        self.song_2_layout.addWidget(self.song_2_reset_button, 8, 1, 1, 1)
        self.song_2_layout.addWidget(self.song_2_play_button, 7, 1, 1, 1)
        self.song_2_layout.addWidget(self.song_2_graph.plot_widget, 7, 0, 2, 1)
        self.song_2_layout.addWidget(self.song_2_label, 5, 0, 1, 2)

        self.controls_layout.addWidget(self.start_button, 0, 0, 1, 1)

        self.main_layout.addLayout(self.song_1_layout, 0, 2, 1, 1)
        self.main_layout.addLayout(self.controls_layout, 4, 0, 1, 1)
        self.main_layout.addLayout(self.song_2_layout, 2, 2, 1, 1)
        self.main_layout.addLayout(self.sliders_layout, 4, 2, 1, 1)
        self.main_layout.addWidget(self.line_2, 0, 1, 3, 1)
        self.main_layout.addWidget(self.line_4, 3, 0, 1, 1)
        self.main_layout.addWidget(self.line_3, 4, 1, 1, 1)
        self.main_layout.addWidget(self.line_1, 3, 2, 1, 1)
        self.main_layout.addLayout(self.table_layout, 0, 0, 3, 1)
        self.main_layout.addWidget(self.line_5, 1, 2, 1, 1)
        self.centralwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.centralwidget)

    def update_weights_label(self, value):
        self.song_1_weight_label.setText(f"{self.song_1_graph.audio.song_name} {value}%")
        self.song_2_weight_label.setText(f"{100 - value}% {self.song_2_graph.audio.song_name}")

def create_line(horizontal = False, thick = True):
        line = QFrame() 
        line.setFrameShape(QFrame.HLine) if horizontal else line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        if thick: line.setStyleSheet("border: 1px solid white;")
        return line
