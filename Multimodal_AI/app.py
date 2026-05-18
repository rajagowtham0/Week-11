from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from text_to_voice_service.whisper_engine import (
    transcribe_audio
)

from image_to_text_service.ocr_engine import (
    extract_text
)

# Create FastAPI app
app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Multimodal AI Services Running Successfully"
    }


# Voice-to-Text Endpoint

@app.post("/speech-to-text")
async def speech_to_text(
    file: UploadFile = File(...)
):

    temp_file = None

    try:

        # Supported audio formats
        allowed_audio_formats = [
            ".wav",
            ".mp3",
            ".m4a"
        ]

        # Get extension
        file_extension = os.path.splitext(
            file.filename
        )[1].lower()

        # Validate audio format
        if file_extension not in allowed_audio_formats:

            return {
                "status": "error",
                "message": "Unsupported audio format"
            }

        # Create temp audio file
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=file_extension,
            mode="wb"
        )

        # Read uploaded file
        content = await file.read()

        # Write audio
        temp_file.write(content)

        temp_file.close()

        # Whisper transcription
        result = transcribe_audio(
            temp_file.name
        )

        return {

            "status": "success",

            "service": "voice_to_text",

            "input_filename":
                file.filename,

            "detected_language_code":
                result.get(
                    "detected_language_code"
                ),

            "detected_language":
                result.get(
                    "detected_language"
                ),

            "original_transcription":
                result.get(
                    "original_transcription"
                ),

            "english_translation":
                result.get(
                    "english_translation"
                )
        }

    except Exception as e:

        return {

            "status": "error",

            "service": "voice_to_text",

            "message": str(e)
        }

    finally:

        # Delete temp file
        if temp_file is not None:

            if os.path.exists(
                temp_file.name
            ):

                os.unlink(
                    temp_file.name
                )


# OCR / Picture-to-Text Endpoint

@app.post("/ocr")
async def ocr_extraction(
    file: UploadFile = File(...)
):

    temp_file = None

    try:

        # Supported image formats
        allowed_image_formats = [
            ".png",
            ".jpg",
            ".jpeg"
        ]

        # Get extension
        file_extension = os.path.splitext(
            file.filename
        )[1].lower()

        # Validate image format
        if file_extension not in allowed_image_formats:

            return {
                "status": "error",
                "message": "Unsupported image format"
            }

        # Create temp image file
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=file_extension,
            mode="wb"
        )

        # Read uploaded image
        content = await file.read()

        # Write image
        temp_file.write(content)

        temp_file.close()

        # OCR extraction
        extracted_text = extract_text(
            temp_file.name
        )

        return {

            "status": "success",

            "service": "ocr_picture_to_text",

            "input_filename":
                file.filename,

            "extracted_text":
                extracted_text
        }

    except Exception as e:

        return {

            "status": "error",

            "service": "ocr_picture_to_text",

            "message": str(e)
        }

    finally:

        # Delete temp file
        if temp_file is not None:

            if os.path.exists(
                temp_file.name
            ):

                os.unlink(
                    temp_file.name
                )