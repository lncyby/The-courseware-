#!/usr/bin/python
#coding=utf-8

#完数 ：除了本身以外的所有约数的和等于它本身。

for i in range(1,1001):
    sum=0
    for j in range(1,i/2+1):
        if i % j ==0:        
            sum+=j
    if sum==i:
        print i
