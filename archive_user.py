#!/usr/bin/env python

#Name: Hans Wun Kevin Ng
#Username: wunh ngk
#CS183
#Project 2

#Archive User Script

import sys,getopt

def archive_users():
    return

def main(argv):
    login_name = ''
    try:
        opts, args = getopt.getopt(argv,"l:")
    except getopt.GetoptError:
        print 'usage: ./archive_user.py -l <login>'
        sys.exit(1)
    if len(opts) != 1:
        print 'usage: ./archive_user.py -l <login>'
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-l","--login"):
            login_name = arg
            print login_name
        else:
            print 'usage: ./archive_user.py -l <login>'
            sys.exit(1)
    return

if __name__ == "__main__":
    main(sys.argv[1:])

