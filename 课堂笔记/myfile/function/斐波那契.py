#!/usr/bin/python
#coding=utf-8

a=input("你想打印斐波那契数列多少项？",)
i=0
l=[1,1]
while i<a:
    n=l[len(l)-1]+l[len(l)-2]
    l.append(n)
    i+=1


print l
