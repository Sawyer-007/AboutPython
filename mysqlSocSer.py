#/usr/bin/python2.7
#socket python mysql test Server
#By Sawyer

if __name__ == '__main__':
    import socket
    import MySQLdb
    import math
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('222.18.167.49',8001))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        print 'Connection by',address,'\n'
        try:
            connection.settimeout(60)
            buf = connection.recv(1024)
            if buf.find('select') == 0:
                try:
                    selLimit = 0
                    selY = len(buf)-(buf.find('limit')+6)   #for get the lenth of number that after limit
                    for i in range(selY):
                        selLimit = selLimit + int(buf[buf.find('limit')+6+i])*pow(10,selY-1-i)  #To get the value of the limit
                    conn1 = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
                    conn2 = MySQLdb.connect(host = '222.18.167.27', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
                    cur1 = conn1.cursor()
                    cur2 = conn2.cursor()
                    cur1.execute(buf)
                    cur2.execute(buf)
                    data1 = cur1.fetchone()
                    data2 = cur2.fetchone()
                    orResult = ''
                    for i in range(selLimit):
                        if data1[2] >= data2[2]:
                            orResult = orResult + str(data1) + '\n'
                            data1 = cur1.fetchone()
                        else:
	                     orResult = orResult + str(data2) + '\n'
	                     data2 = cur2.fetchone()
                    cur1.close()
                    cur2.close()
                    conn1.close()
                    conn2.close()
                    connection.send(orResult)
                except MySQLdb.Error,e:
                    errInfo = "Mysql Error %d: %s" % (e.args[0], e.args[1])
                    connection.send(orResult)
            elif buf.find('insert') == 0:
                try:
                    inClass = int(buf[buf.find(')')-1]) #To get the class and decide what table should into
                    if(inClass % 2 == 1):
                        conn1 = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
                        cur1 = conn1.cursor()
                        cur1.execute(buf)
                        conn1.commit()
                        cur1.close()
                        conn1.close()
                        connection.send('Success insert data1 into Data1\n')
                    else:
                        conn2 = MySQLdb.connect(host = '222.18.167.27', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
                        cur2 = conn2.cursor()
                        cur2.execute(buf)
                        conn2.commit()
                        cur2.close()
                        connection.send('Success insert data into Data2\n')
                except MySQLdb.Error,e:
                    errInfo = "Mysql Error %d: %s" % (e.args[0], e.args[1])
                    connection.send(orResult)
            elif buf.find('delete') == 0 or buf.find('update') == 0:
                try:
                    conn1 = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
                    conn2 = MySQLdb.connect(host = '222.18.167.27', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
                    cur1 = conn1.cursor()
                    cur2 = conn2.cursor()
                    cur1.execute(buf)
                    cur2.execute(buf)
                    conn1.commit()
                    conn2.commit()
                    cur1.close()
                    cur2.close()
                    conn1.close()  
                    conn2.close()
                    connection.send('Ok accept!\n')
                except MySQLdb.Error,e:
                    errInfo = "Mysql Error %d: %s" % (e.args[0], e.args[1])
                    connection.send(orResult)
            elif buf == 'exit':
                connection.send('Bye Bye')
                connection.close()
            else:
                connection.send('Shen me GUI!!!')
        except socket.timeout:
            print 'time out'
            connection.close()

