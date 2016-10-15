#!/usr/bin/python
#coding=utf-8

l=[1]
for x in [1,2,3,4,5,6,7,8,9]:
    for y in l:
        print "" "%d×%d=%d\t"%(y,x,x*y),
    print
    n=y+1
    l.append(n)



        
