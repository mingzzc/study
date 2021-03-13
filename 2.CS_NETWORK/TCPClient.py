from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
# connect first
clientSocket.connect((serverName, serverPort))
sentence = input('Input the lowercase sentence')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print('From Server:' + modifiedSentence.decode())
clientSocket.close()
