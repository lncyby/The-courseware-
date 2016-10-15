#!/usr/bin/python


for a in  range(5,101):
    l=[]
    for b in range(2,a/2):
        l.append(a%b)
    if 0 in l:
        continue
    else:
        print a

    



