#!/usr/bin
def rev(string):
	if len(string) == 0:
		return string
	else:
		return rev(string[1:]) + string[0]
def rev2(s):
	str = ""
	for i in s:
		str = i+str
	return str
def rev3(stream):
	return stream[::-1]
 
if __name__ == "__main__":
	string = raw_input("enter a string to be reversed \n")
	s = raw_input("enter another string \n")
        stream = raw_input("Enter 3rd string \n")
	print rev2(s)
        result = rev(string)
	print result
        print rev3(stream)
       


