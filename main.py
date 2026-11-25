"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the monologue to $ENTRY_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, no network. Deterministic: same bytes on every run.
"""

import os

TEXT = """Come in. Mind the third step. It still bites. I had it enchanted in '87, back when traps sang.

You want the crown? Take it. No — sit. The tea's cold, the ravens stopped answering my letters, which is… fine.

Tonight the river gates open at moonrise. My barges — black sails, the ones your grandfather burned — carry the salt tax upriver. By dawn every mill in Valdris owes me. Not blood. Rent.

Don't look so shocked. I kept the receipts. Forty years, in the cellar, next to the —

…where was I? Right. Kneel, or don't. The floor's cold either way.
"""

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
