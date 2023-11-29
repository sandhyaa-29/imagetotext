pip install pytesseract
import pytesseract
from PIL import Image
# Open an image file
img = Image.open('image.jpg')
# Use pytesseract to extract text from an image
extracted_information = pytesseract.image_to_string(Image.open('OCR_sample.png'))
# Print the extracted text
print(extracted_information)

