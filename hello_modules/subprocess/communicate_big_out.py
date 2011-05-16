#!/bin/env python
# -*- coding: utf-8 -*-


from subprocess import PIPE, Popen

cmd = ['python', 'stub.py', str(32), str(1024 * 1024)]


def main():
    proc = Popen(cmd, stdout=PIPE)
    (stdout, _) = proc.communicate()

    print '%d bytes received. press return. : ' % len(stdout),
    raw_input()


if __name__ == '__main__':
    main()
