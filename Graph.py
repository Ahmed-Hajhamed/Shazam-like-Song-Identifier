import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout, QLabel
import MediaPlayer
import AudioFile


class Graph():
    def __init__(self, MainWindow, centralWidget):
        super().__init__()
        self.MainWindow = MainWindow
        self.plot_widget = CustomPlotWidget(self, centralWidget)
        self.audio_file = AudioFile.AudioFile()
        self.media_player = MediaPlayer.AudioPlayerWidget()
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Double-click To Load a Song")
        self.shading_region = pg.LinearRegionItem([0, 0], brush=(50, 50, 200, 50), pen="r")

        self.shading_region.setMovable(False)
        self.plot_widget.addItem(self.shading_region)
        self.media_player.media_player.positionChanged.connect(self.update_shading_region)

        self.plot_widget.setBackground('#2E2E2E')  
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.plot_widget)
        self.layout.addWidget(self.media_player)
        self.is_paused = False
        self.is_off = False

    def load_audio(self, path = None):
        self.audio_file.load_song(path)
        if self.audio_file.time_data is not None and self.audio_file.audio_data is not None:
            self.plot_widget.clear()
            self.plot_widget.addItem(self.shading_region)
            self.plot_widget.plot(self.audio_file.time_data, self.audio_file.audio_data, pen = '#df78ef')    
            self.media_player.update_song(self.audio_file.file_path)    
            self.title_label.setText(self.audio_file.song_name)
            self.set_plot_limits()
            self.MainWindow.detect_song()
            self.MainWindow.update_weights_label(self.MainWindow.weights_slider.value())

    def set_plot_limits(self):
        """Set the plot limits based on the loaded data."""
        if len(self.audio_file.time_data)>0:
            x_max = self.audio_file.time_data[-1]

            y_min = min(self.audio_file.audio_data)
            y_max = max(self.audio_file.audio_data)

            y_min = y_min - y_min * 0.2 if y_min > 0 else y_min + y_min * 0.2

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
