#!/usr/bin/python
import os,sys
putfile = sys.argv[1]
newfilename = sys.argv[2]
fr = open(putfile,'r')
a = fr.read()
fw = open(newfilename,'a+')
fw.write(a)
print "copy OK"
fr.close()
fw.close()



