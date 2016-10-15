#!/usr/bin/python

b='abcdabcaab'
a='a'
def fun3(a,b):
    s=b.count(a)
    return s
print "%s contain %d %s"%(b,fun3(a,b),a)
