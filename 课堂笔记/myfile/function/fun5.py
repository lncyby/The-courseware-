#!/usr/bin/python

k=raw_input()
def fun5(k):
    for i in k:
        if i not in {"0","1","2","3","4","5","6","7","8","9"}:
            k=k.replace(i,"a")
    l=k.split("a")
    for j in l:
        if j!='':
            print j
fun5(k)
