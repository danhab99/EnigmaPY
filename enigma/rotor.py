import transformer

class Rotor(transformer.Transformer):

    def __init__(self, abc cypher, initPos):
        self.cypher = cypher
        self.offset = initPos
        self.cypher = cypher
        self.abc = abc

    def parse(self, d, invert):
        def next():
            r = self.offset + 1
            self.offset = r
            if (self.offset >= len(self.cypher)):
                self.offset = len(self.cypher)

            return r

        def rotate(l, n):
            return l[-n:] + l[:-n]

        newCypher = rotate(self.cypher, self.offset)
        newABC = rotate(self.abc, self.offset)

        if (invert):
            return newCypher[newABC.index(d)]
        else:
            return newABC[newCypher.index(d)]
