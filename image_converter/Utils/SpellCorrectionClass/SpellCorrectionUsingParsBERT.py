import re
from .NorvigSpellChecker import *
from .MaskedSentencePredictor import *
import os
class SpellCorrectionUsingParsBERT_CLS:
    def open_text_file(self):
        # Get the current directory of the Django project
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Specify the filename you want to open (change 'example.txt' to your actual filename)
        file_name = 'example.txt'

        # Construct the full path to the text file
        file_path = os.path.join(current_directory, file_name)

        try:
            # Open the text file in read mode
            with open(file_path, 'r') as file:
                # Read the contents of the file
                file_content = file.read()

            # Do something with the file content, for example, return it as an HTTP response
        # return HttpResponse(file_content, content_type='text/plain')
            return file_content

        except FileNotFoundError:
            return file_content
    def clean_text(self, text,normalizer,tokenizer, output='word'):
        normalized_text = normalizer.normalize(text)
        punc_removed = re.sub(r'[^\w\s]', '', normalized_text)
        cleaned_text = tokenizer.tokenize(punc_removed)
        if output == 'word':
            return cleaned_text
        else:
            return ' '.join(cleaned_text)
    def load_data(self, file_path):
        return open(file_path, "r").read()#open_text_file()#
    def OpenFile(self, filename):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)
        with open(file_path, 'r') as file:
            # Read the contents of the file
            return  file.read()
    def find_homophone_pair(self,word, homophones):
        for pair in homophones:
            if word in pair:
                new_pair = [*pair]
                new_pair.remove(word)
                return new_pair[0]
        return None
    def correct_spelling(self, sentence,normalizer,tokenizer,spl,bert_predictor,homophones_list,homophones):
        # Split the sentence into words and clean it
        words = self.clean_text(sentence,normalizer,tokenizer)

        # Check each word for spelling errors
        for i, word in enumerate(words):
            # If the word is spelled correctly, keep it
            if word == spl.candidates(word):
                continue
            # Otherwise, replace it with a mask and predict the correct spelling
            else:
                words[i] = "[MASK]"
                masked_sentence = ' '.join(words)
                preds = bert_predictor.predict_masked_sent(masked_sentence, top_k=500)
                norvig_cands = spl.candidates(word)
                first_match = next((element for element in preds if element in norvig_cands), None)

                # If a correct spelling is found, replace the mask with the correct spelling
                if first_match:
                    words[i] = first_match
                else:
                    words[i] = spl.correction(word)

        # Check if the sentence contains homophones
        homophones_set = set(homophones_list)
        sentence_set = set(words)
        has_homophone = list(sentence_set.intersection(homophones_set))

        # If the sentence contains homophones, replace one with a mask and predict the correct spelling
        if has_homophone:
            homophone_index = words.index(has_homophone[0])
            words[homophone_index] = "[MASK]"
            masked_sentence = ' '.join(words)
            preds = bert_predictor.predict_masked_sent(masked_sentence, top_k=500)

            homophone_pair = self.find_homophone_pair(has_homophone[0],homophones)

            # If a correct spelling is found, replace the mask with the correct spelling
            if homophone_pair in preds:
                pred_index = preds.index(homophone_pair)
                words[homophone_index] = preds[pred_index]
            else:
                words[homophone_index] = has_homophone[0]

        # Join the corrected words back into a sentence
        corrected_sentence = ' '.join(words)

        return corrected_sentence
    def __init__(self):
        self.homophones = [
            ["خار", "خوار"],
            ["سد", "صد"],
            ["خیش", "خویش"],
            ["خاست", "خواست"],
            ["ثواب", "صواب"],
            ["قاضی", "غازی"],
            ["علم", "الم"],
            ["غریب", "قریب"],
            ["غالب", "قالب"],
            ["پرتغال", "پرتقال"],
            ["غدیر", "قدیر"],
            ["حول", "هول"],
            ["اساس", "اثاث"],
            ["اسم", "اثم"],
            ["عمل", "امل"],
            ["امارت", "عمارت"],
            ["حیات", "حیاط"],
            ["سیف", "صیف"],
            ["خان", "خوان"],
            ["سفر", "صفر"],
            ["عرض", "ارز"],
            ["ارض", "ارز"],
            ["ارض", "عرض"],
            ["راضی", "رازی"],
            ["آقا", "آغا"],
            ["غذا", "قضا"],
            ["خرد", "خورد"],
            ["هضم", "حزم"],
            ["تهدید", "تحدید"],
            ["حوزه", "حوضه"],
            ["قدر", "غدر"],
            ["صر", "سر"]
        ]
        self.homophones_list = [word for pair in self.homophones for word in pair]

        self.normalizer = hazm.Normalizer()
        self.tokenizer = hazm.WordTokenizer()

        DATA_FILE_PATH = "Persian-WikiText-1.txt"
        wikipedia = self.OpenFile(DATA_FILE_PATH)
        wikipedia_words = self.clean_text(wikipedia,self.normalizer,self.tokenizer)

        self.spl = NorvigSpellChecker(wikipedia_words)
        #import pickle
        #with open("spl_object.pkl", "wb") as file:
            #pickle.dump(spl, file)

        self.bert_predictor = MaskedSentencePredictor()

        predictions = self.bert_predictor.predict_masked_sent("من در این معامله خیلی [MASK] کردم", top_k=5)
        print(predictions)
        print(self.find_homophone_pair('خوار', self.homophones))

    def correct_spelling_fun(self,text_row):
        correct_text=self.correct_spelling(text_row,self.normalizer,self.tokenizer,self.spl,self.bert_predictor,self.homophones_list,self.homophones)
        return(correct_text)





