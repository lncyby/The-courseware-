#!/usr/bin/python

l=[1,2,3,4,5,6,7,8,9]

def fun6(a):
    for i in range(1,a+1):
        n=l[8]
        l.remove(l[8])
        l.insert(0,n)
    print l
a=input("Enter a number in [0,9]",)
fun6(a)
