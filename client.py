import sys
import time
import linecache
import socket
import random
from _thread import *

filename=sys.argv[1]#get configuration filename from command line
ID=sys.argv[2]#get ID for node
s=socket.socket()
host=socket.gethostname()
i=0,j=0
nodelist=[]#it stores all the active nodes' ports and its own port

##Read configuration file to find own port
line=linecache.getlines('config.txt')
for i in range(0,len(line)):
	if ID==line[i].strip().split(' ')[0]:
		port=line[i].strip().split(' ')[1]

s.connect((host,port))
s.bind(host,port)
s.listen(100)
nodelist.append(port)
##Send its own id and port to all nodes
for i in range(0,len(line)):
	if line[i].strip().split(' ')[1]!=port:
		if(s.connect_ex((host,line[i].strip().split(' ')[1]))==0):
			nodelist.append(line[i].strip().split(' ')[1]))
			info=line[i].strip().split(' ')[0]+' '+line[i].strip().split(' ')[1]
			s.send(bytes(info,'utf-8'))

def clientthread():
	l=0#the lamport clock value
	def local_event():
		n=random.randrange(1,6)		
		l=l+n
		print('l '+n)
	def send_message():
                ra=random.randrange(0,length(nodelist))
		nodeport=nodelist[ra]
		for i in range(0,len(line)):
			if line[i].strip().split(' ')[1]==nodeport:
				nodeID=line[i].strip().split(' ')[0]
		s.connect(host,nodeport)
		msg=ID+' '+l
		s.send(bytes(msg,'utf-8'))
                print('s '+nodeID+' '+l)
        def receive_message():
                msg=s.recv(1024)
                if msg!=' ':
                        start_new_thread(messagethread,(msg))
                def messagethread(msg):
                        sender=msg.split(' ')[0]
                        clock=int(msg.split(' ')[1])
                        l=l+clock
                        printf('r '+sender+' '+clock+' '+l)

        for j in range(0,100):
                i=random.range(0,2)
                if i==0:
                        local_event()
                else:
                        send_message()
        exit()



while True:
    try:
        conn, addr = s.accept()
    except:
        print ('Exception :\'(')
        continue
    buf=s.recv(1024)
    if(buf=='yes'):
	start_new_thread(clientthread)
