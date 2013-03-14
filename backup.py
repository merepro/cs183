#!/usr/bin/env python
import sys, getopt, re, subprocess,os,shutil,time, filecmp
from time import gmtime, strftime

stamp = time.strftime("%Y%m%d%H%M%S", gmtime())


shutil.copy2(sys.argv[1], sys.argv[1]+'.'+stamp)

diff=filecmp.cmp(sys.argv[1],sys.argv[1]+'.'+stamp)

#shutil.copy2(sys.argv[1], '/home/kevin/Desktop/newf.'+stamp)

#diff=filecmp.cmp(sys.argv[1],'/home/kevin/Desktop/newf.'+stamp)
if diff ==True:
	pass
	print sys.argv[1]+" has been backed up."
else:
	os.remove(sys.argv[1]+'.'+stamp)
