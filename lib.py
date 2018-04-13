class Transformer:

    def parse(self, d, invert):
        pass;

class Rotor(transformer.Transformer):

    def __init__(self, abc, cypher, initPos):
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

class Plugboard(transformer.Transformer):
    def __init__(self, abc, cypher):
        self.abc = abc
        self.cypher = cypher

    def parse(self, d, invert):
        if (invert):
            return self.cypher[self.abc.index(d)]
        else:
            return self.abc[self.cypher.index(d)]

class Machine:

    def __init__(self, abc):
        self.abc = abc;
        self.transformer = [transformer]

    def addTransformer(self, *t):
        if False not in [type(i) == transformer.Transformer for i in t]:
            self.transformer.append(t)
        else
            raise ValueError("Parameter(s) must be a transformer")

    def parse(self, d):
        r = self.abc.index(d)
        for trans in self.transformer:
            r = trans.parse(r, False)

        r = invert(r)

        for trans in reversed(self.transformer):
            r = trans.parse(r, True)

        return r

    def invert(self, d):
        work = self.abc.index(d)
        work = word / len(self.abc)
        work = 1 - work
        work = work * len(self.abc)
        return self.abc[work]
