# Shazam-like Song Identifier

A Python desktop application that identifies songs and enables users to mix songs with weighted averages. It provides advanced analysis and matching features using mel-spectrogram, MFCC, and chroma-STFT, with perceptual hashing for efficient comparison.

---

## Features

- **Song Visualization**:
  - Double-click on a graph to load a song.
- **Song Mixing**:
  - Use a slider to add a weighted average between two songs.
- **Song Matching**:
  - A table on the left displays top matches for the uploaded or mixed song.
- **Media Player**:
  - Small players for each song with play, pause, reset, and seek functionalities.
- **Custom Database**:
  - Users can build a custom database by running `FeatureExtraction.py` after adding their folder of music.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo-name.git

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
-Run the application:
    ```bash
    python app.py
    ```

-Load songs by double-clicking the graphs.
-Mix songs using the slider to adjust the weighted average.
-View matching results in the table.
-Use the media players to listen to and seek through the songs.
-To create a custom database:
-Add your folder of music to the appropriate directory.
-Run ```bash FeatureExtraction.py ``` to extract features.

Requirements
Python: Version 3.8 or higher
Libraries:
librosa
PyQt5
numpy
pyqtgraph
qt_material
ImageHash
pandas

## Screenshots

**Load Songs By Double-Clicking on Graphs**
![alt text](<Python 3.11 12_30_2024 11_28_22 PM-1.png>)
**Adjust The Weight of Each Song**
![alt text](<Python 3.11 12_30_2024 11_30_05 PM.png>)
**Interactive Media Player**
![alt text](<Python 3.11 12_30_2024 11_28_35 PM.png>)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or bug fixes.

## Contact
For questions or support, please reach out via the GitHub issues page or email: ahmed.hajhamed03@eng-st.cu.edu.eg.