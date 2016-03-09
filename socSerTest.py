#/usr/bin/python2.7
#socket test file by sawyer

#judge use xx.py file with import or cmd 
if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the host and port
    sock.bind(('localhost',8001))
#point the max of connect people
    sock.listen(5)
    while True:
	connection,address = sock.accept()
#print the client IP address
	print 'Conncted by',address      
	try:
            connection.settimeout(5)
	    buf = connection.recv(1024)
	    if buf == '1':
               connection.send('welcome to server!')
            else:
               connection.send('please go out!')
        except socket.timeout:
            print 'time out'
        connection.close()
