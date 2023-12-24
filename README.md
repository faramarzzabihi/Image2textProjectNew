# Simple OCR, Spell Correction, and Similarity Checker for Farsi Text
This Django-based project offers a comprehensive solution for handling natural language processing (NLP) tasks specifically tailored for Farsi, English, and Arabic texts. By integrating various tools and libraries, users can convert images to text, assess text similarity, and perform spell correction effortlessly.

## Features:
1. OCR (Optical Character Recognition):

    - Convert images containing Farsi, English, or Arabic text into machine-encoded text.
    - Utilizes PadellOcr for Farsi and Arabic text extraction and Tesseract for English text recognition.
1. Similarity Checker:

    - Determine the textual similarity score between two given texts using the SentenceTransformer model.
    - Offers insights into how closely two texts align in content and context.
1. Spell Correction:

    - Enhance OCR accuracy by post-processing the extracted text to rectify spelling errors.
    - Implements the SpellCorrectionUsingParsBERT project for intelligent spell-checking of Farsi text.
  
## Notice:
Please note that this project utilizes some .pkl files to optimize performance. To maintain transparency and facilitate customization:

- The .pkl files are pre-computed models for specific functionalities.
- Instead of relying on pre-existing .pkl files, consider using the corresponding classes or functionalities in the codebase to generate the desired outputs programmatically.

## Installation and Setup:
### Tesseract Installation:
For Linux:\
```sudo apt-get install tesseract-ocr```

### Getting Started:
Setting Up the Django Project:
Clone the repository to your local machine:
```
git clone [repository_url]
cd [repository_folder]
```
Install the required Python packages:
```
pip install -r requirements.txt
```
Run the Django development server:
```
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/ in your web browser to access the project interface.
## Usage:
1. OCR Feature:

    - Upload an image containing Farsi, English, or Arabic text.
    - Select the appropriate language (Farsi, English, or Arabic).
    - Click the 'Convert' button to extract text from the image.
1. Similarity Checker:

    - Enter two texts in Farsi, English, or Arabic into the provided input fields.
    - Click the 'Check Similarity' button to obtain a similarity score between the two texts.
1. Spell Correction:

    - If your selactde language is Farsi and you are selected 'Spell Correction', after using the OCR feature, the 'Correct Spelling' function will apply intelligent spell correction using the ParsBERT model.
## Contribution:
If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request. Your contributions are highly appreciated!


By integrating cutting-edge NLP techniques and tools, this project aims to provide a seamless experience for users looking to perform OCR, text similarity checking, and spell correction tasks specifically for Farsi, English, and Arabic languages.
