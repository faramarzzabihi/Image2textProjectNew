
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
import pytesseract
from PIL import Image
from .forms import ImageToTextForm
from .Utils.SpellCorrecting import RunSpellCorrection
from .Utils.SimilarityCheck import SimilarityChecker
from .Utils.PadellOCR import PaddleOCRT2I
#import OcrSourceCode
def ConvertImage2Text(request):
    text = None
    img_url= '/media/01.jpg'
    font_size = 12
    language = 'fas'
    post_processing = 'no'
    model = 'Tesseract'

    if request.method == 'POST':
        form = ImageToTextForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            font_size = form.cleaned_data['font_size']
            language = form.cleaned_data['language']
            post_processing = form.cleaned_data['post_processing']
            model = form.cleaned_data['model']
            img = Image.open(image)

            uploaded_image = request.FILES['image']
            image_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.name)
            with open(image_path, 'wb+') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)
            img_url = os.path.join(settings.MEDIA_URL, uploaded_image.name)
            
            if model=="Tesseract" :
                text = pytesseract.image_to_string(img, lang=language)
            else:
                text=PaddleOCRT2I(img,font_size,language)
            #RunSpellCorrection.SaveFile('ConvertedText.txt',text)
            if post_processing=='Yes':
                first_half  = text[:len(text)//2]
                second_half = text[len(text)//2:]
                text=RunSpellCorrection.SpellCorrectiion(first_half)
                text+=RunSpellCorrection.SpellCorrectiion(second_half)

    else:
        form = ImageToTextForm()

    return render(request, 'image_converter/convert.html', {'form': form,'image_url':img_url, 'converted_image': text, 'font_size': font_size, 'language': language,'model':model, 'post_processing': post_processing})

def CompareTexts(request):

    if request.method == 'POST':
        text1 = request.POST.get('text1', '')
        text2 = request.POST.get('text2', '')
        SimilarityCheckerObj=SimilarityChecker()
        comparison_result = SimilarityCheckerObj.calculate_transformer_similarity( text1 ,text2 )
        return render(request, 'image_converter/compare_texts.html', {'text1': text1, 'text2': text2, 'comparison_result': comparison_result})
    else:
        return render(request, 'image_converter/compare_texts.html')