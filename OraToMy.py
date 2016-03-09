#/usr/bin/python2.7
#By Sawyer

if __name__ == '__main__':
    import cx_Oracle
    import MySQLdb
    import time

    try:
        mysqlCon = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123456',port = 3306,db = 'test')
        oracleCon = cx_Oracle.connect('syz','1234','10.254.247.69:1521/ORCL')
        mysqlCur = mysqlCon.cursor()
        oracleCur = oracleCon.cursor()

        startTime = time.time()
        oracleCur.execute('select * from STUDENT_MID')  #get the mid table data
        rowResult = oracleCur.fetchall()                  #get all table
        countOfMid = oracleCur.rowcount                 #get the number of mid table
        print "Current count is",countOfMid

        
        for row in rowResult:
            if row[4] == 1:
                sql = "insert into student values("+str(dataArray[0])+",'"+str(dataArray[1])+"',"+str(dataArray[2])+","+str(dataArray[3])+")"
                mysqlCur.execute(sql)
            if row[4] == 2:
                sql = "delete from student where id = "+str(dataArray[0])   #use primekey delete only row
                mysqlCur.execute(sql)
            if row[4] == 3:
                sql = "delete from student where id = "+str(dataArray[0])
                mysqlCur.execute(sql)
            if row[4] == 4:
                sql = "insert into student values("+str(dataArray[0])+",'"+str(dataArray[1])+"',"+str(dataArray[2])+","+str(dataArray[3])+")"
                mysqlCur.execute(sql)
            delSQL = "delete from STUDENT_MID where rownum <= 1"
            oracleCur.execute(delSQL)
            mysqlCon.commit()
            oracleCon.commit()
        mysqlCur.close()
        mysqlCon.close()
        oracleCur.close()
        oracleCon.close()

        print "Accept! Running :",time.time()-startTime,"s"
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])