#!/usr/bin/env python
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run python code like awk. '
        'If -n is used, "s" will refer to each line, stripped. '
        'Otherwise, it will refer to the whole stdin.')
    parser.add_argument('command', help='snippet of python code')
    parser.add_argument('-i', help='import statments')
    parser.add_argument('-n', action='store_true', help='execute command for each line')
    opts = parser.parse_args()

    if opts.i:
        exec opts.i

    if opts.n:
        for line in sys.stdin:
            s = line.strip()
            exec opts.command
    else:
        s = sys.stdin.read()
        exec opts.command

if __name__ == '__main__':
    main()
