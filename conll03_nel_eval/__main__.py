#!/usr/bin/env python
import argparse
import sys
from filter import Filter
from evaluate import Evaluate

APPS = [
    Filter,
    Evaluate,
]

def main(args=sys.argv[1:]):
    p = argparse.ArgumentParser(description='Evaluation tools for Named Entity Linking output.')
    p.add_argument('fname', metavar='FILE')
    sp = p.add_subparsers()
    for a in APPS:
        a.add_arguments(sp)

    namespace = vars(p.parse_args(args))
    cls = namespace.pop('cls')
    cls(**namespace)

if __name__ == '__main__':
    main()