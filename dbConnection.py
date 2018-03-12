import MySQLdb
connection = MySQLdb.connect(host="localhost",user="root",passwd="",db="cosmetics")
connection.select_db("cosmetics")
cursor = connection.cursor()
