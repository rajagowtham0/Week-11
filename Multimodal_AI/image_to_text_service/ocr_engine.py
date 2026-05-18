from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

print("Loading TrOCR model...")

# Load processor and model
processor = TrOCRProcessor.from_pretrained(
    "microsoft/trocr-base-printed"
)

model = VisionEncoderDecoderModel.from_pretrained(
    "microsoft/trocr-base-printed"
)

print("TrOCR model loaded successfully")


def extract_text(image_path):

    try:

        # Open image
        image = Image.open(image_path).convert("RGB")

        # Preprocess image
        pixel_values = processor(
            images=image,
            return_tensors="pt"
        ).pixel_values

        # Generate text
        generated_ids = model.generate(
            pixel_values
        )

        # Decode generated text
        extracted_text = processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        # Clean text
        extracted_text = " ".join(
            extracted_text.split()
        )

        extracted_text = extracted_text.strip()

        # Handle empty output
        if extracted_text == "":

            return "No text detected"

        return extracted_text

    except Exception as e:

        return f"OCR Extraction Error: {str(e)}"