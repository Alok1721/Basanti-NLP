import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the necessary resources
nltk.download('punkt')

def tokenize_sentences(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    return sentences

def tokenize_words(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    return words

# Example usage
text = "This is an example sentence. Tokenization splits text into individual tokens."
sentences = tokenize_sentences(text)
words = tokenize_words(text)

print("Sentences:")
for sentence in sentences:
    print(sentence)

print("\nWords:")
for word in words:
    print(word)
