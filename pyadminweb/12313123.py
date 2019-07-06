import pymysql
config={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'database':'123',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.Cursor,
 }

conn=pymysql.connect(**config)
# 创建游标
cursor=conn.cursor()
# 增加数据
sql='insert into user(user,hsd) values(%s,%s)'
data=[("wawa","d是是")]
cursor.executemany(sql,data)
conn.commit()

cursor.close()
conn.close()

