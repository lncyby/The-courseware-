#!/usr/bin/python
#coding=utf-8
import os
from time import sleep
from signal import *

pid = os.fork()

if pid < 0:
    print "create process failed"
elif pid == 0:
    print "This is child process:",os.getpid()
else:
    signal(SIGCHLD,SIG_IGN)
    sleep(0.1)
    print("parent process:",os.getpid())
    while True:
        pass

print "++++++++++++++++++++++++"



print '防止僵尸进程的方法：1.子进程结束时向父进程发送信号2.使用os.wait()'
