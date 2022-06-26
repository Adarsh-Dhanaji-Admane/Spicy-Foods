import pymysql as p 

def getconnection():
    return p.connect(host="localhost",user="root",password="",database="spicyfood")

def adddata(t):
    con = getconnection()
    
    query = "insert into Registration(FNAME,LNAME,EMAIL,PHONE,ZIP,CITY,STATE,ADDRSS,USERNAME,PASS) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cur=con.cursor()
    cur.execute(query,t)
    con.commit()
    con.close()


def show_data():
    con = getconnection()
    cur = con.cursor()
    query = "select * from Registration;"
    cur.execute(query)
    detaillist = cur.fetchall()
    con.commit()
    con.close()
    return detaillist
    