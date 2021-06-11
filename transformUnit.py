import xlwt
import xlrd
import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="test", charset="utf8")
cur = db.cursor()

def e_transform_m(path,tablename) :
    xl = xlrd.open_workbook(path)
    st = xl.sheets()[0]
    rowdata = []
    for i in range(0, st.nrows):
        rowdata.append(st.row_values(i))
    sql = "insert into "+ tablename +" value(%s,%s,%s,%s,%s);"
    for index, value in enumerate(rowdata):
        cur.execute(sql, value)
    db.commit()



def m_transform_e(path,tablename) :
    xl = xlwt.Workbook()
    st = xl.add_sheet("数据库")

    sql = "select * from %s;"
    cur.execute(sql,tablename)
    data = cur.fetchall()
    for index,value in enumerate(data) :
        for i in range(0,len(value)) :
            st.witer(index,i,value[i])
    xl.save(path)





def serverclose():
    cur.close()
    db.close()






