import pymysql
db = pymysql.connect(host="localhost",user="root",password="123456",database="test")
cur = db.cursor()


def update(sql,param):
    cur.execute(sql,param)
    db.commit()

def select(sql,param,mode="all",size=0) :
    cur.execute(sql,param)

    if mode == "all" :
        return cur.fetchall()
    elif mode == "one" :
        return cur.fetchone()
    elif mode == "many" :
        return cur.fetchmany(size)

def pdbcclose():
    cur.close()
    db.close()