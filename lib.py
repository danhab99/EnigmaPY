from abc import ABC, abstractmethod
from inspect import isclass
import pdb
import traceback

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
            return newCypher.index(newABC[d])
        else:
            return newABC.index(newCypher[d])

class Plugboard(Transformer):
    def __init__(self, abc, cypher):
        super().__init__(abc, cypher)

    def parse(self, d, index, invert):
        if (invert):
            return self.cypher.index(self.abc[d])
        else:
            return self.abc.index(self.cypher[d])

class Machine:

    def __init__(self, cypher):
        self.cypher = cypher
        self.abc = self.cypher.ittTransformer()[0].getABC()

    def parse(self, d, index):
        try:
            if (type(d) is int):
                d = bytes([d])

            r = self.abc.index(d)

            for trans in list(self.cypher.ittTransformer()):
                r = trans.parse(d=r, index=index, invert=False)

            r = self.invert(r)

            for trans in reversed(self.cypher.ittTransformer()):
                r = trans.parse(d=r, index=index, invert=True)

            return self.abc[r]
        except:
            traceback.print_exc()
            pdb.set_trace()
            return self.parse(d, index)

    def invert(self, i):
        l = len(self.abc) - 1
        return l - i
