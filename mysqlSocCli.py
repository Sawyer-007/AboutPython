#!/usr/bin/python2.7
#socket python mysql test Clinet
#For INSERT and SELECT by Sawyer

if __name__ == '__main__':
    import socket
    while True:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(('222.18.167.49',8001))
        func = raw_input('Welcome to Sawyer mysql\n')
        sock.send(func)
        print sock.recv(1024)
    sock.close()

