
from django import forms

class ImageToTextForm(forms.Form):
    image = forms.ImageField(label='Select an image', required=True)
    font_size = forms.IntegerField(label='Font Size', initial=12, min_value=1)
    language = forms.ChoiceField(label='Language', choices=[('eng', 'English'), ('fas', 'Farsi'), ('ara', 'Arabic')], initial='eng')
    model=forms.ChoiceField(label='Model', choices=[('Tesseract', 'Tesseract'), ('PadellOCR', 'PadellOCR')], initial='Tesseract')
    post_processing = forms.ChoiceField(label='Do SpellCorrection(It take a while to  be processed)', choices=[('No', 'No'), ('Yes', 'Yes(It take a while to  be processed)')], initial='No')
