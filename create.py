from enigma import *
import argparse

def Create():
    parser = argparse.ArgumentParser(description='This interactive utility is used to help you create a custom codex for the encryptor')
    abc_mutual = parser.add_mutually_exclusive_group()
    abc_mutual.add_argument('--abc', help='Manually define an alphabet to be used')
    abc_mutual.add_argument('-p, --preset',
        help='Use one of the predefined alphabets',
        choices=['ABC', 'bytes', 'numbers', 'ASCII', 'UTF'],
        default='bytes')

    create_rotor = parser.add_subparsers('rotor', help='Rotors are transformers that rotate their codex by one place per each use')
    create_plugboard = parser.add_subparsers('plugboard', help='Plugboards simply switch one symbol for another')
    end = parser.add_subparsers('end', help='Finalizes the codex')

    def addCodexArg(i):
        i.add_argument('-c, --codex',
            help='The codex to use')

    create_rotor.add_argument('-i, --initial',
        help='The initial rotor position to start at (default = 0)',
        type=int,
        default=0)

    addCodexArg(create_rotor)
    addCodexArg(create_plugboard)

    parser.print_usage()
    keepRunning = True

    while(keepRunning):
        args = parser.parse_args(input(">"))
        
