## Multimodal CCMS_AI

Multimodal CCMS_AI is a reusable healthcare-oriented multimodal AI backend system developed using FastAPI.  
The project integrates:

1. Multilingual Voice-to-Text Conversion
2. OCR-Based Picture-to-Text Extraction
3. Clinical Audio Processing
4. Clinical Document Digitization



## Finalised libraries for the project
1. fastapi-Backend API framework
2. uvicorn-ASGI server for FastAPI
3. openai-whisper-Speech-to-text model
4. torch-Deep learning backend
5. torchaudio-Audio processing support
6. torchvision-Torch utility package
7. easyocr-OCR text extraction
8. opencv-python-Image preprocessing
9. pillow-Image handling
10. numpy-Numerical operations
11. Python-multipart-File upload handling in APIs
12. pydantic-Data validation for API responses

# Folder and File Explanation

## app.py

Main FastAPI application file.

## requirements.txt

Contains all required Python libraries and dependencies needed to run the project.
## text_to_voice_service/

This folder contains all speech-processing modules.

### whisper_engine.py

Core multilingual speech-to-text engine.

## image_to_text_service/

This folder contains OCR-related modules.

### ocr_engine.py

Core OCR extraction engine.

# sample_audio/

Contains sample multilingual audio files used for testing.

# sample_images/

Contains sample OCR test images.


# Speech to text API

## Supported Formats

- .wav
- .mp3
- .m4a

## Features

1. Multilingual transcription
2. Automatic language detection
3. English translation

## Sample response

{
  "service": "voice_to_text",
  "input_filename": "Tamil_cough.mp3",
  "detected_language": "Tamil",
  "original_transcription": "நோயாளைக்கு இறுமல் மற்றும் தலை வலி உளது",
  "english_translation": "The patient has a headache and dizziness."
}


# OCR / Picture-to-Text API

## Supported Formats

- .png
- .jpg
- .jpeg

## Features

- Prescription OCR
- Clinical text extraction
- Report digitization

## Sample Response

json Structured
{
  "service": "ocr_picture_to_text",
  "input_filename": "hairloss_prescription_1.png",
  "extracted_text": "Dermatology Prescription Patient Karthik M Diagncsis Hair Lccs 1. Minoxidil5% Solution Twice daily 2. Biotin Tablets-Once daily 3. Protein-rich dietadvised Reviewafter 30 days"
}
