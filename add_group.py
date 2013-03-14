#!/usr/bin/env python

#Name: Hans Wun Kevin Ng
#Username: wunh ngk
#CS183
#Project 2

#Add Group Script

import sys, getopt, re, subprocess,os


def check_syntax_group_name(group_name):
    regex = re.search('(^[a-zA-Z0-9]+$)',group_name)
    if regex:
        return True
    print >> sys.stderr, "Invalid group name syntax"
    sys.exit(1)
def check_syntax_gid(gid):
    regex = re.search('(^0*(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$)',gid)
    if regex:
        return True
    print >> sys.stderr, "Invalid GID syntax"
    sys.exit(1)

def add_group(name,gid):
    cmd = 'groupadd -g '+ gid + ' ' + name
    print cmd
    subprocess.Popen(str(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True).communicate()[0]
    return 0

def validate_group_name_and_gid(name,gid,group_dict):
    if not name in group_dict and not gid in group_dict.values():
        return True
  
    print >> sys.stderr, "Error validating group name or GID"
    sys.exit(1)

def main(argv):
    group_dict = {}
    group_file = open('/etc/group','r')
    for lines in group_file:
        line_list = lines.split(':')
        group_dict[line_list[0]] = line_list[2]
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
    if validate_group_name_and_gid(group_name,group_id,group_dict):
        print "key and value are unique"
        if check_syntax_group_name(group_name) and check_syntax_gid(group_id):
            print "key and value have correct syntax"
            add_group(group_name, group_id)
	    os.system("./backup.py /etc/group")
        return

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
