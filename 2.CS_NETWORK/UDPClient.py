from socket import *

serverName = '127.0.0.1'
serverPort = 4399

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence.')
# Udp need to assign the (ip,port) while receiving doesn't need.
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
print(serverAddress)
clientSocket.close()
