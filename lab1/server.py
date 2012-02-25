#! /usr/bin/python2.7

import socket, os, select

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
ip = "127.0.0.1"
port = 2000
commands=[ "%HastaLaVista", "%Time", "%ShowTime",  "%help", "%WhichMachine", "%Get",  "%Close"]
openSockets = []; #a list of opened sockets

print('bindig to ',ip,':',port)
ss.bind((ip,port));
ss.listen(10); #the queue size of connections

while True:
   rlist, wlist, xlist = select.select( [ss] + openSockets, [], [] )
   for i in rlist:
      if i is ss: 
         #if they are the same object, then we need to create a new one and add it to the openSocket list
         print('Starting the blocking function\n')
         newSocket, address = ss.accept();
         openSockets.append( newSocket );
      else:
            recvMess = i.recv(1024);
            if recvMess == "":
               openSockets.remove(i);
               print('Connection closedr')
            elif recvMess ==  commands[0]: #hasta la vista
               i.close();
               quit();
            elif recvMess == commands[1]: #time
               print('Importing date and time module');
               import datetime;
               time = str(datetime.datetime.now());
               print('sending ', time);
               newSocket.send(time);
            elif recvMess == commands[2]: #showtime
               filename = 'Terminator2.jpg';
               FILE = open(filename, 'rb');
               image = FILE.read();
               newSocket.send(image);
            elif recvMess == commands[3]: #help
               print('sending help');
               help1='%HastaLaVista - close server \n %Time -\
                     get the time \n %Showtime - send a file \n\
                     %help - this help \n %WhichMachine - the os\
                     server is running on \n %Get - get a list of\
                     directories from current one \n %Close - close\
                     the connection'
               newSocket.send(help1);
            elif recvMess == commands[4]: #which machine
               print('importing sys module');
               import sys
               print('finding out what is the platform of server');
               os = sys.platform;
               print('sending the info about os');
               newSocket.send(os);
            elif recvMess == commands[5]: #get the list of file from the current directory
               print('getting folder list');
               folders=os.listdir('.');
               print('sending the folder list');
               for i in list(range(len(folders))):
                  newSocket.send(folders[i]);
                  print('\n');
            elif recvMess == commands[6]: #close
               newSocket.send("Closing connection!");
               newSocket.close();  
            elif (recvMess[len(recvMess)-1] == '?'): # this is the case where we check whether there is a '?' at the end
               newSocket.send('42');
            else:
               print('Can you elaborate on that?');
newSocket.close();
quit()
