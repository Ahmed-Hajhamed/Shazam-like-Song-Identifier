import librosa
import numpy as np
import os
import json

# Function to generate a spectrogram and extract features
def process_audio(file_path, duration=20.0):
    # Load the audio file (limit to the first 'duration' seconds)
    audio, sr = librosa.load(file_path, duration=duration)
    
    # Compute the spectrogram (magnitude of the STFT)
    spectrogram = np.abs(librosa.stft(audio))
    # Extract features from the spectrogram
    features = {
        "spectral_centroid": float(librosa.feature.spectral_centroid(S=spectrogram, sr=sr).mean()),
        "spectral_bandwidth": float(librosa.feature.spectral_bandwidth(S=spectrogram, sr=sr).mean()),
        "spectral_contrast": float(librosa.feature.spectral_contrast(S=spectrogram, sr=sr).mean()),
        "spectral_flatness": float(librosa.feature.spectral_flatness(S=spectrogram).mean()),
        "rms_energy": float(librosa.feature.rms(S=spectrogram).mean()),
    }
    
    return features

# Function to process all files in a folder and save features
def process_folder(audio_folder, output_file):
    all_features = {}
    for audio_file in os.listdir(audio_folder):
        if audio_file.endswith('.mp3') or audio_file.endswith('.wav'):
            file_path = os.path.join(audio_folder, audio_file)
            features = process_audio(file_path)
            all_features[audio_file] = features
            print(f"Processed: {audio_file}")
    
    # Save features to a JSON file
    with open(output_file, 'w') as f:
        json.dump(all_features, f, indent=4)
    print(f"Features saved to {output_file}")

# Example usage
audio_folder = 'Songs\\all'
output_file = "spectrogram_features_all__.json"
# process_folder(audio_folder, output_file)
process_audio("Songs\stan\Stan(instrumental).wav")
