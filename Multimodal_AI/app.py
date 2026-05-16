from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from text_to_voice_service.whisper_engine import transcribe_audio

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Multilingual Voice-to-Text API Running Successfully"
    }


@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):

    # Create temporary audio file
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    try:

        # Read uploaded audio
        content = await file.read()

        # Write audio to temporary file
        temp_file.write(content)

        temp_file.close()

        # Process audio using Whisper
        result = transcribe_audio(temp_file.name)

        return {
            "status": "success",
            "input_filename": file.filename,
            "detected_language": result["detected_language"],
            "original_transcription": result["original_transcription"],
            "english_translation": result["english_translation"]
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

    finally:

        # Delete temporary file
        os.unlink(temp_file.name)