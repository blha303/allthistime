#!/usr/bin/env python3
import argparse

seqs = {
    "intro": ["intro", "g1", "g2", "g3", "g4"],
}

class Text:
    def __init__(self):
        self.blocks = {}
        with open("text") as f:
            for block in f.read().split(">*<"):
                tag, *lines = block.strip().split("\n")
                self.blocks[tag] = "\n".join(lines)

    def get(self, tag):
        return self.blocks[tag]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("block", help="Text block to print")
    args = parser.parse_args()
    t = Text()
    print(t.get(args.block))
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
