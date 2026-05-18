import warnings
warnings.filterwarnings("ignore")

import easyocr
import cv2
import numpy as np

# Load OCR Model

print("Loading OCR model...")

reader = easyocr.Reader(
    ['en'],
    gpu=False
)

print("OCR model loaded successfully")


# OCR Extraction Function

def extract_text(image_path):

    try:

        # Read Image
        image = cv2.imread(image_path)

        # Validate image
        if image is None:

            return "Unable to read image"

        # Convert image to grayscale
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        # Resize image for better OCR accuracy
        gray = cv2.resize(
            gray,
            None,
            fx=3,
            fy=3,
            interpolation=cv2.INTER_CUBIC
        )

        # Denoise image
        gray = cv2.fastNlMeansDenoising(
            gray,
            None,
            10,
            7,
            21
        )

        # Adaptive thresholding
        processed_image = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            11
        )

        # OCR Extraction
        results = reader.readtext(
            processed_image,
            detail=1,
            paragraph=False
        )

        # Store extracted text
        extracted_text = []

        for result in results:

            # Safe validation
            if len(result) < 3:
                continue

            bounding_box = result[0]
            text = result[1]
            confidence = result[2]

            # Filter weak predictions
            if confidence >= 0.20:

                cleaned_text = text.strip()

                if cleaned_text != "":

                    extracted_text.append(cleaned_text)

        # Join all extracted text
        final_text = " ".join(extracted_text)

        # Remove extra spaces
        final_text = " ".join(final_text.split())

        # Handle empty detection
        if final_text == "":

            return "No text detected"

        return final_text

    except Exception as e:

        return f"OCR Extraction Error: {str(e)}"