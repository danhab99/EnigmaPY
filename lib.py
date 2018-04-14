from abc import ABC, abstractmethod

class Transformer(ABC):

    def __init__(self, abc, cypher):
        self.abc = abc
        self.cypher = cypher

    @abstractmethod
    def parse(self, d, index, invert):
        pass;

    def getABC(self):
        return self.abc

    def getCypher(self):
        return self.cypher

class Rotor(Transformer):

    def __init__(self, abc, cypher, initPos):
        super().__init__(abc, cypher)
        self.offset = initPos

    def parse(self, d, index, invert):
        def rotate(l, n):
            return l[-n:] + l[:-n]

        labc = len(self.abc)
        offset = index
        while (offset > labc):
            offset = offset - labc

        newCypher = rotate(self.cypher, offset)
        newABC = rotate(self.abc, offset)

        if (invert):
            return newCypher[newABC.index(d)]
        else:
            return newABC[newCypher.index(d)]

class Plugboard(Transformer):
    def __init__(self, abc, cypher):
        super().__init__(abc, cypher)

    def parse(self, d, index, invert):
        if (invert):
            return self.cypher[self.abc.index(d)]
        else:
            return self.abc[self.cypher.index(d)]

class Machine:

    def __init__(self, abc):
        self.abc = abc;
        self.transformer = [Transformer]

    def addTransformer(self, *t):
        self.transformer.append(t)

    def parse(self, d, index):
        D = str(d)
        r = self.abc.index(D)
        for trans in self.transformer:
            r = trans.parse(d=r, index=index, invert=False)

        r = invert(r)

        for trans in reversed(self.transformer):
            r = trans.parse(d=r, index=index, invert=True)

        return r

    def invert(self, d):
        work = self.abc.index(d)
        work = word / len(self.abc)
        work = 1 - work
        work = work * len(self.abc)
        return self.abc[work]
