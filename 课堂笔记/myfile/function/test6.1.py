#!/usr/bin/python
   
a=raw_input("Please input your date >",)
l=a.split('-')
y=int(l[0])
m=int(l[1])
d=int(l[2])
sum=0
dcount=[31,28,31,30,31,30,31,31,30,31,30,31]
if y>0 and 0<m<=12 and 0<d<=31:
        if m==2 :
            if (y%4!=0 or(y%100==0 and y%400!=0))and 0<d<=28 :
                print "The date is the %d day"%(d+31)
            elif ((y%4==0 and y%100!=0)or y%400==0) and 0<d<=29:
                print "The date is the %d day"%(d+31) 
            else:
                print "Input Error!"
                
                
        '''if 0<d<=29:
                    print "The date is the %d day"%(d+31)

                else:
                    print "Input Error!"
            else:
                if 0<d<=28:
                    print "The date is the %d day"%(d+31)
                else:
                    print "Input Error!"        '''
        if m!=2 and 0<d<=dcount[d-1]:
           
            if ((y%4==0 and y%100!=0)or y%400==0) :
                dcount[1]+=1
            for i in range(0,m-1):
                sum=dcount[i]+sum
            print "This date is the %d day!"%(sum+d)


            
            
            
        '''    if m in [1,3,5,7,8,10,12]:
                
                    if 0<d<=31:
                        if ((y%4==0 and y%100!=0)or y%400==0):
                            dcount[1]+=1
                        for i in range(0,m-1):
                            sum=dcount[i]+sum
                        print "This date is the %d day!"%(sum+d)
                    else:
                        print "Input Error!"
            elif m in [4,6,9,11]:
                if 0<d<=30:
                        if ((y%4==0 and y%100!=0)or y%400==0):
                            dcount[1]+=1
                        for i in range(0,m-1):
                            sum+=dcount[i]
                        print "This date is the %d day!"%(sum+d)
                else:
                    print "Input Error!"
            else:
                print "Input Error!"

else:
    print "Input Error!"'''

