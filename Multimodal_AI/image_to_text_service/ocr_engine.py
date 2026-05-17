import easyocr
import cv2
import numpy as np

print("Loading OCR model...")

reader = easyocr.Reader(['en'])

print("OCR model loaded successfully")


def extract_text(image_path):

    # Read image
    image = cv2.imread(image_path)

    # OCR extraction
    results = reader.readtext(image)

    extracted_text = []

    for result in results:

        text = result[1]

        extracted_text.append(text)

    final_text = " ".join(extracted_text)

    return final_text