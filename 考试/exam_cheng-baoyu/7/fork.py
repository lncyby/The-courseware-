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



print '��ֹ��ʬ���̵ķ�����1.�ӽ��̽���ʱ�򸸽��̷����ź�2.ʹ��os.wait()'
