import pyqtgraph as pg
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import  QSize
import numpy as np
import AudioFile

def set_icon(button, icon_path):
    pixmap = QPixmap(icon_path)
    button.setIcon(QIcon(pixmap))
    button.setIconSize(QSize(30, 30))
    button.setFixedSize(30, 30)
    button.setStyleSheet("border: none; background-color: none;")

class Graph():

    def __init__(self, centralWidget):
        super().__init__()
        self.plot_widget = CustomPlotWidget(self, centralWidget)
        self.plot_widget.setBackground('#2E2E2E')  
        self.plot_widget.setMinimumHeight(300)
        self.audio = AudioFile.AudioFile()
        self.is_paused = False
        self.is_off = False

    def load_audio(self):
        self.audio.load_song()
        if self.audio.time_data is not None and self.audio.audio is not None:
            self.plot_widget.clear()
            self.plot_widget.plot(self.audio.time_data, self.audio.audio, pen = '#df78ef')        
            # self.set_plot_limits()

    def play_pause(self, play_pause_button):
        if self.is_paused:
            # set_icon(play_pause_button, "icons\pause.png")
            play_pause_button.setText("PAUSE")
        else:
            # set_icon(play_pause_button, "icons/play.png")
            play_pause_button.setText("PLAY")
        self.is_paused = not self.is_paused

    def off_signal(self):
        self.graph_1.setLimits(xMin=0, xMax=2, yMin=-2, yMax=2)

    def set_plot_limits(self):
        """Set the plot limits based on the loaded data."""
        if len(self.audio.time_data)>0:
            x_max = self.audio.time_data[-1]

            y_min = min(self.audio.audio)
            y_max = max(self.audio.audio)

            y_min = y_min - y_min * 0.8 if y_min > 0 else y_min + y_min * 0.8

            self.plot_widget.setLimits(
                xMin = -0.5, xMax = 2 * x_max,
                yMin = y_min, yMax = 1.5 * y_max
            )
            

class CustomPlotWidget(pg.PlotWidget):
    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.graph = graph

    def mouseDoubleClickEvent(self, event):
        if event.button() == 1:  
            self.graph.load_audio()
