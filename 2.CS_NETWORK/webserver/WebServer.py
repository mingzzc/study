#import socket module
from socket import *


port = 80

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', port))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(4096)
        print("request:\n" + message.decode())
        filename = message.split()[1]
        f = open(filename[1:], 'rb')
        outputdata = f.readlines()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\n' \
                     'Date: Sun, 28 Feb 2021 12:39:08 GMT\n' \
                     'Content-Type: text/html; charset=utf-8\n\n'.encode())
        #there must be add one line \n\n

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found'.encode())
        #Close client socket
        connectionSocket.close()

serverSocket.close()