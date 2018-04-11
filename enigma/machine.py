import transformer

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
