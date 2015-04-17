#udp-client.py

import socket

ClientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
WriteRequest = '\x00'+'\x02' + 'abcd.txt'+'\x00'+'netascii'+'\x00'
TFTP.sendto(WriteRequest,('192.168.56.101.'))
ClientMsg = "O Toni é o máior"
ClientSock.sendto(ClientMsg,('192.168.56.101',5005))
print "Message to erver: ", ClientMsg
(ServerMsg(ServerIP, ServerPort)) = ClientSock.recvfrom(100)
print "Message from server: ", ServerMsg
ClientSock.close()

#correcta

import socket
ClientSock=socket.socket(socket.AF_INET,	socket.SOCK_DGRAM)	
ClientSock.sendto(Registery,	('localhost',	7006))
print	("Message	to	server:	",	Registery)
(ServerMsg,	(ServerIP,	ServerPort))	=	ClientSock.recvfrom (1024)	
print	("Message from server: ",	ServerMsg)
ClientSock.close ()

print("REGESTERY")
print("From?")
Input = raw_input()	#get the input from the user
Registery =Input #create the registery msg
print("To?")
Input = raw_input()	#get the input from the user
Registery = Registery +" "+Input #create the registery msg
Input=""
while  1: #need to put a right mode 
	print("Mode W/R?")
	Input = raw_input().upper()	#get the input from the user
	print(Input)
	if Input=="R":break
	if Input=="W":break
Registery = "R "+ Input+" " + Registery #create the registery msg
