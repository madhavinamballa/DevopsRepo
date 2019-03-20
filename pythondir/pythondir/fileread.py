#!/usr/bin
import os
cwd = os.getcwd()
print cwd
for (dirname,dirs,files)in os.walk(cwd):
	for filename in files:
		if filename.endswith('.py'):
			thefile = os.path.join(dirname,filename)
			size = os.path.getsize(thefile)
			if size == 2578 or size == 2565:
				continue
			fhand = open(thefile,'r')
			lines = list()
			for line in fhand:
				lines.append(line)
			fhand.close()
			if len(lines) > 1:
				print len(lines),thefile
				print lines[1:4]
