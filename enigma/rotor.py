import transformer

class Rotor(transformer.Transformer):

    def __init__(self, abc cypher, initPos):
        self.cypher = cypher
        self.offset = initPos
        self.cypher = cypher
        self.abc = abc

    def parse(self, d, invert):
