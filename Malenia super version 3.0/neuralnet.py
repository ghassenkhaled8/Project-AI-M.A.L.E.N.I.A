import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

maleniacop = "hello" , "hellos" , "hello?"

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def sac_of_words(tokenized_sentence, words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    sac = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_word:
            sac[idx] = 1
    return sac

