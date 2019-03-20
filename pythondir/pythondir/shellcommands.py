#!/usr/bin
import os
import subprocess
mycmd = 'echo $HOME'
os.system(mycmd)
# stor output of shell command
com = os.popen("echo $PWD").read()
print com

#execute shell commands using subprocess module
subprocess.call("ls")
subprocess.call(["ls", "-l","."])
# store shell command output
myout = subprocess.Popen(['ansible','--version'],
             stdout=subprocess.PIPE,
             stderr=subprocess.STDOUT)
stdout,stderr = myout.communicate()
print(stdout)
print(stderr)
