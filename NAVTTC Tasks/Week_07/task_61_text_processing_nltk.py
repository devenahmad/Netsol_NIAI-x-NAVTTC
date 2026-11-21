# Task 61 - text processing with nltk
import re
import nltk

for pkg in ["punkt", "punkt_tab", "stopwords", "wordnet", "averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng", "omw-1.4"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, FreqDist

text = ("Natural language processing helps computers understand people. "
        "Companies are using it for chatbots, translation and search! "
        "It's running faster and getting better every year.")

sentences = sent_tokenize(text)
print("sentences:", len(sentences))
for s in sentences:
    print("  -", s)

words = word_tokenize(text)
print("\nwords:", words)

stop = set(stopwords.words("english"))
clean = [w.lower() for w in words if w.isalpha() and w.lower() not in stop]
print("\nafter cleaning:", clean)

stemmer = PorterStemmer()
lemma = WordNetLemmatizer()
print("\nword           stem          lemma")
for w in ["running", "better", "companies", "faster", "understand", "processing"]:
    print(f"{w:14s} {stemmer.stem(w):13s} {lemma.lemmatize(w, pos='v')}")

print("\npart of speech tags")
print(pos_tag(word_tokenize("The quick brown fox jumps over the lazy dog")))

freq = FreqDist(clean)
print("\nmost common:", freq.most_common(5))

messy = "Contact: ali@example.com, call 0300-1234567 or visit https://example.com!!!"
print("\nemails:", re.findall(r"[\w.]+@[\w.]+", messy))
print("phones:", re.findall(r"\d{4}-\d{7}", messy))
print("links :", re.findall(r"https?://\S+", messy.rstrip("!")))
print("no punctuation:", re.sub(r"[^\w\s]", "", messy))