#!/usr/bin/python

def fun4(a):
    l=a.split(" ")
    n=l[0]
    for i in range(1,len(l)):
        n+=l[i]
    l1=n.split("-")
    m=l1[0]
    for j in range(1,len(l1)):
        m+=l1[i]
    print str(m)
while True:
    s=raw_input()
    if s=='':
        break
    fun4(s)
