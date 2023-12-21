from .SpellCorrectionClass.SpellCorrectionUsingParsBERT import *
class RunSpellCorrection:
    def __init__(self): 
         pass
    def OpenFile(self, filename):
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, filename)
            with open(file_path, 'r') as file:
                return  file.read()

    def SaveFile(filename,text):
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, filename)
            with open(file_path, 'w') as file:
                file.write(text)
            
    def SpellCorrectiion(text_row):
        SpellCorrection=SpellCorrectionUsingParsBERT_CLS()
        #text_row=OpenFile("text_paddle.txt")
        #print(a)
        return(SpellCorrection.correct_spelling_fun(text_row))

