#!/usr/bin
def rev(s):
	return s[::-1]
def rev2(s):
	str = ""
	for i in s:
		str = i+str
	return str
def rev2(s):
	if len(s) == 0:
		return s
	else:
		retrun (rev(s)+s[0])
if __name__ == "__main__":
	s = raw_input("enter a stirng to be reversed \n")
	print rev(s)
