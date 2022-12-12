#===================================IMPORTING REQUIRED MODULES FOR PROGRAM============================================================#

import mysql.connector as c
from tabulate import tabulate

#============================================ESTABLISHING CONNECTION WITH MYSQL=======================================================#

s=c.connect(host="localhost",user="root",password="Swati*2003",database="timetable")
if s.is_connected():
    print("finally")
p=s.cursor()

#======================================DEFINING FUNCTIOND OF PURPOSE==================================================================#

def fulltable(k):
    command="select * from %s" %(k,)
    p.execute(command)    
    data=p.fetchall()
    d=tabulate(data,headers=['_SRNO_ ','_DAY_','_I_ ','_II_','_III_','_IV_','_V_','_VI_','_VII_','_VIII_'],tablefmt="psql")
    return d
def daywise(sub,day):
    print(sub,day)
    c="select * from %s where day='%s'"%(sub,day)
    p.execute(c)
    d=p.fetchall()
    tbl=tabulate(d,headers=['_SRNO_ ','_DAY_','_I_ ','_II_','_III_','_IV_','_V_','_VI_','_VII_','_VIII_'],tablefmt="psql")
    return tbl
def update(sub,pe,c,d):
    com="update %s set %s='%s' where day='%s'"%(sub,pe,c,d)
    p.execute(com)
    s.commit()
def particular(sub,d1,period):
    c=f"select %s from %s  where day='%s'"%(period,sub,d1)
    p.execute(c)
    d=p.fetchall()
    tbl=tabulate(d,headers=['Your schedule'],tablefmt="psql")
    return tbl
def delete(sub,day):
    c="delete from %s where day='%s'"%(sub,day)
    p.execute(c)
    s.commit()
def insert(sub,sr,d,i,ii,iii,iv,v,vi,vii,viii):
    c=f"insert into {sub} values({sr},'{d}','{i}','{ii}','{iii}','{iv}','{v}','{vi}','{vii}','{viii}')"
    p.execute(c)
    s.commit()
