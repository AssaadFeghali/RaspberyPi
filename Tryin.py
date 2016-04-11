import bluetooth
import math
import time
import datetime
import csv
import os.path
from firebase import firebase

i=1
firebase = firebase.FirebaseApplication('https://pitest.firebaseio.com', None)




t=1

print ('IN?')
path='/home/Assaad/bluetooth'

tim=time.strftime('%Y-%m-%d,%H:%M:%S', time.gmtime())
print (tim)
name='value'+'('+tim+')'
excel=csv.writer(open(name,'w'), dialect='excel', delimiter=' ', quotechar=' ')
os.path.join(path, name)
excel.writerow(tim)
for t in range (t, 100):

    tor=time.strftime('%D %H:%M:%S', time.gmtime())
    

    me=bluetooth.discover_devices(lookup_names=True)

    if (len(me)!=0):
        print ('found %d devices') %len(me)

    if (len(me)==0):
        print ('no devices available')
        excel.writerow('none '+tor)
       
    for addr, name in me:
            ml='%s'%(name)
            mol='%s'%(addr)
            
            print (time.strftime('%a, %D %H:%M:%S', time.gmtime()))
            result=bluetooth.lookup_name(mol, timeout=5)

            
            if (result != None):
                while (i<3):
                        results = firebase.get('/ais',i)
                        if (mol == results):
                            print (mol+' '+ml+' Present')
                            excel.writerow(result+' '+tor)
                        i=i+1




                


            

                               

    time.sleep(10)
            

       
              
    

