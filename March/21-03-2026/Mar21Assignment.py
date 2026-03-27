'''
Assignment (21/03/2026)

Assignment Name : Build a Text Cleaner
Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.
'''

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

texts = [
    "Hello! This is an AMAZING day, isn't it?",
    "Python is the BEST language for Data Science!!!",
    "Stop!!! Don't do that... it's not allowed.",
    "NLP makes text processing so much easier :)",
    "I LOVE machine learning, deep learning & AI!!"
]

stop_words = set(stopwords.words('english'))

def clean(text):
    text   = text.lower()
    text   = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

print("=" * 55)
for i, text in enumerate(texts, 1):
    result = clean(text)
    print(f"\n{i}. Original : {text}")
    print(f"   Cleaned  : {result}")
print("=" * 55)