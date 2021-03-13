from socket import *

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', 80))
tcpSerSock.listen(1)
while True:
    # Strat receiving data from the client
    print("Ready to receive")
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(2048).decode()
    print('Message:' + message)
    print('File name:' + message.split()[1])
    filename = message.split()[1].partition("/")[2]
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        for data in outputdata:
            tcpCliSock.send(data.encode())
        f.close()
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        print('This web had not cache')
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            print('filename:' + filename)
            host = filename.replace("www.", "", 1)

            print('host:' + host)
            try:
                c.connect((host, 80))
                print('connected')
                request = message.replace("127.0.0.1", host)
                request = request.replace(filename, '/')
                print("Request:" + request)
                c.send(request.encode())
                result = c.recv(2048)
                print('Result:', result)
                tcpCliSock.send(result)
                tempFile = open("./"+filename, 'wb')
                tempFile.write(result)
                tempFile.close()
                print('Write to file')
            except:
                print("Illegal request")
        else:
            tcpCliSock.send("HTTP/1.0 404 PageNotFound\r\n".encode())
    # Close the client and the server sockets
    tcpCliSock.close()