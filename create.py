from lib import *
import argparse
import string
from random import shuffle, sample, randint
from inspect import isclass
from create import Transformer

class Cypher():

    def __init__(self):
        self.abc = None
        self.transformers = list()

    def addTransformer(self, t):
        if (isinstance(t, Transformer) and not isclass(t)):
            if (t.cypher is None):
                raise ValueError("Cypher not set")
            self.transformers.append(t)

    def setABC(self, t):
        self.abc = t

    def ittTransformer(self):
        return self.transformers

    def getABC(self):
        return self.abc

def genPreset(p):
    if (p == 'ABC'):
        return list("abcdefghijklmmnopqrstuvwxyz")
    if (p == 'bytes'):
        return [str(bytes(i)) for i in range(0, 255)]
    if (p == 'numbers'):
        return [str(i) for i in range(0, 9)]
    if (p == 'ASCII'):
        return list(string.printable)
    if (p == 'UTF'):
        return [str(char(i)) for i in range(0, int(0x10ffff))]

def Create():
    parser = argparse.ArgumentParser(description='This interactive utility is used to help you create a custom cypher for the encryptor')

    def prompt():
        return parser.parse_args(input(">>> Create ").split())

    subparsers = parser.add_subparsers(help='Which command to run', dest='subroutine')

    set_alphabet = subparsers.add_parser('abc', help='Manage the alphabet being used, **do this first**')
    create_rotor = subparsers.add_parser('rotor', help='Rotors are transformers that rotate their cypher by one place per each use')
    create_plugboard = subparsers.add_parser('plugboard', help='Plugboards simply switch one symbol for another')
    end = subparsers.add_parser('end', help='Finalizes the cypher')

    abc_mutual = set_alphabet.add_mutually_exclusive_group(required=True)
    abc_mutual.add_argument('-r, --raw', help='Manually define an alphabet to be used')
    abc_mutual.add_argument('-p, --preset',
        help='Use one of the predefined alphabets',
        choices=['ABC', 'bytes', 'numbers', 'ASCII', 'UTF'],
        default='bytes',
        dest='preset')

    def addcypherArg(i):
        m = i.add_mutually_exclusive_group(required=True)
        m.add_argument('-c, --cypher', help='The cypher to use', dest='cypher')
        m.add_argument('-r, --random', help='Generates a random cypher', action='store_true', dest='cypher')

    create_rotor.add_argument('initial',
        help='The initial rotor position to start at (default = 0)',
        type=int,
        default=0)

    addcypherArg(create_rotor)
    addcypherArg(create_plugboard)

    parser.print_help()
    keepRunning = True
    ABC = None
    cypher = Cypher()

    def bakeCypherArgs(arg):
        # print(arg)
        if (arg.cypher is True):
            return sample(ABC, len(ABC))
        else:
            return arg.cypher

    while(keepRunning):
        try:
            args = prompt()

            if (args.subroutine == 'abc'):
                if (ABC):
                    raise ValueError("Alphabet already set")
                if (hasattr(args, 'raw')):
                    ABC = args.raw
                if (hasattr(args, 'preset')):
                    ABC = genPreset(args.preset)

                cypher.setABC(ABC)
                continue

            if (not ABC):
                raise ValueError('Please specify alphabet')

            if (args.subroutine == 'rotor'):
                cypher.addTransformer(Rotor(abc=ABC, cypher=bakeCypherArgs(args), initPos=args.initial))
                continue

            if (args.subroutine == 'plugboard'):
                cypher.addTransformer(Plugboard(abc=ABC, cypher=bakeCypherArgs(args)))
                continue

            if (args.subroutine == 'end'):
                keepRunning = False
                continue

        except ValueError as e:
            print(str(e))
            parser.print_help()
        except SystemExit:
            pass

    return cypher
def random(abc, min, max):
    c = Cypher()
    c.setABC(abc)

    def shuff():
        return sample(abc, len(abc))

    for i in range(min, max):
        if (randint(0, 1) == 0):
            c.addTransformer(Rotor(abc, shuff, randint(0, len(abc))))
        else:
            c.addTransformer(Plugboard(abc, shuff, randint(0, len(abc))))

    return c
