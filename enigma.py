from create import Create
from lib import Machine
from lib import Transformer
import argparse
# import sys, os
import pickle

parser = argparse.ArgumentParser(description='A simulation of the enigma encryption algorithm', prog='enigma.py')
subparsers = parser.add_subparsers(help='Which command to run', dest='subroutine')

create_parser = subparsers.add_parser('create', help='A utility to create encryption codexes')
encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file with a codex')

create_parser.add_argument('file',
    metavar='<File>',
    type=argparse.FileType('w'),
    help='The file to output to')
create_parser.add_argument('-r, --random',
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

encrypt_mutual = encrypt_parser.add_mutually_exclusive_group()
encrypt_mutual.add_argument('--codex',
    type=argparse.FileType('r'),
    help='The codex to use')
encrypt_mutual.add_argument('--random',
    action='store_true',
    help='Create a random codex')

args = parser.parse_args()

if (args.subroutine == 'create'):
    file = list(Create())
    with open(args.file.name, mode='wb+') as output:
        pickle.dump(file, output, pickle.HIGHEST_PROTOCOL)

if (args.subroutine == 'encrypt'):
    print('Encrypt subroutine')
