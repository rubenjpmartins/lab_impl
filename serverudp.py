# Servidor

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
print("ICHAT SERVER")
print
data={}

hostIP = ''  #aceita qualquer ip
hostPort = 5005
flag =0

#Inicio de Variaveis  
writerUsername  = ""
reciverDestUser = ""

#Inicio do Socket

ServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
ServerSock.bind	((hostIP,hostPort))	




while True:

	print "estou a espera de mensagem"

	(ClientMsg,(ClientIP,ClientPort))= ServerSock.recvfrom(1024) 

	print "recebi uma mensagem"

	divideMsg=ClientMsg.split(' ')

	print "ClientMsg: "+ ClientMsg
	
	#Registo
	if divideMsg[0]=="1":
		print divideMsg
		
		if divideMsg[1]=="W":
			# faz o registo do escritor, exemplo:
			# {'escritor': ['leitor', '127.0.0.1', 53773]}
			data[divideMsg[2]]=[divideMsg[3],ClientIP,ClientPort]
			
			# Para saber se ja existe um user com o mesmo modo
			if writerUsername == "":
				#nome do escritor
				writerUsername=divideMsg[2]
				#Servidor envia a mensagem - Registo ok
				ServerSock.sendto("sender",(data[writerUsername][1], data[writerUsername][2]))
			
			else:
				reciverDestUser=divideMsg[2]
				#Servidor envia a mensagem com o modo contrario pois ja existe um sender
				ServerSock.sendto("reciver",(data[reciverDestUser][1], data[reciverDestUser][2]))

			print data

			


		if divideMsg[1]=="R":
			# faz o registo do leitor, exemplo:
			# {'leitor': ['escritor', '127.0.0.1', 53773]}
			data[divideMsg[2]]=[divideMsg[3],ClientIP,ClientPort]

			# Para saber se ja existe um user com o mesmo modo
			if reciverDestUser == "":
				#nome do leitor
				reciverDestUser=divideMsg[2]
				#Servidor envia a mensagem - Registo ok
				ServerSock.sendto("reciver",(data[reciverDestUser][1], data[reciverDestUser][2]))
			
			else:
				writerUsername=divideMsg[2]
				#Servidor envia a mensagem com o modo contrario pois ja existe um reciver
				ServerSock.sendto("sender",(data[writerUsername][1], data[writerUsername][2]))
				
			print data


	# Envio de mensagens		
	if divideMsg[0]=="3":
		print "divideMsg: " 
		print divideMsg
		
		# Se o outro user n tiver registado
		if reciverDestUser == "":
			# opcode 4 - Reconhecimento de mensagem enviada (MSG ACK); 
			print "6 Reconhecimento de mensagem nao enviada (ERRO)"
			ServerSock.sendto("6 Reconhecimento de mensagem nao enviada (ERRO)",(data[writerUsername][1], data[writerUsername][2]))	


		#Terminacao da Ligacao (FIM)
		elif divideMsg[1]=="FIM":
			if flag==0:
				ClientMsg = "8 - o utilizador saiu"
				#envio de mesagem para o outro user a avisar da saida do utilizador
				ServerSock.sendto(ClientMsg,(data[reciverDestUser][1], data[reciverDestUser][2]))
				#envio de mesagem para o user com o opcode 7
				ServerSock.sendto("7 - ADEUS",(data[writerUsername][1], data[writerUsername][2]))
				print "7 - Cliente Desligou"
				flag = 1
			else:
				ServerSock.sendto("7 - ADEUS",(ClientIP,ClientPort))
				print "7 - Cliente Desligou"
		
		#tudo ok
		else:
			# opcode 3 - envio de mensagem para o outro user	
			print "3 Mensagem"		
			ServerSock.sendto(ClientMsg,(data[reciverDestUser][1], data[reciverDestUser][2]))
			# opcode 4 - Reconhecimento de mensagem enviada (MSG ACK); 
			print "4 MSG ACK"
			ServerSock.sendto("4 ENVIO DE MENSAGEM - MSG ACK",(data[writerUsername][1], data[writerUsername][2]))
			
			# opcode 5 - Recebe confirmacao do user
			(ClientMsg,(data[reciverDestUser][1],data[reciverDestUser][2]))= ServerSock.recvfrom(1024)

			print ClientMsg

			# faz a troca apos envio de mensagens
			username1 = data[writerUsername][1] 
			username2 = data[writerUsername][2] 
			data[writerUsername][1] = data[reciverDestUser][1]
			data[writerUsername][2] = data[reciverDestUser][2]
			data[reciverDestUser][1] = username1
			data[reciverDestUser][2] = username2



ServerSock.close()






