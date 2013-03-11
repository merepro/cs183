#! /bin/usr/env python

#Name: Hans Wun Kevin Ng
#Username: wunh ngk
#CS183
#Project 2

#Add Group Script

import sys, getopt, time, re, os

def main(argv):
    group_name = ''
    group_id = ''
    try:
        opts, args = getopt.getopt(argv,"n:g:")
    except getopt.GetoptError:
        print 'usage: add_group.py -n <name> -g <gid>'
        sys.exit(1)
    if len(opts) != 2:
        print 'usage: add_group.py -n <name> -g <gid>'
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-n","--name"):
            group_name = arg
        elif opt in ("-g", "--gid"):
            group_id = arg
        else:
            print 'usage: add_group.py -n <name> -g <gid>'
            sys.exit(1)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
