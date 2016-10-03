import sys
import time
import linecache
import socket
import random
from _thread import *

filename=sys.argv[1]#get configuration filename from command line
ID=sys.argv[2]#get ID for node
#print(filename,ID)
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
	clock=0
	def local_event():
		r=randrange(1,6)		
	def send_message():
		ra=randrange(0,length(nodelist))
		nodeport=nodelist[ra]
		for i in range(0,len(line)):
			if line[i].strip().split(' ')[1]==nodeport:
				nodeID=line[i].strip().split(' ')[0]
		s.connect(host,nodeport)
		msg=ID+' '+l
		s.send(bytes(info,'utf-8'))








while True:
    try:
        conn, addr = s.accept()
    except:
        print ('Exception :\'(')
        continue
    buf=s.recv(1024)
    if(buf=='yes'):
	start_new_thread(clientthread)

