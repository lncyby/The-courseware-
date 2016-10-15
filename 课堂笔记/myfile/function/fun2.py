#!/usr/bin/python

#奇数移到偶数之前
l1=[1,2,3,4,5,6,7,8,9]

def fun(l):
    for i in range(0,len(l)):
        if l[i]%2==0:
            l.append(l[i])
            l.remove(l[i])
fun(l1)
print l1

