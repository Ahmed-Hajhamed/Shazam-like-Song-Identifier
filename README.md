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
   https://github.com/Ahmed-Hajhamed/Shazam-like-Song-Identifier.git

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
-Run the application:
    ```bash
    python app.py
    ```

- Load songs by double-clicking the graphs.
- Mix songs using the slider to adjust the weighted average.
- View matching results in the table.
- Use the media players to listen to and seek through the songs.
- To create a custom database of music:
  1. Add your folder of music to ```bash process_folder("path_to_folder")``` function in FeatureExtraction.py. Make sure all audio files are in the subfolder.
  2. Run ```bash FeatureExtraction.py ``` to create the database and you are ready to go!


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
![Python 3 11 12_30_2024 11_28_22 PM](https://github.com/user-attachments/assets/78cb942b-21a5-44cc-a3d2-176bd2c7bfd7)

**Adjust The Weight of Each Song**
![Python 3 11 12_30_2024 11_30_05 PM](https://github.com/user-attachments/assets/23506d94-4489-4406-b30c-1d81e7f77cb1)

**Interactive Media Player**
![Python 3 11 12_30_2024 11_28_35 PM](https://github.com/user-attachments/assets/da41ea4c-9453-41a7-a2c0-cceca1c1b16d)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or bug fixes.

## Contact
For questions or support, please reach out via the GitHub issues page or email: ahmed.hajhamed03@eng-st.cu.edu.eg.
