import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout, QLabel
import MediaPlayer
import AudioFile


class Graph():
    def __init__(self, MainWindow, centralWidget):
        super().__init__()
        self.MainWindow = MainWindow
        self.plot_widget = CustomPlotWidget(self, centralWidget)
        self.plot_widget.setBackground('#2E2E2E')  
        self.audio = AudioFile.AudioFile()
        self.media_player = MediaPlayer.AudioPlayerWidget()
        self.media_player.media_player.positionChanged.connect(self.update_shading_region)
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Song")

        self.shading_region = pg.LinearRegionItem([0, 0], brush=(50, 50, 200, 50), pen="r")
        self.shading_region.setMovable(False)
        self.plot_widget.addItem(self.shading_region)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.plot_widget)
        self.layout.addWidget(self.media_player)
        self.is_paused = False
        self.is_off = False

    def load_audio(self):
        self.audio.load_song()
        if self.audio.time_data is not None and self.audio.audio is not None:
            self.plot_widget.clear()
            self.plot_widget.addItem(self.shading_region)
            self.plot_widget.plot(self.audio.time_data, self.audio.audio, pen = '#df78ef')    
            self.media_player.update_song(self.audio.file_path)    
            self.title_label.setText(self.audio.song_name)
            self.set_plot_limits()
            self.MainWindow.detect_song()
            self.MainWindow.update_weights_label(self.MainWindow.weights_slider.value())

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
                yMin = 1.2 * y_min, yMax = 1.2 * y_max
            )
            
    def update_shading_region(self, value):
        """Update playback line and shading region."""
        current_time = value/1000
        self.shading_region.setRegion([0, current_time])
    
    def reset_shading_region(self):
        self.shading_region.setRegion([0, 0])


class CustomPlotWidget(pg.PlotWidget):
    def __init__(self, graph, parent=None):
        super().__init__(parent)
        self.graph = graph

    def mouseDoubleClickEvent(self, event):
        if event.button() == 1:  
            self.graph.load_audio()
