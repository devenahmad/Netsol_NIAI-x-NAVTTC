# Task 60 - language + machine learning
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = [
    ("i loved this movie, it was great", 1),
    ("what a wonderful and fun film", 1),
    ("amazing acting and a brilliant story", 1),
    ("really enjoyed it, highly recommend", 1),
    ("best thing i have watched this year", 1),
    ("a beautiful and touching story", 1),
    ("fantastic, i would watch it again", 1),
    ("great music and lovely characters", 1),
    ("so good, i laughed the whole time", 1),
    ("excellent direction and superb cast", 1),
    ("this movie was terrible", 0),
    ("what a boring and awful film", 0),
    ("horrible acting and a stupid story", 0),
    ("really hated it, do not recommend", 0),
    ("worst thing i have watched this year", 0),
    ("a messy and painful story", 0),
    ("awful, i would never watch it again", 0),
    ("bad music and annoying characters", 0),
    ("so bad, i fell asleep", 0),
    ("poor direction and weak cast", 0),
]
texts = [r[0] for r in reviews]
labels = [r[1] for r in reviews]

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.3, random_state=3, stratify=labels
)

cv = CountVectorizer()
Xtr = cv.fit_transform(X_train)
Xte = cv.transform(X_test)
print("vocabulary size:", len(cv.vocabulary_))

nb = MultinomialNB().fit(Xtr, y_train)
print("naive bayes accuracy:", round(accuracy_score(y_test, nb.predict(Xte)), 2))

tf = TfidfVectorizer()
Xtr2 = tf.fit_transform(X_train)
Xte2 = tf.transform(X_test)
lr = LogisticRegression().fit(Xtr2, y_train)
print("tf-idf + logistic accuracy:", round(accuracy_score(y_test, lr.predict(Xte2)), 2))

new = [
    "great story and wonderful acting",
    "boring and terrible, i hated it",
    "the film was ok",
]
for s, p in zip(new, lr.predict(tf.transform(new))):
    print(f"'{s}' -> {'positive' if p == 1 else 'negative'}")

words = tf.get_feature_names_out()
order = lr.coef_[0].argsort()
print("\nmost negative words:", [words[i] for i in order[:6]])
print("most positive words:", [words[i] for i in order[-6:]])