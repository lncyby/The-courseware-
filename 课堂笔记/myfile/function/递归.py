#!/usr/bin/python

def action(n):
    if n<=1:
        return 1
    return (n*action(n-1))
print action(5)
