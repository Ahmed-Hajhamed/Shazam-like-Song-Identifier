import json
import numpy as np
from PIL import Image
import imagehash

# Step 1: Load features from JSON
def load_features(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Step 2: Normalize features
def normalize_features(features_dict):
    # Collect all feature values globally
    all_values = {key: [] for key in next(iter(features_dict.values())).keys()}
    for features in features_dict.values():
        for key, value in features.items():
            all_values[key].append(value)
    
    # Compute min-max for each feature
    min_max = {key: (min(values), max(values)) for key, values in all_values.items()}
    
    # Normalize features
    normalized_features = {}
    for song, features in features_dict.items():
        normalized_features[song] = {
            key: (value - min_max[key][0]) / (min_max[key][1] - min_max[key][0])
            for key, value in features.items()
        }
    
    return normalized_features

# Step 3: Generate perceptual hashes
def generate_hash(features):
    # Convert features to a small grayscale image
    feature_vector = np.array(list(features.values())).astype('float32')
    feature_image = (feature_vector * 255).reshape((1, -1))  # Single-row image
    image = Image.fromarray(feature_image).convert("L")
    
    # Generate perceptual hash
    return str(imagehash.phash(image))

# Step 4: Process all songs
def process_fingerprints(features_dict):
    normalized_features = normalize_features(features_dict)
    fingerprints = {
        song: {
            "normalized_features": features,
            "hash": generate_hash(features)
        }
        for song, features in normalized_features.items()
    }
    return fingerprints

# Step 5: Save fingerprints to a JSON file
def save_fingerprints(fingerprints, output_file):
    with open(output_file, 'w') as f:
        json.dump(fingerprints, f, indent=4)
    print(f"Fingerprints saved to {output_file}")

# Example usage
features_file = "spectrogram_features_all__.json"
fingerprints_file = "song_fingerprints_all__.json"

# Load, process, and save
features = load_features(features_file)
fingerprints = process_fingerprints(features)
save_fingerprints(fingerprints, fingerprints_file)
