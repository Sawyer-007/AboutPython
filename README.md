## About Python ##
这里有我一些写过的python脚本，大多和数据库有关。
## 简介 ##
### libget.py ###
一个简易爬虫，可以通过设置post中的学号姓名来知道借书情况。
### OraToMy.py ###
实现异构数据库同步的脚本，用例为Oracle数据库到Mysql数据的信息同步，需要在Oracle数据库需要同步的表添加增删查改触发器，同时建立一张中间表，将增删查改的内容写入到中间表STUDENT_MID，在利用这个py文件进行同步。
### socSerTest.py ###
python socket服务端编程示例
### socCliTest.py ###
python socket客户端编程示例
### insertTest.py  ###
从单个表中取数据成绩前10名</br>

**这个实例是为了完成大数据的分服务器的增删查改，这些小文件是学习python时的测试用的，为了模拟真实数据，我们这里用学习成绩来代替数据，根据不同的班级的存储到不同的服务器上，并且可以通过socket进行统一操作**
### selectTest2.py ###
向不同服务器中添加数据
### selectOrder1.py  ###
直接输出两个表中前10名示例
### selectOrder2.py ###
存储然后输出两个表中前10名示例
### mysqlSocCli.py ###
分服务增删查改的客户端python文件
### mysqlSocSer.py ###
实现对于mysql服务器数据增删查改的分服务器操作，可以通过socket同时向多台服务器添加数据，查询数据，删除数据。