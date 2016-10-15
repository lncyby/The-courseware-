#!/usr/bin/python
from time import sleep
import os,sys
try:
    os.mkfifo('/home/linux/myfifo')
except OSError:
    print 'fifo exist'
filename = sys.argv[1]
thefile = open(filename,'a+')

f = open('/home/linux/myfifo','r')
sleep(1)
while True:
    data = f.readline()
    print data

    thefile.write(data)
    f.flush()
    if not data:
        break
f.close()
      

    
    


    

