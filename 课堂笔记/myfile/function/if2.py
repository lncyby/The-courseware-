#!/usr/bin/python
#coding=utf-8

a=input()

if a>100:
    print "a>100"
elif a<=100:
    if a>50:
        print "50<a<=100"
    else:
        if a>=20:
            print "20<=a<=50"
        else:
            if a>=0:
                print "0<=a<=20"
            else:
                if a>=-10:
                    print "-10<=a<0"
                 else:
                     print "a<-10"


