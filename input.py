import urllib2, urllib
import json
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

filepath = 'output.txt'  
with open(filepath) as fp:  
   line = fp.readline()
   rms = line
   count = 0
   while line:
        if(count == 0):
            power = fp.readline()
        elif(count == 1):
            gas = fp.readline()
        elif(count == 2):
            light = fp.readline()
        elif(count == 3):
            temp = fp.readline()
        elif(count == 4):
            humid = fp.readline()
        elif(count == 5):
            lqd_q = fp.readline()
        elif(count == 6):
            flow = fp.readline()
        elif(count == 7):
            lqd_o = fp.readline()
        else: break

        count += 1

rms = rms[13:-6]
power = power[16:-3]
gas = gas[11:-1]
light = light[13:-5]
temp = temp[6:-4]
humid = humid[10:-3]
lqd_q = lqd_q[7:-7]
flow = flow[24:-8]
lqd_o = lqd_o[24:-2] 

mydata=[('rid',room_number), ('rms',rms), ('power',power), ('gas',gas), ('light',light), ('temp',temp), ('humid',humid), ('lqd_q',lqd_q), ('flow',flow), ('lqd_o',lqd_o), ('user_id',str(uid))]
mydata=urllib.urlencode(mydata)
path='http://www.activehousedatabase.xyz/write3.php'
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
print page
