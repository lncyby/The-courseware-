#!/usr/bin/python
#coding=utf-8

#输入日期，确定是当年的多少天。
a=raw_input("Please input your date>",) #input date

l=a.split('-')  #把字符串形式的年月日按-分割并放在列表里。
y=int(l[0])
m=int(l[1]) 
d=int(l[2])
sum=0
dcount=[31,28,31,30,31,30,31,31,30,31,30,31]
if (y%4==0 and y%100 !=0) or y%400==0 :
    dcount[1]+=1

for i in range(0,m-1):
    sum+=dcount[i]
print "This date is the %d day!"%(sum+d)
