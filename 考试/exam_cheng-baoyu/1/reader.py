#!/usr/bin/python
from time import sleep
import os,sys
filename = sys.argv[1]
thefile = open(filename,'r')

try:
    os.mkfifo('/home/linux/myfifo')
except OSError:
    print 'fifo exit'

f = open('/home/linux/myfifo','w')
sleep(1)
data = thefile.readlines()
for mess in data: 
    f.write(mess)
    print mess
    f.flush()


