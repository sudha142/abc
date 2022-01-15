import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sudha142@python",
    database="New"
)
cur=con.cursor()
q="insert into student(id,name,class,section)values(%s,%s,%s,%s)"
v=[(1,"sudha",9,"A"),(2,"karan",10,"B"),(3,"tulasi",8,"A")]
cur.executemany(q,v)
con.commit()
cur.close()
con.close()