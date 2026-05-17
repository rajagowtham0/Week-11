from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from text_to_voice_service.whisper_engine import transcribe_audio
from image_to_text_service.ocr_engine import extract_text

# Create FastAPI app
app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Multimodal AI Services Running Successfully"
    }


# ==========================================
# Voice-to-Text Endpoint
# ==========================================

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

        # Write audio into temporary file
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


# ==========================================
# OCR / Picture-to-Text Endpoint
# ==========================================

@app.post("/ocr")
async def ocr_extraction(file: UploadFile = File(...)):

    # Create temporary image file
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    try:

        # Read uploaded image
        content = await file.read()

        # Write image into temporary file
        temp_file.write(content)

        temp_file.close()

        # Extract text using OCR
        extracted_text = extract_text(temp_file.name)

        return {
            "status": "success",
            "input_filename": file.filename,
            "extracted_text": extracted_text
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

    finally:

        # Delete temporary image file
        os.unlink(temp_file.name)