import pdb, create, pickle
from random import sample
from itertools import chain

with open('testCypher.pkl', mode='rb') as file:
    cypher = pickle.load(file)
    abc = cypher[0].getABC()
    # print(cypher)
    machine = create.Machine(abc)
    [machine.addTransformer(i) for i in cypher]

    def gen(length):
        c = [sample(abc, len(abc))] * length
        return chain.from_iterable(c)

    def transform(d):
        return [machine.parse(value, counter) for counter, value in enumerate(d)]

    testData = list(gen(5))
    pdb.set_trace()
    results = transform(transform(testData))
    if (False not in [item[0] == item[1] for item in zip(testData, results)]):
        print("This is a valid cypher")
    else:
        print("This is NOT a valid cypher")
