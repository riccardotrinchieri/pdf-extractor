import nltk
from nltk.tokenize import sent_tokenize
import re


nltk.download('punkt')

def break_into_sentences(text):
  return  sent_tokenize(text)


def remove_noisy_words(text):
    alphanumeric_pattern = re.compile(r'\b[a-zA-Z0-9]+\b')
    alphanumeric_strings = alphanumeric_pattern.findall(text)
    
    return ' '.join(alphanumeric_strings)
    

def preprocess(text):
   sentences = break_into_sentences(text)
   cleaned_sentences = [remove_noisy_words(sentence).strip() for sentence in sentences]
   non_empty_sentences = filter(lambda sentence: sentence, cleaned_sentences)
   return '.\n'.join(non_empty_sentences)

