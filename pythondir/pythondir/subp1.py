#!/usr/bin
import sys
import subprocess

HOST = "127.0.0.1"
ssh = subprocess.Popen(["ssh",
                          "%s" % HOST],
                          stdin = subprocess.PIPE,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE)
ssh.stdin.write("ls .\n")
ssh.stdin.write("uname -a\n")
ssh.stdin.write("uptime\n")
ssh.stdin.close()
 
# fetch output
for line in ssh.stdout:
    print(line),
