#!/use/bin
import os
from fnmatch import fnmatch
def printfile(spath):
	for path,subdirs,files in os.walk(spath):
		for name in files:
			print os.path.join(path,name)
def patternmatch(spath,pattern):
	for path,subdirs,files in os.walk(spath):
		for name in files:
			if fnmatch(name,pattern):
				print os.path.join(path,name)

if __name__ == "__main__":	
	spath = raw_input("enter a path \n")
        #printfile(spath)
	pattern = raw_input("enter type of file you are looking for \n")
        patternmatch(spath,pattern)
	
