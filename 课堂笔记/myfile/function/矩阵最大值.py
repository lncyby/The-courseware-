#!/usr/bin/python
#coding=utf-8

l=[[3,9,12,8],[4,20,15,9],[9,17,11,2]]
i=[0][0]
for x in range(3):
    for y in range(4):        
        if l[x][y]>i:
            i=l[x][y]
print "max=%d,the site is [%d,%d]"%(i,x,y)

