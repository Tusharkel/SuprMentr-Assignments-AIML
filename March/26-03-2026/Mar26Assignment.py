'''
Assignment (26/03/2026)

Assignment Name : Movie Review Analyzer
Description : Build a simple sentiment analyzer and test on 5 reviews.
'''

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

train_reviews=[
"this movie is amazing and very good",
"i love this film it is fantastic",
"what a great and wonderful movie",
"this movie is bad and boring",
"i hate this film it is terrible",
"worst movie ever very disappointing"
]

train_labels=[1,1,1,0,0,0]

vectorizer=CountVectorizer()
x_train=vectorizer.fit_transform(train_reviews)

model=MultinomialNB()
model.fit(x_train,train_labels)

test_reviews=[
"this movie is fantastic",
"i hate this movie",
"it was a wonderful film",
"boring and bad experience",
"very good and amazing movie"
]

x_test=vectorizer.transform(test_reviews)
predictions=model.predict(x_test)

for i in range(len(test_reviews)):
    if predictions[i]==1:
        sentiment="Positive"
    else:
        sentiment="Negative"
    print("Review:",test_reviews[i])
    print("Sentiment:",sentiment)
    print()