
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
    
