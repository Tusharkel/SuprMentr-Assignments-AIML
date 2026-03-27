"""
Assignment (10/03/2026)

Assignment Name : Spam Classifier Thinking
Description : Design a spam detection system: features, data needed, possible mistakes.
"""

import csv, math
with open("emails.csv", newline="") as f:
    emails = list(csv.DictReader(f))
    for e in emails:
        e["links"] = int(e["links"])
SPAM_WORDS = ["free","win","won","prize","claim","cheap","offer","gift","selected","reward","limited","buy","click"]
SUSPICIOUS = [".xyz",".biz",".net","promo","deals","gifts","winner"]
def extract_features(e):
    text = (e["subject"] + " " + e["body"]).lower()
    return [
        sum(1 for w in SPAM_WORDS if w in text),
        1 if "!" in text else 0,
        sum(1 for w in text.split() if w.isupper() and len(w) > 2),
        e["links"],
        1 if any(d in e["sender"] for d in SUSPICIOUS) else 0,
    ]
def euclidean(v1, v2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(v1,v2)))
def knn_predict(train_f, train_l, point, k=3):
    top_k = [l for _,l in sorted([(euclidean(point, train_f[i]), train_l[i]) for i in range(len(train_f))], key=lambda x: x[0])[:k]]
    return "spam" if top_k.count("spam") > top_k.count("ham") else "ham"
features = [extract_features(e) for e in emails]
labels   = [e["label"] for e in emails]
correct, fp, fn = 0, [], []
for i, email in enumerate(emails):
    pred   = knn_predict(features[:i]+features[i+1:], labels[:i]+labels[i+1:], features[i])
    actual = email["label"]
    correct += pred == actual
    if pred == "spam" and actual == "ham": fp.append(email["subject"])
    if pred == "ham"  and actual == "spam": fn.append(email["subject"])
    print(f"{email['subject'][:30]:<30} | {pred.upper()} vs {actual.upper()} {'✅' if pred==actual else '❌'}")
print(f"\nAccuracy: {correct}/{len(emails)} | FP: {len(fp)} | FN: {len(fn)}")

print("""
DESIGN REFLECTION

FEATURES USED BY KNN:
  · Spam keyword count in subject + body
  · Exclamation mark presence
  · All-caps word count
  · Number of links
  · Suspicious sender domain

HOW KNN WORKS HERE:
  · Each email is a point in 5D feature space
  · KNN finds the 3 closest emails (k=3)
  · Majority label among neighbours = prediction
  · Uses leave-one-out: each email tested against the rest

DATA NEEDED FOR A REAL MODEL:
  · Thousands of labeled emails (spam / ham)
  · Diverse senders, languages, and topics
  · Temporal data (spam patterns change over time)

POSSIBLE MISTAKES:
  · False Positive  — ham flagged as spam
      e.g. "FREE donuts in the kitchen today!"
  · False Negative  — spam slips through
      e.g. Carefully worded phishing with no trigger words

LIMITATIONS:
  · Small dataset — only 8 emails
  · KNN is slow at scale (compares every email to all others)
  · Feature engineering still done manually
""")