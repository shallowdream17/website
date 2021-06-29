import pymysql

db=pymysql.connect(
    host='webmysql.rwlb.rds.aliyuncs.com',
    user='qianmeng',
    passwd='ShallowDream17',
    port=3306,
    db='web',
)

cursor=db.cursor()
sql="select * from test"
cursor.execute(sql)

data=cursor.fetchall()
print(data)


