# udp-server.py

# TFTP Opcodes

import socket
hostIP = '127.0.0.1'
hostPort = 5005
modeserver = ""
firstUsername = ""
firstDestUser = ""
secondusername = ""
secondDestUser = ""

def server():
	ServerMsg='Nice to	meet you :)	!'	
	ServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
	ServerSock.bind((hostip,hostPort))	
	(ClientMsg,(ClientIP,ClientPort))=ServerSock.recvfrom(100)	
	ServerSock.sendto(ServerMsg,(ClientIP,ClientPort))	
	ServerSock.close()

	def register(originName,destName,mode):
		#verificação do user
		if firstusername == "":
			firstusername = originName
			firstDestUser = destName
			
		else:
			secondusername = originName
			secondDestUser = destName

		#verificação do modo
		if mode == modeserver:
			#errormessage
		else:
			modeserver=mode

	 

