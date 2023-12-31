#pip install sentence-transformers
from sentence_transformers import SentenceTransformer, util
import os
class SimilarityChecker:
    def __init__(self):
      #  self.model = SentenceTransformer("m3hrdadfi/bert-zwnj-wnli-mean-tokens")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, "SentenceTransformerModel.pkl")
        import pickle
        with open(file_path, "rb") as file:
           # pickle.dump(self.model, file)
            self.model = pickle.load(file)

        
    def calculate_transformer_similarity(self,text1, text2):#, model_name="m3hrdadfi/bert-zwnj-wnli-mean-tokens"
        embedding1 = self.model.encode(text1, convert_to_tensor=True)
        embedding2 = self.model.encode(text2, convert_to_tensor=True)

        similarity_score = util.pytorch_cos_sim(embedding1, embedding2).item()

        return similarity_score
   
   
   
    def OpenFile(filename):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)
        with open(file_path, 'r') as file:
            return  file.read()
        
    #text1 =OpenFile("t1.txt")
    #text2 =OpenFile("t2.txt")
    #similarity_score = calculate_transformer_similarity(text1, text2)

    #print(f"Transformer Similarity Score: {similarity_score}")
