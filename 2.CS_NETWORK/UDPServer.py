from socket import *

serverPort = 4399
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")
while True:

    message, clientAddress = serverSocket.recvfrom(2048)
    print(message)
    print(clientAddress)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
