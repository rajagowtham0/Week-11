import warnings

# Ignore unnecessary warnings
warnings.filterwarnings("ignore")

# Import required libraries
import easyocr
import cv2

# Import TextBlob for spell correction
from textblob import TextBlob

# Load EasyOCR model

# Initialize EasyOCR Reader
# ['en'] -> English language support
# gpu=False -> Uses CPU for processing
reader = easyocr.Reader(
    ['en'],
    gpu=False
)

print("EasyOCR model loaded successfully")


# Text Cleaning Function
def clean_text(text):

    # Remove extra spaces from extracted text
    text = " ".join(text.split())

    # Perform spell correction
    corrected_text = str(
        TextBlob(text).correct()
    )

    # Return cleaned text
    return corrected_text.strip()


# OCR Text Extraction Function
def extract_text(image_path):

    try:

        print("Starting OCR Extraction Pipeline")

        # Display image path
        print(f"Processing Image: {image_path}")

        # Read image using OpenCV
        image = cv2.imread(image_path)

        # Validate image loading
        if image is None:

            print("Image loading failed")

            return "Unable to read image"

        print("Image loaded successfully")

        # Resize image
        # Enlarging image improves OCR accuracy
        image = cv2.resize(
            image,
            None,
            fx=3,
            fy=3,
            interpolation=cv2.INTER_CUBIC
        )


        # Perform OCR extraction

        results = reader.readtext(
            image,
            paragraph=True
        )

        print("OCR text detection completed")

        # Display raw OCR results
        print("OCR Raw Results:")
        print(results)

        # Store extracted text
        extracted_text = []

        # Loop through OCR results
        for result in results:

            # Validate OCR result structure
            if len(result) < 2:

                continue

            # Extract detected text
            text = result[1]

            print(f"Detected Text: {text}")

            # Store cleaned text
            extracted_text.append(
                text.strip()
            )

        # Combine extracted text
        final_text = " ".join(extracted_text)


        # Clean and correct extracted text
        final_text = clean_text(
            final_text
        )


        # Handle empty OCR output
        if final_text == "":

            print("No text detected in image")

            return "No text detected"

        # Display final extracted text
        print("Final Extracted Text:")
        print(final_text)

        # Return final extracted text
        return final_text

    except Exception as e:

        # Print OCR extraction error
        print("OCR Extraction Error:")
        print(str(e))

        # Return error message
        return f"OCR Extraction Error: {str(e)}"