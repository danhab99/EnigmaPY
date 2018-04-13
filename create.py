from enigma import *
import argparse
import string

def genPreset(p):
    if (p == 'ABC'):
        return list("abcdefghijklmmnopqrstuvwxyz")
    if (p == 'bytes'):
        return [str(bytes[i]) for i in range(0, 255)]
    if (p == 'numbers'):
        return [str(i) for i in range(0, 9)]
    if (p == 'ASCII'):
        return list(string.printable)
    if (p == 'UTF'):
        return [str(char(i)) for i in range(0, int(0x10ffff))]

def Create():
    parser = argparse.ArgumentParser(description='This interactive utility is used to help you create a custom cypher for the encryptor')
    abc_mutual = parser.add_mutually_exclusive_group()
    abc_mutual.add_argument('--abc', help='Manually define an alphabet to be used')
    abc_mutual.add_argument('-p, --preset',
        help='Use one of the predefined alphabets',
        choices=['ABC', 'bytes', 'numbers', 'ASCII', 'UTF'],
        default='bytes',
        dest='preset')

    parser.print_usage()

    def prompt():
        return parser.parse_args(input("create ").split())

    temp = prompt()
    ABC = temp.abc

    if (temp.preset is not None and temp.ABC is None):
        ABC = genPreset(temp.prompt)


    parser = argparse.ArgumentParser(description='This interactive utility is used to help you create a custom cypher for the encryptor')
    subparsers = parser.add_subparsers('command', help='Which command to run', dest='subroutine')

    create_rotor = subparsers.add_subparsers('rotor', help='Rotors are transformers that rotate their cypher by one place per each use')
    create_plugboard = subparsers.add_subparsers('plugboard', help='Plugboards simply switch one symbol for another')
    end = subparsers.add_subparsers('end', help='Finalizes the cypher')

    def addcypherArg(i):
        i.add_argument('-c, --cypher',
            help='The cypher to use')

    create_rotor.add_argument('-i, --initial',
        help='The initial rotor position to start at (default = 0)',
        type=int,
        default=0)

    addcypherArg(create_rotor)
    addcypherArg(create_plugboard)

    parser.print_usage()
    keepRunning = True

    while(keepRunning):
        args = prompt()

        if (args.subroutine == 'rotor'):
            yield enigma.Rotor(abc=ABC, cypher=args.cypher, initPos=args.initial)
            continue

        if (args.subroutine == 'plugboard'):
            yield enigma.Plugboard(abc=ABC, cypher=args.cypher)
            continue

        if (args.subroutine == 'end')
            keepRunning = False
            continue
