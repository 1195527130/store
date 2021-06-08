import xlrd
import pymysql

db = pymysql.connect(host = "localhost",user = "root",password = "123456",database = "test",charset = "utf8")
cur = db.cursor()

xl = xlrd.open_workbook(r'F:\python\12月份衣服销售数据.xlsx')
table = xl.sheets()[0]
rowdata = []
for i in range(1,table.nrows):
    rowdata.append(table.row_values(i))

sql = "insert into cloth value(%s,%s,%s,%s,%s);"
for index,value in enumerate(rowdata) :
    cur.execute(sql,value)
db.commit()
cur.close()
db.close()












