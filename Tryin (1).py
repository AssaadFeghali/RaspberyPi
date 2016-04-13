import bluetooth
import time
import datetime
import csv
import os.path
from firebase import firebase
import RPi.GPIO as GPIO
import math

firebase = firebase.FirebaseApplication('https://pitest.firebaseio.com', None)#Setting up a connection with the firebase server 

path='/home/Assaad/Desktop/bluetooth/Values'#Setting up a path to change the csv file's save location from the /home folder to a personal directory

timing=time.strftime('%Y-%m-%d,%H:%M:%S', time.gmtime())#Setting up the timing to be used when naming the file 
name='Test'+'('+timing+')'
os.path.join(path,name)
data=csv.writer(open(name,'w'), dialect='excel', delimiter=' ', quotechar=' ')#Creating a csv file which will be filled with incoming bleutooth devices present in the server. A row is filled per loop


def blue(device_lookup): #Bluetooth function to find all devices in the vicinity
    if (len(device_lookup)!=0):
        print ('found %d devices') %len(device_lookup)

    if (len(device_lookup)==0):
        print ('no devices available')
        data.writerow('none '+tor)
        
def prog(data,timing): #Function containing the actual identifying of Bluetooth devices in the server 
    print ('IN?') 

    t=1 
    
    print (timing)
    data.writerow(timing)
    
    for t in range (t, 120): #looped 120 times, since each loop takes about 1 minute, results in a two hour loop

        file_time=time.strftime('%D %H:%M:%S', time.gmtime())
        

        device_lookup=bluetooth.discover_devices(lookup_names=True)#Looking up Bluetooth Devices

        blue(device_lookup)
           
        for addr, name in device_lookup:
                ident='%s'%(name)
                address='%s'%(addr)
                
                print (time.strftime('%a, %D %H:%M:%S', time.gmtime()))
                result=bluetooth.lookup_name(address, timeout=5)

                
                if (result != None):#If devices are present, the program will search firebase for their codes
                    
                    server=firebase.get('/ais',None) #Searches a directory we named ais for the Bluetooth devices
                    
                    
                    values=server.values()#Shows all Bluetooth Addresses present on the server
                    print (values)
                    

                    position=str(values).find(str(address))#Searches for any common devices amongst the perceived devices and those on the server
                    print (position)
                    
                    n=position%22 #Position returns an integer which represents the position of the first starting character of the address
                                  #Each address takes up about 22 character spaces
                                  #When looking up the item in the list, its list number must be found, which is its position relative to its character number
                                  #hence it is position divided 22 
                    final_integer=int(math.floor(n))#This would return a decimal, thus we need the closest integer rounded down
                                                    #We take the math.floor value of the decimal n
                    print (final_integer)

                    
                    if (int(position) <0):#This is present to prevent the non-server addresses from interfering with the rest of the 
                        empty=[]
                        empty.append(final_integer)

                    elif (position >= 0):#Finds the perceived devices also present on the server, then writes them to the csv file
                        
                        value_final=values[final_integer]
                        result_final=bluetooth.lookup_name(value_final, timeout=5)
                        data.writerow(result_final+' '+value_final+' '+file_time)

                if (result == None):#writes none if no devices are detected
                    print ('none found at the moment')
                    data.writerow('None Found at the Moment')

        t=t+1
        
        time.sleep(10)


    
    
    

        
GPIO.setmode(GPIO.BCM)#Setting up the GPIO so that the program commences upon being clicked by a button
GPIO.setup(21,GPIO.OUT)#Led to show pi is powered on
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)#Button input. pull_up_down=GPIO.PUD_UP will give a False return when clicked, thus helping the program begin only when considered false
inpt=GPIO.input(17)#Makes button press readable
GPIO.output(21,True)#Turns led on
time.sleep(5)

if (inpt==False):#Starts the program
    print ('On it!')
    GPIO.output(21,False)
    prog(data,timing)
    
GPIO.cleanup()             
 
                                   

       
            
     
              
    

