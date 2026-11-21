# Task 62 - text analysis
import re
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "Machine learning lets computers learn patterns from data.",
    "Deep learning is a part of machine learning that uses neural networks.",
    "Neural networks learn from lots of data and many examples.",
    "The cricket team won the match by five wickets yesterday.",
    "The batsman scored a century and the team won the cricket series.",
    "Fresh vegetables and fruit are good for your health.",
]

STOP = {"the", "a", "of", "and", "is", "that", "for", "from", "by", "your", "are", "many", "lets"}


def tokens(text):
    words = re.findall(r"[a-z']+", text.lower())
    return [w for w in words if w not in STOP]


all_words = [w for d in docs for w in tokens(d)]
print("total words:", len(all_words))
print("unique words:", len(set(all_words)))
print("top words:", Counter(all_words).most_common(6))

avg_len = np.mean([len(d.split()) for d in docs])
print("average document length:", round(avg_len, 1), "words")

cv = CountVectorizer(stop_words="english")
bow = cv.fit_transform(docs)
print("\nbag of words matrix:", bow.shape)

tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(docs)
names = tfidf.get_feature_names_out()

print("\ntop words per document")
for i, row in enumerate(X.toarray()):
    top = row.argsort()[-3:][::-1]
    print(i, [names[j] for j in top])

sim = cosine_similarity(X)
print("\nsimilarity matrix")
print(np.round(sim, 2))

query = "how do neural networks learn"
q = tfidf.transform([query])
scores = cosine_similarity(q, X)[0]
best = scores.argmax()
print("\nquery:", query)
print("closest doc:", docs[best], "(score", round(scores[best], 2), ")")

good = {"good", "great", "fresh", "won", "best"}
bad = {"bad", "lost", "poor", "worst"}
for d in docs:
    t = tokens(d)
    score = sum(w in good for w in t) - sum(w in bad for w in t)
    print(score, "|", d)