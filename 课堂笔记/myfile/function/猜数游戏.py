#!/usr/bin/python
#coding=utf-8
import random

#猜数游戏。
#Name:chance.Lee
#E-mail:292808135@qq.com

i=1
while i<=4:
    num=random.randint(0,9)
    print "Please input your number >"
    a=input()
    if a ==num:
        print "恭喜你，猜对了！"
        break
    else:
        if a<num:
            print "sorry,猜小了,正确的是%d,你还有%d次机会。"%(num,4-i)
        else:
            print "sorry,猜大了,正确的是%d,你还有%d次机会。"%(num,4-i)
    i+=1
else:
    print "game over"
