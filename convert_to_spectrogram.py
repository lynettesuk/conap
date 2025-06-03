import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


# Load audio file
audio_path = 'example.wav'  # Replace with your file name
y, sr = librosa.load(audio_path, sr=None)

# Convert to mel spectrogram
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
S_dB = librosa.power_to_db(S, ref=np.max)

# Display the mel spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram')
plt.tight_layout()
plt.show()
