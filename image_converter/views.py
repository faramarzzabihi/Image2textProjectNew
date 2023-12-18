
from django.shortcuts import render
from django.http import JsonResponse
import pytesseract
from PIL import Image
from .forms import ImageToTextForm
from .Utils.SpellCorrecting import RunSpellCorrection
from .Utils.SimilarityCheck import SimilarityChecker
from .Utils.PadellOCR import PaddleOCRT2I
#import OcrSourceCode
def ConvertImage2Text(request):
    text = None
    font_size = 12
    language = 'fas'
    post_processing = 'no'

    if request.method == 'POST':
        form = ImageToTextForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            font_size = form.cleaned_data['font_size']
            language = form.cleaned_data['language']
            post_processing = form.cleaned_data['post_processing']
            model = form.cleaned_data['model']
            img = Image.open(image)
            if model=="Tesseract" :
                text = pytesseract.image_to_string(img, lang=language)
            else:
                text=PaddleOCRT2I(img,font_size)
            #RunSpellCorrection.SaveFile('ConvertedText.txt',text)
            if post_processing=='Yes':
                first_half  = text[:len(text)//2]
                second_half = text[len(text)//2:]
                text=RunSpellCorrection.SpellCorrectiion(first_half)
               # text+=RunSpellCorrection.SpellCorrectiion(second_half)

    else:
        form = ImageToTextForm()

    return render(request, 'image_converter/convert.html', {'form': form, 'converted_image': text, 'font_size': font_size, 'language': language, 'post_processing': post_processing})

def CompareTexts(request):

    if request.method == 'POST':
        text1 = request.POST.get('text1', '')
        text2 = request.POST.get('text2', '')
        SimilarityCheckerObj=SimilarityChecker()
        comparison_result = SimilarityCheckerObj.calculate_transformer_similarity( text1 ,text2 )
        return render(request, 'image_converter/compare_texts.html', {'text1': text1, 'text2': text2, 'comparison_result': comparison_result})
    else:
        return render(request, 'image_converter/compare_texts.html')