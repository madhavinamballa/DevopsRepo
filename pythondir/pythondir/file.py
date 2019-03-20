#!/usr/bin
import os
from os.path import join
cwd = os.getcwd()
os.path.exists('test.txt')
print cwd
# get the count of files in given directory
count = 0
for (dirname,dirs,files) in os.walk(cwd):
	for filename in files:
		if filename.endswith('.py'):
			count += 1
print 'Files: ',count
	
#print out the files and size of each file
for (dirname,dirs,files) in os.walk(cwd):
	for filename in files:
		if filename.endswith('.py'):
			thefile = os.path.join(dirname,filename)
			print os.path.getsize(thefile),thefile
			
