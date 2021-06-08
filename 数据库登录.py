import pymysql

db = pymysql.connect(host = "localhost",user = "root",password = "123456",database = "test",charset = "utf8")
cur = db.cursor()

sql = "select * from login_user;"
cur.execute(sql)
# db.commit()
data = cur.fetchall()
flag = False
name = input("请输入用户名: ")
password = input("请输入密码: ")
for index,value in enumerate(data) :
    if name == value[0] and password == value[1] :
        print("登录成功！您的信息为：",value)
        flag = True
if 1 - flag :
    print("登录失败！")
cur.close()
db.close()