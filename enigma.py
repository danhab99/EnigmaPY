import create
from lib import Machine
from lib import Transformer
import argparse
import pickle
from itertools import chain
from random import shuffle

parser = argparse.ArgumentParser(description='A simulation of the enigma encryption algorithm', prog='enigma.py')

subparsers = parser.add_subparsers(help='Which command to run', dest='subroutine')

create_parser = subparsers.add_parser('create', help='A utility to create encryption codexes')
encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file with a codex')

parser.add_argument('--test',
    type=argparse.FileType('r'),
    help='Validate a cypher')

create_parser.add_argument('file',
    metavar='<File>',
    type=argparse.FileType('w'),
    help='The file to output to')
create_parser.add_argument('-r --random',
    action='store_true',
    help='Generates a completly random codex')


encrypt_parser.add_argument('in_file',
    metavar='<Input file>',
    type=argparse.FileType('r'),
    help='The file to be encrypted')
encrypt_parser.add_argument('out_file',
    metavar='<Out file>',
    type=argparse.FileType('w'),
    help='The destination for the resuts')

encrypt_mutual = encrypt_parser.add_mutually_exclusive_group(required=True)
encrypt_mutual.add_argument('--codex',
    type=argparse.FileType('r'),
    help='The codex to use')
encrypt_mutual.add_argument('--random',
    nargs=3,
    help='Create a random codex using a preset alphabet [ABC, bytes, numbers, ASCII, UTF], a minimum number of transformers, and a maximum number of transformers')

args = parser.parse_args()

if (args.test):
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

if (args.subroutine == 'create'):
    file = list(create.Create())
    with open(args.file.name, mode='wb+') as output:
        pickle.dump(file, output)

if (args.subroutine == 'encrypt'):
    CYPHER = None
    if (args.codex):
        with open(args.codex, 'rb') as file:
            CYPHER = pickle.load(file)

    if (args.random):
        CYPHER = create.random(create.genPreset(args.random[0]), args.random[1], args.random[2])

    machine = Machine(abc=CYPHER[0].getABC())
    with open(args.in_file.name, 'rb') as input, open(args.out_file.name, 'wb') as output:
        clean = input.read()
        crypt = [machine.parse(i, value) for i in enumerate(clean)]
        output.write(crypt)
