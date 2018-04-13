from enigma import *
import argparse

def Create():
    parser = argparse.ArgumentParser(description='This interactive utility is used to help you create a custom codex for the encryptor')
    parser.print_usage()
    keepRunning = True

    while(keepRunning):
        args = parser.parse_args(input(">"))
        
