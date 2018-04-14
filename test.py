import pdb, create

with open(args.test.name, mode='rb') as file:
    cypher = pickle.load(file)
    abc = cypher[0].getABC()
    # print(cypher)
    machine = Machine(abc)
    [machine.addTransformer(i) for i in cypher]

    def gen(length):
        c = [shuffle(abc)] * length
        return chain(c)

    def transform(d):
        return [machine.parse(i, value) for i, value in enumerate(d)]

    testData = gen(5)
    results = transform(transform(testData))
    if (False not in [item[0] == item[1] for item in zip(testData, results)]):
        print("This is a valid cypher")
    else:
        print("This is NOT a valid cypher")
