#!/usr/bin/python
#coding=utf-8

a=input('你想打出杨辉三角多少项？', )
def triangle(a):
    l=[[1],[1,1]]
    for i in range(2,a):
        l.append([1,1])
        for k in range(1,i):
            l[i].insert(k,(l[i-1][k-1]+l[i-1][k]))
    for x in l:
        print x
triangle(a)
