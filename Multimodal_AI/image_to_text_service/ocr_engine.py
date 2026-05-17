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

    
        # Convert to Grayscale
        

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        
        # Resize Image
        # Improves OCR accuracy

        gray = cv2.resize(
            gray,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC
        )

        # Noise Reduction

        gray = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        # Adaptive Thresholding
        # Better than fixed threshold

        threshold = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )


        # Image Sharpening

        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        sharpened = cv2.filter2D(
            threshold,
            -1,
            kernel
        )

        # OCR Text Extraction

        results = reader.readtext(
            sharpened,
            paragraph=True
        )

        # Extract Clean Text

        extracted_text = []

        for result in results:

            text = result[1]

            confidence = result[2]

            # Ignore weak confidence predictions
            if confidence > 0.30:

                extracted_text.append(text)


        # Final Clean Output

        final_text = " ".join(extracted_text)

        final_text = final_text.strip()

        return final_text

    except Exception as e:

        return f"OCR Extraction Error: {str(e)}"