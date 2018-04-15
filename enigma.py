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
encrypt_parser.add_argument('codex',
    type=argparse.FileType('r'),
    help='The codex to use')

args = parser.parse_args()

if (args.test):
    with open('cypher.pkl', mode='rb') as file:
        cypher = pickle.load(file)
        abc = cypher.getABC()
        # print(cypher)
        machine = Machine(cypher)

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


if (args.subroutine == 'create'):
    file = create.Create()
    with open(args.file.name, mode='wb+') as output:
        pickle.dump(file, output)

if (args.subroutine == 'encrypt'):
    machine = None
    with open(args.codex.name, 'rb') as file:
        machine = Machine(pickle.load(file))

    with open(args.in_file.name, mode='rb') as input, open(args.out_file.name, mode='wb+') as output:
        for chunk in iter(lambda: input.read(2 ** 7), b''):
            crypt = [machine.parse(item, index) for index, item in enumerate(chunk)]
            output.write(crypt)
