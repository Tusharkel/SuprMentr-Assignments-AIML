'''
Assignment (20/03/2026)

Assignment Name : Text Challenges
Description :Collect 20 messy sentences and identify slang, emojis, typos; explain preprocessing needed.
'''

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

sentences = [
    "omg i cant believe u did tht lmaooo 😂😂",
    "plzz send me da assignmnt asap bro 🙏",
    "yooo this moviie was soooo gud!!!! 🔥",
    "i dunno wat ur tlkng abt tbh 😅",
    "gonna grab sum foood b4 the exam lol",
    "ur such a vibe fr fr no cap 💯",
    "wth hapnd 2 ur phne bro its ded 💀",
    "ngl tht presentation was kinda mid tbh 😬",
    "lemme kno wen ur free 2nite yeah??",
    "bruh i forgt my passwrd agn smh 🤦",
]

slang = {"omg","lmaooo","lol","u","ur","da","asap","bro",
         "tbh","ngl","fr","bruh","smh","wth","nah","gonna",
         "lemme","dunno","vibe","yooo","cap","mid","sum"}

typos = {"tht","assignmnt","plzz","moviie","soooo","gud",
         "wat","tlkng","foood","hapnd","phne","forgt",
         "passwrd","agn","boringg","evn","midnite","clas"}

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def pipeline(sentence):
    text   = re.sub(r'[^\x00-\x7F]', '', sentence).lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens

print("=" * 55)
for i, s in enumerate(sentences, 1):
    tokens  = word_tokenize(s.lower())
    emojis  = re.findall(r'[^\x00-\x7F]+', s)
    s_found = [t for t in tokens if t in slang]
    t_found = [t for t in tokens if t in typos]
    result  = pipeline(s)
    print(f"\n{i}. {s}")
    print(f"   Emojis : {emojis  or 'None'}")
    print(f"   Slang  : {s_found or 'None'}")
    print(f"   Typos  : {t_found or 'None'}")
    print(f"   Output : {result}")
print("=" * 55)