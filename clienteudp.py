# Cliente

# PTSM Opcodes
#
# 1    Pedido de registo (PR);
# 2    Reconhecimento do registo (ACK);
# 3    Mensagem (DATA);
# 4    Reconhecimento de mensagem enviada (MSG ACK); 
# 5    Reconhecimento de mensagem recebida no destinatario
# 6    Reconhecimento de mensagem nao enviada (ERRO); 
# 7    Terminacao da ligacao (FIM);
# 8    Indicacao ao outro user da saida de um deles


import socket
print "ICHAT CLIENTE"
print
print "Modo?"


Input="1 "+raw_input()

print "Quem es?"
Input = Input + " "+raw_input()

print "Para quem?"
Input=	Input +" "+raw_input()

flag=0


#Inicio do Socket

ClientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Envia o registo do user para o servidor
ClientSock.sendto(Input,('localhost',	5005))
print	"Menssagem para o servidor: " +	Input

# Recebe mensagem do servidor
(ServerMsg,	(ServerIP,	ServerPort))	=	ClientSock.recvfrom (1024)  
print	"Menssagem do servidor: 2 Estas registado!  "
print "modo - "+ ServerMsg

#modo (receiver/sender)
modo=ServerMsg


# Ciclo apos resgisto
while True:
	# se for o escritor 
	if modo=="sender":
		msg = raw_input("> ")
		
		#Opcode 3 - Mensagem
		msgtoserver="3"+" "+ msg
		
		if flag==1:
			print "Vou sair tambem"
			msg = "FIM"
			msgtoserver="3"+" "+ msg
			ClientSock.sendto(msgtoserver,('localhost',	5005))
			print	("Menssagem para o servidor: " +	msg)
			(ServerMsg,	(ServerIP,	ServerPort))	=	ClientSock.recvfrom (1024)	
			print	("Message from server: " +	ServerMsg)
			print "Adeus"
			ClientSock.close ()
			break	


		#Se o sender quiser sair
		if msg == "FIM":
			ClientSock.sendto(msgtoserver,('localhost',	5005))
			print	("Menssagem para o servidor: " +	msg)
			(ServerMsg,	(ServerIP,	ServerPort))	=	ClientSock.recvfrom (1024)	
			print	("Message from server: " +	ServerMsg)
			print "Adeus"
			ClientSock.close ()
			break	
		
		# Envia input para o servidor	
		print "vou tentar enviar"
		ClientSock.sendto(msgtoserver,('localhost',	5005))
		print	("Message to server: " + msgtoserver)

		(ServerMsg,	(ServerIP,	ServerPort))	=	ClientSock.recvfrom (1024)	
		print	("Message from server: " +	ServerMsg)

		#Se o outro user n tiver registado
		if ServerMsg!="6 Reconhecimento de mensagem nao enviada (ERRO)":	
			modo="reciver"
			print "modo - "+ modo

	# se for o leitor	
	if modo =="reciver":
		(ServerMsg,	(ServerIP,	ServerPort))	=	ClientSock.recvfrom (1024)	
		print	("Message from server: " +	ServerMsg)

		if ServerMsg=="8 - o utilizador saiu":
			flag = 1

		msgtoserver="5 USER ACK"
		ClientSock.sendto(msgtoserver,('localhost',	5005))
		
		modo="sender"
		print "modo - "+ modo










