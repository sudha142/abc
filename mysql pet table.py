import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sudha142@python",
    database="pet"
)
cur=con.cursor()
q="insert into pet(name,owner,species,sex,birth,death)values(%s,%s,%s,%s,%s,%s)"
v=[("neel","vas","fake","f",'1998-01-16','2022-01-16'),("neel","vas","fake","f","1998-01-16","1998-01-16"),("neel","vas","fake","f","1998-01-16","1998-01-16"),("nee","vas","fake","f","1998-01-16","1998-01-16"),("nee","vas","fake","f","1998-01-16","1998-01-16")]
cur.executemany(q,v)
con.commit()
cur.close()
con.close()
