'''
Train a Mini Word2Vec Model
Task:

Create your own small dataset of at least 15 sentences on any topic like:

sports
food
movies
college life

Train a Word2Vec model and print:

vector of one word
5 most similar words for any chosen word
Expected outcome: understand how embeddings are learned from context.
'''

from gensim.models import Word2Vec

sentences = [
    ["students", "attend", "lectures", "every", "morning"],
    ["the", "library", "is", "open", "late", "at", "night"],
    ["students", "submit", "assignments", "before", "deadlines"],
    ["professors", "explain", "concepts", "during", "lectures"],
    ["college", "life", "involves", "exams", "and", "projects"],
    ["the", "canteen", "serves", "food", "during", "breaks"],
    ["students", "form", "study", "groups", "before", "exams"],
    ["the", "hostel", "is", "home", "for", "many", "students"],
    ["internships", "help", "students", "gain", "experience"],
    ["the", "campus", "has", "a", "big", "sports", "ground"],
    ["friends", "hang", "out", "in", "the", "canteen"],
    ["projects", "require", "teamwork", "and", "deadlines"],
    ["professors", "give", "assignments", "after", "every", "lecture"],
    ["college", "festivals", "are", "enjoyed", "by", "students"],
    ["exams", "cause", "stress", "but", "also", "motivation"]
]

model = Word2Vec(
    sentences,
    vector_size=50,  
    window=2,        
    min_count=1,      
    sg=1             
)

print("Vector for 'students':")
print(model.wv['students'])

print("\n5 words most similar to 'exams':")
similar = model.wv.most_similar('exams', topn=5)
for word, score in similar:
    print(f"  {word:15s}  similarity: {score:.4f}")
