import transformer

class Plugboard(transformer.Transformer):
    def __init__(self, abc, cypher):
        self.abc = abc
        self.cypher = cypher

    def parse(self, d, invert):
        if (invert):
            return self.cypher[self.abc.index(d)]
        else:
            return self.abc[self.cypher.index(d)]
