#!/usr/bin/python

def p(n,x):
    if n>1:
        return ((2*n-1)*x*p(n-1,x)-(n-1)*p(n-2,x))/n
    if n==1:
        return x
    if n==0:
        return 1
a=input()
b=input()
print p(a,b)
