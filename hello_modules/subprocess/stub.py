#!/bin/env python
# -*- coding: utf-8 -*-


import sys


def usage():
    print '''
usage:
    %s <col width> <line count>

produces <line count> lines of <col width> chars.
''' % sys.argv[0]


def main():
    try:
        cols = int(sys.argv[1])
        lines = int(sys.argv[2])
    except:
        usage()
        exit()

    fmt = '%%0%dd' % cols

    for i in xrange(lines):
        print fmt % i


if __name__ == '__main__':

    main()

