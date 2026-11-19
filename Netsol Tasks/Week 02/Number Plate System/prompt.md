# Number Plate System: One-Shot Prompt

Paste everything inside the block below into the model as a single message. Architecture: `architecture_diagram.jpg` (same folder).

Token-saving choices:
- Every "YOUR CALL" decision from the diagram is already made in the prompt, so no clarifying back-and-forth.
- Spec is terse, with no prose or background.
- The model is told to return one file with no explanations, and to run no extra steps or restate the task.

---

```text
ROLE: Python engineer. Output ONE file `plate_gen.py` (stdlib only). No explanation, no markdown outside the code block, no restating this spec.

GOAL: N-gram number-plate recommender. Pipeline, in this order, one function per stage:
schema -> load_data -> preprocess -> train -> generate -> validate -> score -> rank -> main

CONFIG (top of file, editable):
SCHEMA = [("L",2),("D",2),("L",3)]   # LL-DD-LLL; L=letter, D=digit
N = 2          # n-gram order
POOL = 2000    # candidates to over-generate
TOP_K = 5
BLOCKLIST = {"WTF","XXX","SEX","KKK","ASS"}   # any block/substring match -> invalid
CORPUS = None  # optional path to a public corpus file, one entry per line
OWN = ["ALI","AHMAD"]  # user's own words

1 DATA: merge CORPUS lines + OWN, uppercase, strip non-alphanumerics, dedupe. Fall back to OWN + a built-in ~50-word list if CORPUS is None.
2 PREPROCESS: ONE MODEL PER SEGMENT (letters and digits never train together). For each block in SCHEMA, build training strings of exactly that length and type: slice entries into windows of the block length, keep only chars of that type. Digit blocks with no data: train on a built-in uniform 0-9 list. Skip entries too short.
3 NGRAM: per-segment char counts -> probabilities, pad with ^ start. Laplace smoothing (add-1) so unseen pairs get small nonzero probability, never crash. Backoff to N-1 when context unseen. N is read from CONFIG; must work for N=1,2,3.
4 GENERATE: input `seed` (user string, e.g. "ALI"). Rules:
   - seed longer than a block: truncate to the block length
   - seed shorter: use it as the prefix, sample the rest
   - seed char of the wrong type for the segment (digit in a letter block, or the reverse): drop that char and sample instead
   Sample POOL plates by weighted random choice per segment. Over-generate on purpose.
5 VALIDATE: keep a plate only if (a) every block has exact length and type, AND (b) no BLOCKLIST word appears in the plate string. Correct length alone is not enough.
6 SCORE: log-probability under the trained models, averaged per character (length-normalised). Higher is better. Also compute perplexity = exp(-avg_logprob). They are inverse; rank by avg_logprob only, and print both.
7 RANK: dedupe identical plates (keep the one occurrence, same score anyway), sort by score descending, cut to TOP_K.

OUTPUT: one line per plate, best first: `AB-12-XYZ  score=-1.234  ppl=3.43`. Then stop.

MAIN: argparse `--seed`, `--n`, `--top`. Run example in `if __name__=="__main__"`. Add seeded `random.seed(42)` for reproducible output. Code must run as-is with `python plate_gen.py --seed ALI`.
```

---

## Decisions already made (answers to the diagram's "YOUR CALL" boxes)

| Stage | Question in diagram | Decision |
|---|---|---|
| Foundation | Which plate format? | `LL-DD-LLL`, in a `SCHEMA` list so it can be changed |
| 2 Preprocessing | One shared model or one per segment? | One per segment, because letters and digits mixed together give meaningless probabilities |
| 3 N-gram | What do N=1,2,3 change, and what about unseen pairs? | N is a setting. Add-1 smoothing plus backoff, so unseen pairs never break it |
| 4 Generation | Seed too long, too short, or wrong type? | Truncate, use as prefix and sample the rest, drop the wrong-type character |
| 5 Validation | Is the right length enough? | No. It must also have the right type per block and no blocklist word |
| 6 Scoring | Perplexity or probability? | Average log-probability, higher is better. Perplexity is shown as well, because it is just the inverse |
| 7 Ranking | Duplicate plates? | Keep one copy, since identical plates have identical scores |