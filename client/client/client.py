import socket

sock = socket.socket()
try:
    sock.connect(('localhost', 9090))
    while True:
        s = input("your word: ")
        if s=='exit':
            sock.close()
            exit
        sock.send(s.encode("utf-8"))
        data = sock.recv(1024)
        print (data)
except:
    print("ну бывает")


