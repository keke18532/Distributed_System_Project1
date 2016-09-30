import socket
import linecache

s=socket.socket()
host=socket.gethostname()

line=linecache.getlines('config.txt')
for i in range(0,len(line)):
	s.connect(line[i].strip().split(' ')[1])
	msg='yes'
	s.send(bytes(msg, 'utf-8'))

	
