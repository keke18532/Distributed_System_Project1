import sys
import time
import linecache

s=socket.socket()
host=socket.gethostname()
filename=sys.argv[1]
ID=sys.argv[2]
with open(str(filename), 'r') as f:
    w=f.read().split()
    if str(ID) in w:
        print('True')
        ind = w.index(str(ID))
        port=int(w[ind+1])
    else:
        print('False')

i=0
ID=str(2)
line=linecache.getline('config.txt')
for i in range(0,len(line)):
	if ID==line[i].strip().split(' ')[0]:
		port=line[i].strip().split(' ')[1]



ID=4
with open('config.txt', 'r') as f:
    s=f.read().split()
    if str(ID) in s:
        print('True')
        ind = s.index(str(ID))
        print(s[ind+1])
    else:
        print('False')
