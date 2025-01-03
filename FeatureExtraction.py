import librosa
import imagehash
from PIL import Image
import os
import pandas as pd

song_names = []
mel_spectrograms = []
mfcc_features = []
chroma_features = []

def extract_fratures(song_path: str= None, audio = None, sampling_rate = 22050):
    song_name = ""
    if song_path is not None:
        song_name =  (os.path.splitext(os.path.basename(song_path))[0])
        audio, sampling_rate = librosa.load(song_path, duration= 30)

    if audio is not None:
        mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sampling_rate)
        mfcc_feature = librosa.feature.mfcc(y=audio, sr=sampling_rate)
        chroma_stft_feature = librosa.feature.chroma_stft(y=audio, sr=sampling_rate)

        mel_spectrogram = hash_feature(mel_spectrogram)
        mfcc_feature = hash_feature(mfcc_feature)
        chroma_stft_feature = hash_feature(chroma_stft_feature)

        song_names.append(song_name)
        mel_spectrograms.append(mel_spectrogram)
        mfcc_features.append(mfcc_feature)
        chroma_features.append(chroma_stft_feature)

        return mel_spectrogram, mfcc_feature, chroma_stft_feature

def process_folder(audio_folder_path: str):
    for audio_file in os.listdir(audio_folder_path):
        if audio_file.endswith('.mp3') or audio_file.endswith('.wav'):
            file_path = os.path.join(audio_folder_path, audio_file)
            extract_fratures(file_path)
            print(f"Processed: {audio_file}")

    song_features_dict = {'Song Name': song_names ,'Mel Spectrogram':mel_spectrograms,
                           'MFCC Feature': mfcc_features, 'Chroma STFT': chroma_features}

    data_frame = pd.DataFrame(song_features_dict)
    data_frame.to_csv('Database/Songs_database.csv', index=False, header=False)

def hash_feature(feature):
    hashed_feature = imagehash.phash((Image.fromarray(feature)), hash_size=16).__str__()
    return hashed_feature

# process_folder("Task 5 Data")
