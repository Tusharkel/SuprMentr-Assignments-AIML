'''
Assignment (27/03/2026)

Assignment Name : Semantic Meaning
Description : Find 5 word pairs and explain semantic similarity.
'''

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pairs=[
("car","automobile"),
("happy","joyful"),
("big","large"),
("fast","quick"),
("smart","intelligent")
]

words=[w for pair in pairs for w in pair]

vectorizer=TfidfVectorizer()
x=vectorizer.fit_transform(words)

matrix=x.toarray()

print("Semantic Similarity Scores:\n")

for i in range(0,len(words),2):
    v1=matrix[i].reshape(1,-1)
    v2=matrix[i+1].reshape(1,-1)
    score=cosine_similarity(v1,v2)[0][0]
    print(words[i],"-",words[i+1],":",round(score,3))