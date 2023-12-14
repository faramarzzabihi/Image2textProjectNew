from collections import Counter
import hazm

class NorvigSpellChecker:
    def __init__(self, words):
        self.WORDS = Counter(words)
        self.N = sum(self.WORDS.values())
        self.letters = 'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'

    def P(self, word):
        "Probability of word."
        return self.WORDS[word] / self.N

    def correction(self, word):
        "Most probable spelling correction for word."
        return max(self.word_pool(word), key=self.P)

    def word_pool(self, word):
        "Generate a pool of possible words."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def candidates(self, word):
        "Generate possible spelling corrections for word."
        if self.WORDS[word] < 30 or len(word) == 1 and word not in hazm.stopwords_list():
            candidates_list = list(self.known(self.edits1(word)))
            candidates_list.sort(key=self.P, reverse=True)
            return candidates_list
        else:
            return word

    def known(self, words):
        "The subset of words that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word):
        "All edits that are one edit away from word."
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in self.letters]
        inserts = [L + c + R for L, R in splits for c in self.letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        "All edits that are two edits away from word."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))
    