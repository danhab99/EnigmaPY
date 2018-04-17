import pdb, create, pickle
from random import sample
from itertools import chain
from lib import Machine

with open('cypher.pkl', mode='rb') as file:
    cypher = pickle.load(file)

    abc = cypher.ittTransformer()[0].getABC()
    machine = Machine(cypher)

    def gen(length):
        c = [sample(abc, len(abc))] * length
        return chain.from_iterable(c)

    def transform(d):
        return [machine.parse(value, counter) for counter, value in enumerate(d)]

    testData = list(gen(5))
    results = transform(transform(testData))
    if (False not in [item[0] == item[1] for item in zip(testData, results)]):
        print("This is a valid cypher")
    else:
        print("This is NOT a valid cypher")
