#!/usr/bin/env python

#Name: Hans Wun Kevin Ng
#Username: wunh ngk
#CS183
#Project 2

#Archive User Script

import sys,getopt, time, subprocess

def validate_login_existence(login):
    group_dict = {}
    group_file = open('/etc/passwd','r')
    for lines in group_file:
        line_list = lines.split(':')
        group_dict[line_list[0]] = line_list[2]
    if login in group_dict:
        return True
    print >> sys.stderr,'Error: login name does not exist in /etc/passwd'
    sys.exit(1)

def archive_user(login):
    timestamp = str(int(time.time()))
    print timestamp
    cmd = 'mv /home/'+login+' ./archived_homedirs/login.'+timestamp
    subprocess.Popen(str(cmd),stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,shell=True)
    cmd2 = 'sed /'+login+'/d /etc/passwd > ./test; mv -f ./test /etc/passwd; rm -f ./test'
    subprocess.Popen(str(cmd2),stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,shell=True)

def main(argv):
    login_name = ''
    try:
        opts, args = getopt.getopt(argv,"l:")
    except getopt.GetoptError:
        print >> sys.stderr,'usage: ./archive_user.py -l <login>'
        sys.exit(1)
    if len(opts) != 1:
        print >> sys.stderr,'usage: ./archive_user.py -l <login>'
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-l","--login"):
            login_name = arg
        else:
            print >> sys.stderr,'usage: ./archive_user.py -l <login>'
            sys.exit(1)
    if validate_login_existence(login_name):
	os.system("./backup.py /etc/passwd")
        archive_user(login_name)
    return

if __name__ == "__main__":
    main(sys.argv[1:])

