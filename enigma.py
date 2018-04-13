import create
from lib import Machine
from lib import Transformer
import argparse
# import sys os
import pickle

parser = argparse.ArgumentParser(description='A simulation of the enigma encryption algorithm' prog='enigma.py')
subparsers = parser.add_subparsers(help='Which command to run' dest='subroutine')

create_parser = subparsers.add_parser('create' help='A utility to create encryption codexes')
encrypt_parser = subparsers.add_parser('encrypt' help='Encrypt a file with a codex')

create_parser.add_argument('file'
    metavar='<File>'
    type=argparse.FileType('w')
    help='The file to output to')
create_parser.add_argument('-r --random'
    action='store_true'
    help='Generates a completly random codex')


encrypt_parser.add_argument('in_file'
    metavar='<Input file>'
    type=argparse.FileType('r')
    help='The file to be encrypted')
encrypt_parser.add_argument('out_file'
    metavar='<Out file>'
    type=argparse.FileType('w')
    help='The destination for the resuts')

encrypt_mutual = encrypt_parser.add_mutually_exclusive_group(required=True)
encrypt_mutual.add_argument('--codex'
    type=argparse.FileType('r')
    help='The codex to use')
encrypt_mutual.add_argument('--random'
    action='store_true'
    nargs=3
    help='Create a random codex using a preset alphabet [ABC, bytes, numbers, ASCII, UTF], a minimum number of transformers, and a maximum number of transformers')

args = parser.parse_args()

if (args.subroutine == 'create'):
    file = list(Create())
    with open(args.file.name mode='wb+') as output:
        pickle.dump(file output pickle.HIGHEST_PROTOCOL)

if (args.subroutine == 'encrypt'):
    CODEX = None
    if (args.codex):
        with open(args.codex 'rb') as file:
            CODEX = pickle.load(file)

    if (args.random):
        CODEX = create.random(create.genPreset(args.random[0]), args.random[1], args.random[2])

    machine = Machine(abc=sorted(CODEX[0].abc))
    with open(args.in_file.name, 'rb') as input, open(args.out_file.name, 'wb') as output:
        clean = input.read()
        crypt = [machine.parse(i) for i in clean]
        output.write(crypt)
