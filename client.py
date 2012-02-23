#! /usr/bin/python2.7
import socket

ip = "127.0.0.1"
port = 2000

commands=[ '%HastaLaVista', '%Time', '%ShowTime',  '%help', '%WhichMachine', '%Get',  '%Close']

ss = socket.socket( socket.AF_INET, socket.SOCK_STREAM );

ss.connect((ip,port));
while True:
   mesg = raw_input('>>')
   if mesg == commands[2]:
      image = file('asdf.jpg', 'wb');
      data = ss.recv(30000);
      image.write(data);
   else:
      ss.send(mesg);
      data = ss.recv(1024);
      print(data)

