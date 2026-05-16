import os

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

import whisper

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Whisper model loaded successfully")


def transcribe_audio(audio_path):

    result = model.transcribe(
        audio_path,
        task="transcribe"
    )

    return {
        "transcript": result["text"],
        "language": result["language"]
    }