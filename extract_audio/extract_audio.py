from pydub import AudioSegment
import random


def extract_audio(audio, length):

    """
    Extracts a random audio clip of a specified duration from a WAV file
    and saves it.

    Parameters:
    ----------
    audio : str
        Path to the input WAV audio file.
    length : int
        Length of the clip to extract, in milliseconds.

    Raises:
    ------
    ValueError
        If the input audio file is shorter than the requested clip length.

    Notes:
    -----
    - The function randomly selects a starting point for the clip.
    - The extracted clip is saved as 'random_clip.wav' in the
    current directory.
    - This function only works with WAV files.
    """

    # Load your audio file (make sure it's in the same directory as
    # extract_audio.py or provide the full path)
    audio = AudioSegment.from_wav(audio)

    # Duration of the audio in milliseconds
    duration = len(audio)

    # Duration of the clip you want to extract (in ms)
    clip_duration = length

    # Make sure the clip fits in the audio
    if duration < clip_duration:
        raise ValueError("Audio file is too short for a 0.5-second clip.")

    # Choose a random start point
    start = random.randint(0, duration - clip_duration)
    end = start + clip_duration

    # Slice the audio
    clip = audio[start:end]

    # Export the extracted clip
    clip.export("random_clip.wav", format="wav")

    print(f"Extracted 0.5-second clip from {start}ms to {end}ms.")
