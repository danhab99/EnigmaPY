from enigma import *
import argparse
import sys, os

parser = argparse.ArgumentParser(description='A simulation of the enigma encryption algorithm', prog="enigma.py")
parser.add_argument('command',
    type=str,
    choices=['encrypt', 'create'],
    help='Which subroutine to run')
parser.add_argument('in_file',
    metavar='<Input file>',
    type=argparse.FileType('r'),
    help='The file to be encrypted')
parser.add_argument('out_file',
    metavar='<Output file>',
    type=argparse.FileType('w'),
    help='The output file')

args = parser.parse_args()

print(args.command)
