from socket import *
import time

serverIp = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)


for i in range(0, 10):
    message = 'the message:' + str(i)
    start = time.time()
    clientSocket.sendto(message.encode(), (serverIp, serverPort))
    clientSocket.settimeout(2)
    try:
        result = clientSocket.recv(2048)
        print('Result:' + result.decode())
    except Exception:
        print(Exception)
    end = time.time()
    print('time:' + str(end - start) + '\n')