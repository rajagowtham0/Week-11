import easyocr
import cv2

print("Loading OCR model...")

reader = easyocr.Reader(
    ['en'],
    gpu=False
)

print("OCR model loaded successfully")


def extract_text(image_path):

    # Read image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Resize image for better OCR
    gray = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Apply thresholding
    _, threshold = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY
    )

    # OCR extraction
    results = reader.readtext(
        threshold,
        paragraph=True
    )

    extracted_text = []

    for result in results:

        text = result[1]

        extracted_text.append(text)

    final_text = " ".join(extracted_text)

    return final_text