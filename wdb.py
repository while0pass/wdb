#! /usr/bin/env python2
# coding: utf-8
import pdb, warnings, sys
import __builtin__

if __name__ == '__main__':
    args, n = [], len(sys.argv)
    if n < 2:
        sys.exit(1)
    elif n > 2:
        args.append(__builtin__.__dict__[sys.argv[2]])
        if n > 3:
            args.append(int(sys.argv[3]))
    warnings.simplefilter('error', *args)  # treat warnings as exceptions

        # TODO: Вместо ``warnings.simplefilter`` можно использовать
        # ``warnings.filterwarnings`` как более гибкое средство.

    try:
        execfile(sys.argv[1])
    except:
        pdb.post_mortem(sys.exc_info()[-1])
