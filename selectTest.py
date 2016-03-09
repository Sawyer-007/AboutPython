#/usr/bin/python2.7
#mysql test select data that from two table

import MySQLdb
try:
    conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
    cur = conn.cursor()
    cur.execute("select * from Class1 order by score DESC")
    for i in range(10):
	data = cur.fetchone()
    	print data
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
