#!/usr/bin
import subprocess
import os
def filelist(spath):
	for path,subdirs,files in os.walk(spath):
		for name in files:
			print path.join(path,name)

if __name__ == "__main__":
#	subprocess.call(['ls','-al'],shell=True)
	spath = subprocess.call(['echo $HOME'],shell=True)
	print spath

