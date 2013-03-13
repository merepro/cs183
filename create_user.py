#!/usr/bin/env python

#Name: Hans Wun Kevin Ng
#Username: wunh ngk
#CS183
#Project 2

#Create user script

import sys, getopt

def validate_checks():

    return

def create_user(login,user_id,group_id,GECOS,home_dir,shell):
    return


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"l:u:g:i:d:s:")
    except getopt.GetoptError:
        print >> sys.stderr,"usage: ./create_user.py -l <login> -u <uid> -g <gid> -i <GECOS> -d <home directory> -s <shell>"
        sys.exit(1)
    if len(opts) != 6:
        print >> sys.stderr,"usage: ./create_user.py -l <login> -u <uid> -g <gid> -i <GECOS> -d <home directory> -s <shell>"
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-l","--login"):
            login_name = arg
        elif opt in ("-u","--uid"):
            user_id = arg
        elif opt in ("-g","--gid"):
            group_id = arg
        elif opt in ("-i", "--GECOS"):
            GECOS = arg
        elif opt in ("-d", "--dir"):
            home_dir = arg
        elif opt in ("-s", "--shell"):
            shell = arg
        else:
            print >> sys.stderr,"usage: ./create_user.py -l <login> -u <uid> -g <gid> -i <GECOS> -d <home directory> -s <shell>"
            sys.exit(1)
        if validate_checks():
            create_user(login_name,user_id,group_id,GECOS,home_dir,shell)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
