#!/usr/bin/python
n = input()
s = set(map(int, raw_input().split()))
N = input()
for i in range(N):
    option = raw_input().split()
    if option[0] == 'pop':
        s.pop()
    elif option[0] == 'remove':
        s.remove(int(option[1]))
    elif option[0] == 'discard':
        s.discard(int(option[1]))
print sum(s)

