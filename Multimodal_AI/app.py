from fastapi import FastAPI, UploadFile, File
import shutil
import os

from text_to_voice_service.whisper_engine import transcribe_audio

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Voice-to-Text API Running Successfully"
    }


@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):

    os.makedirs("sample_audio", exist_ok=True)

    file_path = f"sample_audio/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = transcribe_audio(file_path)

    return {
        "status": "success",
        "filename": file.filename,
        "detected_language": result["language"],
        "transcript": result["transcript"]
    }