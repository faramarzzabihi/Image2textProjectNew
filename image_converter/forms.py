
from django import forms

class ImageToTextForm(forms.Form):
    image = forms.ImageField(label='Select an image', required=True)
    font_size = forms.IntegerField(label='Font Size', initial=12, min_value=1)
    language = forms.ChoiceField(label='Language', choices=[('eng', 'English'), ('fas', 'Farsi'), ('fas', 'Arabic')], initial='eng')
    model=forms.ChoiceField(label='Model', choices=[('Tesseract', 'Tesseract'), ('PadellOCR', 'PadellOCR')], initial='Tesseract')
    #forms.CharField(label='Language', initial='eng', max_length=3, help_text='ISO 639-3 language code')
    post_processing = forms.ChoiceField(label='Do SpellCorrection(It take a while to  be processed)', choices=[('No', 'No'), ('Yes', 'Yes(It take a while to  be processed)')], initial='No')
