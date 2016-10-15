#!/usr/bin/python

def fun(a,b):
    print a,b
def fun1(a,b=0):
    print a
    print b
fun1(1)
def fun2(*a):
    print a
fun2(1,2,3,4,5)

def fun4(**a):
    print a
fun4(a=1,b=2,c=3)

def fun5(b,*a):
    print a
    print b
fun5(1,2,3,4,5)



def fun7(**a,b):
    print a,b
fun7(a=10,b=11,c=20)
