# -*-coding:utf-8 -*-
import mysql.connector
config={
    'host':'172.16.1.49',
    'user':'root',
    'password':'root',
    'port':'3306',
    'database':'hytpdtgpsdb'
}
conn=mysql.connector.connect(**config)
cursor=conn.cursor()
cursor.execute('select * from SDSMsGpsInfo where LDSID = %s', ('5555002',))
values=cursor.fetchall()
print values
