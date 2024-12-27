from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplication, QMainWindow, QLabel, QGridLayout, QFrame, QSlider,
                             QPushButton, QGraphicsView, QTableWidget, QWidget)
from qt_material import apply_stylesheet


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(1175, 766)
        self.centralwidget = QWidget()

        self.song_1_graph = QGraphicsView()
        self.song_2_graph = QGraphicsView()

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
        
        self.weights_slider = QSlider()
        self.weights_slider.setOrientation(Qt.Horizontal)
        self.weights_slider.setMaximum(100)
        self.weights_slider.setValue(100)
        self.weights_slider.valueChanged.connect(self.update_weights_label)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)

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
        self.song_1_layout.addWidget(self.song_1_graph, 2, 0, 2, 1)
        self.song_1_layout.addWidget(self.song_1_play_button, 2, 1, 1, 1)
        self.song_1_layout.addWidget(self.song_1_label, 0, 0, 1, 2)

        self.song_2_layout.addWidget(self.song_2_reset_button, 8, 1, 1, 1)
        self.song_2_layout.addWidget(self.song_2_play_button, 7, 1, 1, 1)
        self.song_2_layout.addWidget(self.song_2_graph, 7, 0, 2, 1)
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
        self.song_1_weight_label.setText(f"Song 1 {value}%")
        self.song_2_weight_label.setText(f"{100 - value}% Song 2")

def create_line(horizontal = False, thick = True):
        line = QFrame() 
        line.setFrameShape(QFrame.HLine) if horizontal else line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        if thick: line.setStyleSheet("border: 1px solid white;")
        return line

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, "dark_purple.xml")
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
