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

