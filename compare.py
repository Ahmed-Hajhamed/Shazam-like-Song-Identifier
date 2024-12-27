import numpy as np
import json
from scipy.spatial.distance import cosine

# Load fingerprints (with normalized features)
def load_fingerprints(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Compute similarity using cosine similarity
def compute_similarity(features1, features2):
    vector1 = np.array(list(features1.values()))
    vector2 = np.array(list(features2.values()))
    return 1 - cosine(vector1, vector2)  # Cosine similarity: 1 - cosine distance

# Compare an input song's features with all stored songs
def compare_songs(input_features, fingerprints):
    similarity_scores = {}
    for song, data in fingerprints.items():
        stored_features = data["normalized_features"]
        similarity_scores[song] = compute_similarity(input_features, stored_features)
    return similarity_scores

# Handle multiple input songs by averaging their similarity scores
def compare_multiple_songs(input_features_list, fingerprints):
    # Compute similarity for each input song
    all_scores = [compare_songs(features, fingerprints) for features in input_features_list]
    
    # Average scores across all input songs
    combined_scores = {}
    for scores in all_scores:
        for song, similarity in scores.items():
            combined_scores[song] = combined_scores.get(song, 0) + similarity
    for song in combined_scores:
        combined_scores[song] /= len(input_features_list)
    
    return combined_scores

# Example usage
fingerprints_file = "song_fingerprints_all.json"
fingerprints = load_fingerprints(fingerprints_file)

# Example: Features of input songs
# (Assume these are normalized features generated using the same pipeline)
input_features_list = [
{
            "spectral_centroid": 0.48766719888699317,
            "spectral_bandwidth": 0.6510773150253634,
            "spectral_contrast": 0.6380668706317858,
            "spectral_flatness": 1.0,
            "rms_energy": 0.2088413936974429
        },
    {
            "spectral_centroid": 0.4109133105605849,
            "spectral_bandwidth": 0.7488382209035563,
            "spectral_contrast": 0.6747822988103109,
            "spectral_flatness": 0.04324448253750454,
            "rms_energy": 0.4928607000926465
        }
]

# Compare and rank songs
similarity_scores = compare_multiple_songs(input_features_list, fingerprints)
sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

# Output sorted similarity scores
print("Similarity Scores:")
for song, score in sorted_scores:
    print(f"{song}: {score:.2f}")
