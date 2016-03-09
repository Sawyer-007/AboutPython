#/usr/bin/python2.7
#mysql test select data that from two table

import MySQLdb
try:
    conn1 = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
    conn2 = MySQLdb.connect(host = 'xxx.xxx.xxx.xx', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cur1.execute("select * from Class1 order by score DESC")
    cur2.execute("select * from Class2 order by score DESC")
    data1 = cur1.fetchone()
    data2 = cur2.fetchone()
    for i in range(10):
        if data1[2] >= data2[2]:
            print data1
	    data1 = cur1.fetchone()
	else:
	    print data2
	    data2 = cur2.fetchone()
    cur1.close()
    cur2.close()
    conn1.close()
    conn2.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
