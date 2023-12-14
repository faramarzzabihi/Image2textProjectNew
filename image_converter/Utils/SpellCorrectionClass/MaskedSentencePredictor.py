

import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM
class MaskedSentencePredictor:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('HooshvareLab/bert-fa-base-uncased')
        self.model = BertForMaskedLM.from_pretrained('HooshvareLab/bert-fa-base-uncased')
        self.model.eval()
        # self.model.to('cuda')

    def predict_masked_sent(self, text, top_k=5):
        """
        Predicts the top-k most likely tokens to fill in a masked token in the input text using the pre-trained
        BERT-based model.

        Args:
            text (str): A string representing the input text with a [MASK] token to be filled in.
            top_k (int): An integer representing the number of top predictions to return.

        Returns:
            A list of the top-k most likely tokens to fill in the [MASK] token in the input text.
        """
        # Tokenize the input text
        text = "[CLS] %s [SEP]" % text
        tokenized_text = self.tokenizer.tokenize(text)
        masked_index = tokenized_text.index("[MASK]")
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
        tokens_tensor = torch.tensor([indexed_tokens])
        # tokens_tensor = tokens_tensor.to('cuda')

        # Make predictions
        with torch.no_grad():
            outputs = self.model(tokens_tensor)
            predictions = outputs[0]

        # Get the top-k most likely tokens and their associated weights
        probs = torch.nn.functional.softmax(predictions[0, masked_index], dim=-1)
        top_k_weights, top_k_indices = torch.topk(probs, top_k, sorted=True)

        # Convert the predicted token indices to actual tokens and return them
        mighty_tokens = []
        for i, pred_idx in enumerate(top_k_indices):
            predicted_token = self.tokenizer.convert_ids_to_tokens([pred_idx])[0]
            token_weight = top_k_weights[i]
            mighty_tokens.append(predicted_token)
        return mighty_tokens
    