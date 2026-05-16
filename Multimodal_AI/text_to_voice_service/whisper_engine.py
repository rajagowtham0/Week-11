import os

# Local FFmpeg path
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

import whisper

print("Loading Whisper model...")

# Load Whisper model
model = whisper.load_model("medium")

print("Whisper model loaded successfully")


def transcribe_audio(audio_path):

    # Original language transcription
    transcription_result = model.transcribe(
        audio_path,
        task="transcribe"
    )

    # English translation
    translation_result = model.transcribe(
        audio_path,
        task="translate"
    )

    return {
        "detected_language": transcription_result["language"],
        "original_transcription": transcription_result["text"].strip(),
        "english_translation": translation_result["text"].strip()
    }