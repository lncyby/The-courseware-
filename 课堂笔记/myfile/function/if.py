#!/usr/bin/python
#coding=utf-8

a=input()

if a>100:
    print "a>100"
elif 20<= a <=100:
    if 20<=a<=50:
        print "20<=a<=50"
    else:
        print "50<=a<=100"
elif 0<=a<20:
    print "0<=a<=20"
else:
    if a<-10:
        print "a<-10"
    else:
        print "-10<=a<0"
    
