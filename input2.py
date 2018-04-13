import urllib2, urllib
import json
import serial
import time
import os

uid = -1
room_number = -1
while True:
     print "Enter username: "
     uname = raw_input()
     print "Enter password"
     pswd = raw_input()

     mycred=[('username',uname), ('password',pswd)]
     mycred=urllib.urlencode(mycred)
     path='http://www.activehousedatabase.xyz/LoginCheck1.php'
     req=urllib2.Request(path, mycred)
     req.add_header("Content-type", "application/x-www-form-urlencoded")
     page=urllib2.urlopen(req).read()
     data = json.loads(page)
     
     if len(data.keys()) == 4:
          uid = data["userid1"]
          print "Log in successful\n"

          myRoom=[('uid',uid)]
          myRoom=urllib.urlencode(myRoom)
          path='http://www.activehousedatabase.xyz/read_data.php'
          req=urllib2.Request(path, myRoom)
          req.add_header("Content-type", "application/x-www-form-urlencoded")
          page=urllib2.urlopen(req).read()
          data = json.loads(page)
          num_of_rooms = len(data['ser_response'])
          
          while True:
               print "Create new room? [y/n]"
               room = raw_input()
               if room is "y":
                    break
               elif room is "n":
                    print "Select the room number: "
                    room_num = raw_input()
                    bool = int(room_num) < int(num_of_rooms) 
                    
                    if (int(room_num) <= int(num_of_rooms) and int(room_num) > 0):
                         print "Entered room number " + str(room_num)
                         room_number = data['ser_response'][int(room_num) - 1]["room_id"]
                         break
                    elif (int(room_num) > int(num_of_rooms)):
                         print "You do not have that room"
                         continue
                    else:
                         print "Invalid Entry"
                         continue
                    
               else:
                    print "Invalid Entry"
          break
          
     else:
          print "Wrong Credentials, Please try again!\n"

rms = 0
power = 0
gas = 0
light = 0
temp = 0.0
humid = 0.0
lqd_q = 0.0
flow = 0.0
lqd_o = 0.0

print "room_number is: " + str(room_number) + "uid " + str(uid)

if(room_number == -1):
     
     mydata=[('rid',room_number), ('rms',rms), ('power',power), ('gas',gas), ('light',light), ('temp',temp), ('humid',humid), ('lqd_q',lqd_q), ('flow',flow), ('lqd_o',lqd_o), ('user_id',str(uid))]
     mydata=urllib.urlencode(mydata)
     path='http://www.activehousedatabase.xyz/write3.php'
     req=urllib2.Request(path, mydata)
     req.add_header("Content-type", "application/x-www-form-urlencoded")
     page=urllib2.urlopen(req).read()
     print page

     mydata=[('uid',str(uid))]
     mydata=urllib.urlencode(mydata)
     path='http://www.activehousedatabase.xyz/lastRoomID.php'
     req=urllib2.Request(path, mydata)
     req.add_header("Content-type", "application/x-www-form-urlencoded")
     page=urllib2.urlopen(req).read()
     print "\n" + page
     data = json.loads(page)
     room_number = data['ser_response'][0]["room_id"]

serial_port = '/dev/ttyUSB0'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
count = 0
while True:
	line = ser.readline()
	line = line.decode("utf-8")
	index=int(line[0:1])
        if(index == 1):
            rms = line[2:]
            print "rms is " + str(rms)
            count += 1
        elif(index == 2):
            power = line[2:]
            print "line is " + str(power)
            count += 1
        elif(index == 3):
            gas = line[2:]
            print "gas is " + str(gas)
            count += 1
        elif(index == 4):
            light = line[2:]
            print "light is " + str(light)
            count += 1
        elif(index == 5):
            temp = line[2:]
            print "temp is " + str(temp)
            count += 1
        elif(index == 6):
            humid = line[2:]
            print "humid is " + str(humid)
            count += 1
        elif(index == 7):
            lqd_q = line[2:]
            print "liquidq is " + str(lqd_q)
            count += 1
        elif(index == 8):
            flow = line[2:]
            print "Flow is " + str(flow)
            count += 1
        elif(index == 9):
            lqd_q = line[2:]
            print "lqd out is " + str(lqd_o)
            count += 1

        if(count == 9):
               print "Saving data to the server"
               
               mydata=[('rid',room_number), ('rms',rms), ('power',power), ('gas',gas), ('light',light), ('temp',temp), ('humid',humid), ('lqd_q',lqd_q), ('flow',flow), ('lqd_o',lqd_o), ('user_id',str(uid))]
               mydata=urllib.urlencode(mydata)
               path='http://www.activehousedatabase.xyz/write3.php'
               req=urllib2.Request(path, mydata)
               req.add_header("Content-type", "application/x-www-form-urlencoded")
               page=urllib2.urlopen(req).read()
               print page
               
               count = 0
               continue
          
	
