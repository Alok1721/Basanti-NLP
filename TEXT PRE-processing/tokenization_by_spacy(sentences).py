#tokenization by spacy(spiliting the sentences)
import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp("dr strange is bose of universe. hulk is my favourite.")
for sentence in doc.sents:
    print(sentence)
    
