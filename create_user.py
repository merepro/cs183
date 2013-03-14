#!/usr/bin/env python

#Name: Hans Wun Kevin Ng
#Username: wunh ngk
#CS183
#Project 2

#Create user script

import sys, getopt, re, subprocess

def check_syntax_login(login_name):
    regex = re.search('(^[a-zA-Z0-9]+$)',login_name)
    if regex:
        return True
    return False

def validate_login(login_name,passwd_dict):
    if not login_name in passwd_dict:
        return True
    return False

def check_syntax_uid(user_id):
    regex = re.search('(^[0-9]+$)',user_id)
    if regex:
        return True
    return False

def validate_uid(user_id,passwd_dict):
    if not user_id in passwd_dict.values():
        return True
    return False

def check_syntax_gid(group_id):
    regex = re.search('(^[0-9]+$)',group_id)
    if regex:
        return True
    return False

def validate_gid(group_id,group_dict):
    if group_id in group_dict:
        return True
    return False

def validate_directory(home_dir, passwd_dict):
    if not home_dir in passwd_dict.values():
        return True
    return False

def validate_dir_path(home_dir):
    dir_split = home_dir.split('/')
    if 'home' in dir_split:
        return True
    return False

def validate_shell_option(shell):
    if shell == '/bin/bash' or shell == '/bin/tcsh':
        return True
    return False

def validate_checks(login_name,user_id,group_id,home_dir,shell,passwd_dict,group_dict):
    if not check_syntax_login(login_name):
        print >> sys.stderr,'Invalid login syntax, must be alphanumeric'
        os.system("./logging.py 'WARN Invalid login syntax, must be alphanumeric'")
        sys.exit(1)
    elif not validate_login(login_name,passwd_dict):
        print >> sys.stderr,'Error: login exists in /etc/passwd'
        os.system("./logging.py 'WARN Error: login exists in /etc/passwd'")
        sys.exit(1)
    elif not check_syntax_uid(user_id):
        print >> sys.stderr, 'Invalid user ID syntax, must be numeric'
        os.system("./logging.py 'WARN Invalid user ID syntax, must be numeric'")
        sys.exit(1)
    elif not validate_uid(user_id,passwd_dict):
        print >> sys.stderr, 'Error: user ID exists in /etc/passwd'
        os.system("./logging.py 'WARN Error: user ID exists in /etc/passwd'")
        sys.exit(1)
    elif not check_syntax_gid(group_id):
        print >> sys.stderr, 'Invalid group ID syntax, must be numeric'
	os.system("./logging.py 'WARN Invalid group ID syntax, must be numeric'")
        sys.exit(1)
    elif not validate_gid(group_id,group_dict):
        print >> sys.stderr, 'Error: group ID does not exist in /etc/passwd'
	os.system("./logging.py 'WARN Error: group ID does not exist in /etc/passwd'")
        sys.exit(1)
    elif not validate_directory(home_dir,passwd_dict):
        print >> sys.stderr, 'Error: home directory does not exist in /etc/passwd'
	os.system("./logging.py 'WARN Error: home directory does not exist in /etc/passwd'")
        sys.exit(1)
    elif not validate_dir_path(home_dir):
        print >> sys.stderr, 'Error: directory is not a directory within home'
	os.system("./logging.py 'WARN Error: directory is not a directory within home'")
        sys.exit(1)
    elif not validate_shell_option(shell):
        print >> sys.stderr, 'Invalid shell option, choices are /bin/bash or /bin/tcsh'
	os.system("./logging.py 'WARN Invalid shell option, choices are /bin/bash or /bin/tcsh'")
        sys.exit(1)
    else:
        return True

def create_user(login,user_id,group_id,GECOS,home_dir,shell):
    cmd = 'echo '+login+':'+'x:'+user_id+':'+group_id+':'+GECOS+':'+home_dir+':'+shell+ ' >> ./passwd'
    cmd2 = 'sort -g -t : -k 3 /etc/passwd/ > ./.tmp; cat ./.tmp > /etc/passwd; rm -f ./.tmp'
    print cmd
    subprocess.Popen(str(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                     shell=True).communicate()
    subprocess.Popen(str(cmd2),stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                     shell=True).communicate()
    os.system("./logging.py 'INFO Created user'")
    return


def main(argv):
    passwd_dict = {}
    group_dict = {}
    passwd_file = open('/etc/passwd','r')
    group_file = open('/etc/group','r')
    for group_lines in group_file:
        group_list = group_lines.split(':')
        group_dict[group_list[2]] = group_list[2]
    for lines in passwd_file:
        line_list = lines.split(':')
        passwd_dict[line_list[0]] = line_list[2]
        passwd_dict[line_list[3]] = line_list[5]
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
    if validate_checks(login_name,user_id,group_id,home_dir,shell,passwd_dict,group_dict):
	os.system("./backup.py /etc/passwd")
        create_user(login_name,user_id,group_id,GECOS,home_dir,shell)
	
    return

if __name__ == "__main__":
    main(sys.argv[1:])
