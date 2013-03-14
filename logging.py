#!/usr/bin/env python
import sys,os,subprocess,time
from time import gmtime, strftime
stamp = time.strftime("%a %b %H:%M:%S %Z %Y", gmtime())
with open("./accounts.log", "a") as myfile:
    myfile.write(stamp+' '+sys.argv[1])
#print stamp
#print sys.argv[1]
