#!/usr/bin/python
passwordFile = open('secretpassword.txt')
secretpassword = passwordFile.read().strip()
print("Enter password")
tpassword = raw_input().strip()
if tpassword == secretpassword:
	print("Acess granted")
else:
	print("Acess denied")
