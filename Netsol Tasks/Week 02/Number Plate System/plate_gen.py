"""N-gram number-plate recommender.

Pipeline: schema -> load_data -> preprocess -> train -> generate -> validate -> score -> rank
Run: python plate_gen.py --seed ALI
"""
import argparse
import math
import random
import re
from collections import Counter, defaultdict

# ---------------- CONFIG ----------------
SCHEMA = [("L", 2), ("D", 2), ("L", 3)]  # LL-DD-LLL; L=letter, D=digit
N = 2            # n-gram order
POOL = 2000      # candidates to over-generate
TOP_K = 5
BLOCKLIST = {"WTF", "XXX", "SEX", "KKK", "ASS"}
CORPUS = None    # optional path to a public corpus file, one entry per line
OWN = ["ALI", "AHMAD"]
BUILTIN = ("LAHORE KARACHI ISLAMABAD PESHAWAR QUETTA MULTAN FAISALABAD SIALKOT "
           "RAWALPINDI HYDERABAD SUKKUR BAHAWALPUR GUJRAT SAHIWAL KASUR OKARA "
           "JHELUM CHAKWAL ATTOCK MARDAN SWAT KOHAT BANNU GWADAR ZHOB TURBAT "
           "HASSAN HUSSAIN BILAL USMAN OMAR UMAR FAHAD KAMRAN ZAIN HAMZA TALHA "
           "SAAD ASAD DANISH FARHAN IMRAN NADEEM RAZA SHAHID WASIM JAVED NAVEED").split()
START = "^"
ALPHABET = {"L": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "D": "0123456789"}
PATTERN = re.compile(r"[^A-Z0-9]")
KIND = {"L": str.isalpha, "D": str.isdigit}


# ---------------- 1 DATA ----------------
def load_data():
    entries = []
    if CORPUS:
        with open(CORPUS, encoding="utf-8") as f:
            entries += f.read().splitlines()
    entries += OWN
    if not CORPUS:
        entries += BUILTIN
    seen, out = set(), []
    for e in entries:
        e = PATTERN.sub("", e.upper())
        if e and e not in seen:
            seen.add(e)
            out.append(e)
    return out


# ---------------- 2 PREPROCESS ----------------
def preprocess(entries):
    """One training set per segment: windows of block length, only chars of that type."""
    sets = []
    for kind, length in SCHEMA:
        strings = []
        for e in entries:
            chars = "".join(c for c in e if KIND[kind](c))
            if len(chars) < length:
                continue
            strings += [chars[i:i + length] for i in range(len(chars) - length + 1)]
        if not strings:  # e.g. no digits in the data -> uniform fallback
            strings = ["".join(random.choice(ALPHABET[kind]) for _ in range(length))
                       for _ in range(200)]
        sets.append(strings)
    return sets


# ---------------- 3 N-GRAM MODEL ----------------
class NGram:
    def __init__(self, strings, kind, n):
        self.n, self.kind = n, kind
        self.vocab = ALPHABET[kind]
        self.counts = defaultdict(Counter)  # context -> next-char counts
        for s in strings:
            padded = START * (n - 1) + s
            for i in range(n - 1, len(padded)):
                for k in range(n):  # also store lower orders for backoff
                    ctx = padded[i - k:i]
                    self.counts[ctx][padded[i]] += 1

    def probs(self, context):
        """Add-1 smoothed distribution; back off to shorter context if unseen."""
        context = (START * (self.n - 1) + context)[-(self.n - 1):] if self.n > 1 else ""
        while context and context not in self.counts:
            context = context[1:]
        c = self.counts.get(context, Counter())
        total = sum(c.values()) + len(self.vocab)
        return {ch: (c[ch] + 1) / total for ch in self.vocab}


def train(sets, n):
    return [NGram(strings, kind, n) for strings, (kind, _) in zip(sets, SCHEMA)]


# ---------------- 4 GENERATION ----------------
def sample_block(model, length, prefix):
    out = prefix
    while len(out) < length:
        p = model.probs(out)
        out += random.choices(list(p), weights=list(p.values()))[0]
    return out


def clean_seed(seed):
    return PATTERN.sub("", seed.upper())


def generate(models, seed, pool=POOL):
    seed = clean_seed(seed)
    plates = []
    for _ in range(pool):
        remaining, blocks = seed, []
        for model, (kind, length) in zip(models, SCHEMA):
            prefix = ""
            # take seed chars for this block; drop wrong-type chars, truncate to length
            while remaining and len(prefix) < length:
                ch, remaining = remaining[0], remaining[1:]
                if KIND[kind](ch):
                    prefix += ch
                # wrong type for this segment -> dropped, sampling fills in
            blocks.append(sample_block(model, length, prefix))
        plates.append(blocks)
    return plates


# ---------------- 5 VALIDATE ----------------
def validate(plates):
    ok = []
    for blocks in plates:
        shape = all(len(b) == l and all(KIND[k](c) for c in b)
                    for b, (k, l) in zip(blocks, SCHEMA))
        flat = "".join(blocks)
        bad = any(w in flat or any(w in b for b in blocks) for w in BLOCKLIST)
        if shape and not bad:
            ok.append(blocks)
    return ok


# ---------------- 6 SCORE ----------------
def score(models, blocks):
    """Length-normalised avg log-probability (higher = better). ppl = exp(-avg)."""
    total, count = 0.0, 0
    for model, block in zip(models, blocks):
        for i, ch in enumerate(block):
            total += math.log(model.probs(block[:i])[ch])
            count += 1
    avg = total / count
    return avg, math.exp(-avg)


# ---------------- 7 RANK ----------------
def rank(models, plates, top_k):
    best = {}
    for blocks in plates:
        key = "-".join(blocks)
        if key not in best:  # identical plate -> identical score, keep one
            best[key] = score(models, blocks)
    ordered = sorted(best.items(), key=lambda kv: kv[1][0], reverse=True)
    return ordered[:top_k]


# ---------------- MAIN ----------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="")
    ap.add_argument("--n", type=int, default=N)
    ap.add_argument("--top", type=int, default=TOP_K)
    a = ap.parse_args()
    random.seed(42)
    models = train(preprocess(load_data()), a.n)
    valid = validate(generate(models, a.seed))
    for plate, (avg, ppl) in rank(models, valid, a.top):
        print(f"{plate}  score={avg:.3f}  ppl={ppl:.2f}")


if __name__ == "__main__":
    main()