""" 
This File is for Mini Project in EED379 :Internet Of Things 
 
Course : Internet Of Things EED379   
Component : Mini Project 
Topic: Home Automation using Google Assistant 
Authors: Ojas Srivastava
        Yatharth Jain
 
Code Component Description : This code is client side for the Raspberry Pi Node. 
                             This program will fetch information from ThingSpeak Cloud and load it on to the  
                             program variables. Upon doing this the program will use the status sent by the cloud to 
                             switch ON or OFF our LED. 
""" 
 
# Importing Important Libraries 
import urllib.request as urllib2  #urllib for oppening any URL and fetching data from there 
import json  #All URLs return information in the form of JSON. This librart will help us decode it from JSON to Python object 
import time   
 
######Libraries specific to Rpi <TO BE FILLED> 
import RPi.GPIO as GPIO                
 
#Defining GLOBAL variables 
READ_API_KEY= #Our READ API key for ThingSpeak Cloud 
CHANNEL_ID= #Our Channel ID for ThingSpeak Cloud 
 
#####GPIO 
GPIO_pin = 6      #Enter as per #Pin connect to LED 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(GPIO_pin,GPIO.OUT) 
 
def switch_on(): 
    GPIO.output(GPIO_pin,GPIO.HIGH) 
    print("LED is ON \n") 
 
def switch_off(): 
    GPIO.output(GPIO_pin,GPIO.LOW) 
    print("LED is OFF \n") 
 
 
#main function is used as the fetcher of data and the command center for the Rpi 
def main(): 
    #print ("http status code=%s" % (conn.getcode()))  #used to get the status code from the server, status code:200 is success
    i=1
    while(True):
        print(i)
        i+=1
        conn = urllib2.urlopen("<Thing Speak Channel URL here>") 
        #opening my ThngSpeak URL which gives data in GET mode. 
 
        response = conn.read() #read the information presented in the URL 
        data=json.loads(response) #the information is in JSON format and hence needs to be unpacked 
 
        #print (data) 
        #The data is in dictionary format and we will access the "feeds" Key 
        temp=data['feeds'] #accessing "feeds" key 
        dic = temp[0] 
        f = dic["field1"] 
        print ("Status is:" + f) #printing the current status 
    
 
        if (f=="2"): 
            switch_on() 
        elif(f=="1"): 
            switch_off() 
        if (f=="3"): #ADD THIS FUNCTIONALITY TO IFTT :Ojas 
            switch_off() 
            break
        #time.sleep(1) #pause for 1 second 
    conn.close() #close connection 
 
if __name__ == '__main__': 
    main()
