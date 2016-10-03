import sys
import time
import linecache
import socket
import random
from _thread import *

filename=sys.argv[1]#get configuration filename from command line
linesNumber=sys.argv[2]#get line number
#ID=sys.argv[2]
host=socket.gethostname()#host
i=0 
j=0
l=0#lamport clock value
nodelist=[]#it stores all the active nodes' ports and its own port
##Read configuration file to find own port
line=linecache.getline(filename,int(linesNumber))
ID=line.split(' ')[0]
port=int(line.split(' ')[1])
nodelist.append(port)
lines=linecache.getlines(filename)

##Send its own id and port to all nodes
for i in range(0,len(lines)):
	s=socket.socket()
	if lines[i].strip().split(' ')[1]!=str(port):
		if(s.connect_ex((host,int(lines[i].strip().split(' ')[1])))==0):
			nodelist.append(lines[i].strip().split(' ')[1])
			info=lines[i].strip().split(' ')[0]+' '+lines[i].strip().split(' ')[1]
			s.send(bytes(info,'utf-8'))
			print('sent')
	s.close()
def clientthread():
	##l=0#the lamport clock value
	def local_event():
		n=random.randrange(1,6)		
		l=l+n
		print('l '+n)
		l=l+1
	def send_message():
		nodeID=0
		global nodelist
		global lines
		s=socket.socket()
		ra=random.randrange(0,length(nodelist))
		nodeport=nodelist[ra]
		for i in range(0,len(lines)):
			temp = lines[i].strip().split(' ')
			if temp[1]==nodeport:
				nodeID=temp[0]
                
		s.connect(host,nodeport)
		msg='message '+ID+' '+l
		#flag
		s.send(bytes(msg,'utf-8'))
		s.close()
		l=l+1
		print('s '+nodeID+' '+l)

		for j in range(0,100):
				i=random.range(0,2)
				if i==0:
						local_event()
				else:
						send_message()
				print('event1')
				time.sleep(0.5)
		time.sleep(2)
		os._exit(0)

def receive_message(msg):
	def messagethread(msg):
		sender=str(msg.split(' ')[1])
		clock=int(msg.split(' ')[2])
		l=l+clock
		printf('r '+sender+' '+clock+' '+l)         
	if msg!=' ':
		start_new_thread(messagethread,(msg,))
	

s=socket.socket()					
s.bind((host,port))
s.listen(100)						
while True:
	buf=''
	conn, addr = s.accept()
	buf=conn.recv(1024)
   
    
	if(buf=='yes'):
		start_new_thread(clientthread)
	if('message' in str(buf)):
	#flag
		receive_message(buf)

