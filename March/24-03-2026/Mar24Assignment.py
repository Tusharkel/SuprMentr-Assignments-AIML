'''
Assignment (24/03/2026)

Assignment Name :Word Importance Explorer
Description : Use TF-IDF on 5 documents and identify top keywords with explanation.
'''

from sklearn.feature_extraction.text import TfidfVectorizer

documents=[
"machine learning improves prediction accuracy using data",
"deep learning uses neural networks for complex tasks",
"artificial intelligence includes machine learning techniques",
"data science applies machine learning for insights",
"neural networks power many deep learning models"
]

vectorizer=TfidfVectorizer()
x=vectorizer.fit_transform(documents)

words=vectorizer.get_feature_names_out()
matrix=x.toarray()

print("Vocabulary:")
print(words)

print("\nTF-IDF Matrix:")
print(matrix)

print("\nTop Keywords per Document:")

for i in range(len(matrix)):
    scores=matrix[i]
    pairs=list(zip(words,scores))
    sorted_pairs=sorted(pairs,key=lambda x:x[1],reverse=True)
    top_words=[w for w,s in sorted_pairs[:5]]
    print("Doc",i+1,":",top_words)