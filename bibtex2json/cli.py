import argparse
import sys

from .bibutils import cleanInputLine

def run():
    parser = argparse.ArgumentParser(description='Tranform BibTeX into minimally structured JSON')
    # If no input is given, default to stdin
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default = sys.stdin)
    
    # If no input is given, default to stdout
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'), default = sys.stdout)

    # Define translation mode/output format
    parser.add_argument('fmt', nargs='?', choices=['bibJSON-simple', 'bibJSON'], default='bibJSON-simple')
    
    args = parser.parse_args()
    inputData = [cleanInputLine(l) for l in args.input.readlines() if cleanInputLine(l) != '']
    if args.fmt == 'bibJSON-simple':
        from .bib2jsonsimple import parse
        outputData = parse(inputData)
    elif args.fmt == 'bibJSON':
        from .bib2json import parse
        outputData = parse(inputData)
    
    
