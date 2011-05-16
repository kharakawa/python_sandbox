#!/bin/env python
# -*- coding: utf-8 -*-


from subprocess import PIPE, Popen

cmd = ['python', 'stub.py', str(32), str(1024 * 1024)]


def main():
    proc = Popen(cmd, stdout=PIPE)
    sumlen = 0
    
    for l in proc.stdout:
        sumlen += len(l)
    
    proc.wait()

    print '%d bytes received. press return. : ' % sumlen,
    raw_input()


if __name__ == '__main__':
    main()
