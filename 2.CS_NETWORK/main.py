from socket import *
import _thread
import time

serverName = '127.0.0.1'
serverPort = 12000


def test(index):
    print("index: " + str(index))
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = 'i am sentence: ' + str(index)
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(2048)
    print('From Server:' + modifiedSentence.decode())
    clientSocket.close()


def main():
    for i in range(0, 20):
        _thread.start_new_thread(test, (i,))


if __name__ == '__main__':
    main()
    time.sleep(1000)
