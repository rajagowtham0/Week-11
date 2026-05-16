from fastapi import FastAPI, UploadFile, File
import tempfile
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

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    try:

        content = await file.read()

        temp_file.write(content)

        temp_file.close()

        result = transcribe_audio(temp_file.name)

        return {
            "status": "success",
            "filename": file.filename,
            "detected_language": result["language"],
            "transcript": result["transcript"]
        }

    finally:

        os.unlink(temp_file.name)