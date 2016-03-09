#/usr/bin/python2.7
#MySQL test1.py to test creat table Class1 and inster datas

import MySQLdb
try:
	conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
	cur = conn.cursor()
	sql = """create table Class1(id int(3) auto_increment not null primary key,
		name char(10) not null,
		score int(3))"""
	cur.execute(sql)
	sql = 'insert into Class1 values(%s,%s,%s)'
	tmp = [(1,'Hqgh',61),(2,'Meay',64),(3,'Nlfd',85),(4,'Firc',71),(5,'Scxg',91),(6,'Bwkf',82),(7,'Qdux',67),(8,'Fnfo',92),(9,'Vsrt',83),(10,'Jpre',84),(11,'Ggxr',87),(12,'Nrvy',79),(13,'Tmwc',96),(14,'Syyc',86),(15,'Pevi',66),(16,'Effm',90),(17,'Nimk',89),(18,'Asvw',60),(19,'Renz',84),(20,'Ycxf',78),(21,'Tlsg',93),(22,'Psfa',70),(23,'Pooe',81),(24,'Xzbc',89),(25,'Ejuv',86),(26,'Vabo',67),(27,'Gpoe',90),(28,'Lfpb',90),(29,'Pljv',77),(30,'Vipy',89)]
	cur.executemany(sql,tmp)
	conn.commit()
	cur.close()
	conn.close()
	conn2 = MySQLdb.connect(host = '222.18.167.27', user = 'root', passwd = '12341234',port = 3306,db = 'Student')
	cur2 = conn2.cursor()
	sql = """create table Class2(id int(3) auto_increment not null primary key,
		name char(10) not null,
		score int(3))"""
	cur2.execute(sql)
	sql = 'insert into Class2 values(%s,%s,%s)'
	tmp = [(31,'Cgsx',63),(32,'Wiam',72),(33,'Awpv',95),(34,'Uqzo',93),(35,'Uerq',73),(36,'Esej',86),(37,'Mgif',81),(38,'Uapu',76),(39,'Gkzd',89),(40,'Kezc',92),(41,'Ymrp',61),(42,'Ailm',77),(43,'Yyoo',88),(44,'Uwuo',98),(45,'Iile',78),(46,'Qkpg',70),(47,'Aqks',67),(48,'Akly',60),(49,'Qint',92),(50,'Serj',74),(51,'Ywcq',79),(52,'Ikpa',90),(53,'Icqc',83),(54,'Oydo',67),(55,'Qsir',98),(56,'Gadu',81),(57,'Yeqc',70),(58,'Skth',70),(59,'Iwbr',71),(60,'Gqtm',67)]
	cur2.executemany(sql,tmp)
	conn2.commit()
	cur2.close()
	conn2.close()

except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
