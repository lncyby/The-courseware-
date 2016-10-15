#!/usr/bin/python
#coding=utf-8

for x in range(100,1000):
    l=str(x)
    if int(l[0])**3+int(l[1])**3+int(l[2])**3 == x:
        print x
