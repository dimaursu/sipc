#! /usr/bin/python

import socket
import os

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ip = "127.0.0.1"
port = 2000
commands=[ '%HastaLaVista', '%Time', '%ShowTime',  '%help', '%WhichMachine', '%Get',  '%Close']


print('bindig to ',ip,':',port)
ss.bind((ip,port));
ss.listen(10); #the queue size of connections

cs = ss.accept();
#def interpret(cs, commands)
rec = 'god knows what'
while not( rec ==  commands[0]):
      rec=cs[0].recv(20);
      print('received info:',rec);
      if rec == commands[1]: #time
         print(rec);
         import datetime;
         time = str(datetime.datetime.now());
         cs[0].send(time);
      elif rec == commands[2]: #showtime
         filename = 'Terminator2.jpg';
         FILE = open(filename, 'r');
         cs[0].send(FILE);
      elif rec == commands[3]: #start chat
         while not ( responds == '!$!'):
               responds = cs[0].recv(1024);
               print('client:', responds,'\n');
               date = input('enter>');
               cs[0].send(data);
      elif rec == commands[4]: #which machine
         import sys
         os = sys.platform;
         cs[0].send(os);
      elif rec == commands[5]: #get the list of file from the current directory
         folders=os.listdir('.');
         cs[0].send(folders);
      elif rec == commands[6]: #close
         cs[0].send("Closing connection!");
         cs[0].close();  
      elif (rec[len(rec)-1] == '?'): # this is the case where we check whether there is a '?' at the end
         cs[0].send('42');
      else:
         print('Can you elaborate on that?');

cs[0].close();

quit()
