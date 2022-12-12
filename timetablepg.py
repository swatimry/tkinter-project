#===========================importing required modules=============================================================================#
from tkinter import *
import timetech as s
from PIL import ImageTk,Image
#==========================making front end for program i.e homepage designing=====================================================#

root=Tk()
root.title('TIMETABLE VIEWER')
root.geometry('900x300')
root.resizable(0,0)


canvas=Canvas(root,width=1200,height=300)
img=ImageTk.PhotoImage(Image.open('mainbg.jpg'))
canvas.create_image(0,0,anchor=NW,image=img)
canvas.pack()

l1=Label(root,text='WELCOME! THIS IS A TIMETABLE VIEWER',cursor="hand2",fg='aqua',bg='black')
l1.place(x=80,y=20)
l2=Label(root,text="Click on the buttons below to perform desired operations!!!",cursor='hand2',fg='#0ee6c2',bg='black')
l2.place(x=78,y=55)
l1.config(font=('Courier',25,"bold","italic",))
l2.config(font=('Courier',15,'bold'))

#=================================adding elements(interior pages) to mainwindow====================================================#

def forfulltable():
    nw1=Toplevel(root)
    from PIL import ImageTk,Image
    import timetech as s
    canvas=Canvas(nw1,width=1000,height=500)
    img=ImageTk.PhotoImage(Image.open('fulltable.jpg'))
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack()
    def full():
        s.fulltable(var.get())
        table=Label(nw1,text=s.fulltable(var.get()),bg='#9ff5b5',font=('Courier',10,"bold"))
        table.place(x=35,y=220)

    nw1.title("TIMETABLE")
    nw1.resizable(0,0)
    l2=Label(nw1,text="Select subject to see full timetable",fg="#11014a",bg="#52d8fa")
    l2.place(x=120,y=25)
    var=StringVar()
    var.set("maths")
    radio=Radiobutton(nw1,text="Maths",padx=14,variable=var,value="maths",font=('Courier',15,"bold","italic"),bg="#52d8fa",\
    fg="#11014a").place(x=125,y=75)
    radio=Radiobutton(nw1,text="Chemistry",padx=14,variable=var,value="chemistry",font=('Courier',15,"bold","italic"),bg="#52d8fa",\
    fg="#11014a").place(x=240,y=75)
    radio=Radiobutton(nw1,text="Hindi",padx=14,variable=var,value="hindi",font=('Courier',15,"bold","italic"),bg="#52d8fa",\
    fg="#11014a").place(x=405,y=75)
    radio=Radiobutton(nw1,text="Cs",padx=14,variable=var,value="cs",font=('Courier',15,"bold","italic"),bg="#52d8fa",
    fg="#11014a").place(x=45,y=75)
    radio=Radiobutton(nw1,text="Physics",padx=14,variable=var,value="physics",font=('Courier',15,"bold","italic"),bg="#52d8fa",   
    fg="#11014a").place(x=520,y=75)
    radio=Radiobutton(nw1,text="English",padx=14,variable=var,value="english",font=('Courier',15,"bold","italic"),bg="#52d8fa",
    fg="#11014a").place(x=650,y=75)
    
    Button(nw1,text="PROCEED",command=full,font=('Courier',15,"bold","italic"),bg="#52d8fa",fg="#11014a").place(x=360,y=125)
 
    label1=Label(nw1,text="Your timetable",bg="#52d8fa",font=('Courier',15,"bold","italic"),fg="#11014a")
    label1.place(x=325,y=175)
    nw1.title('FULL WEEK TIMETABLE')
    nw1.geometry('850x400')
    l2.config(font=('Courier',20,"bold","italic",))
    nw1.mainloop()

def forparticularday():
    nw2=Toplevel(root)
    import timetech as s
    from PIL import ImageTk,Image
    subjects=["MATHS","HINDI","CHEMISTRY","CS","ENGLISH","PHYSICS"]
    
    days=["Mon","Tue",'Wed','Thu','Fri','Sat']
    period=["I",'II','III','IV','V','VI','VII','VIII']
    nw2.resizable(0,0)
    
    canvas=Canvas(nw2,width=1000,height=500)
    img=ImageTk.PhotoImage(Image.open('abcd.jpg'))
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack()
    
    def part():
        s.particular(variable.get(),variable2.get(),variable3.get())
        label1.configure(text=s.particular(variable.get(),variable2.get(),variable3.get()),bg='#7ab1e6')
    
    variable=StringVar(nw2)
    variable2=StringVar(nw2)
    variable3=StringVar(nw2)
    variable.set(subjects[0])
    variable2.set(days[0])
    variable3.set(period[0])
    heading=Label(nw2,text='Select subject,period,and day to proceed',bg='#e8e8e8',fg='#140c54')
    heading.place(x=30,y=50)
    sub=OptionMenu(nw2,variable,*subjects)
    sub.config(bg='#e8e8e8',fg='#140c54',font=('Courier',13,"bold"))
    sub.place(x=200,y=138)
    subh=Label(nw2,text='SUBJECT',font=('Courier',13,"bold"),bg='#e8e8e8',fg='#140c54')
    subh.place(x=200,y=105)
    dy=OptionMenu(nw2,variable2,*days)
    dy.place(x=320,y=138)
    dyh=Label(nw2,text='DAY',font=('Courier',13,"bold"),bg='#e8e8e8',fg='#140c54')
    dyh.place(x=320,y=105)
    dy.config(bg='#e8e8e8',fg='#140c54',font=('Courier',13,"bold"))
    per=OptionMenu(nw2,variable3,*period)
    per.place(x=450,y=138)
    perh=Label(nw2,text='PERIOD',font=('Courier',13,"bold"),bg='#e8e8e8',fg='#140c54')
    perh.place(x=450,y=105)
    per.config(bg='#e8e8e8',fg='#140c54',font=('Courier',13,"bold"))
    fortable=Frame(nw2,bg="blue")
    fortable.place(x=250,y=200)
    label1=Label(fortable,text="Here will be table",bg='#e8e8e8',fg='#140c54',font=('Courier',15,"bold"))
    label1.pack()
    nw2.title('PARTICULAR PERIOD')
    nw2.geometry('700x400')
    heading.config(font=('Courier',20,"bold","italic"))
    Button(nw2,text="PROCEED",command=part,font=('Courier',13,"bold"),bg='#e8e8e8',fg='#140c54',height='2',width='20',cursor="hand2"\
    ,borderwidth=5,relief='raised').place(x=260,y=335)
    nw2.mainloop()


def fordaywise():
    nw3=Toplevel(root)
    subjects=["MATHS","HINDI","CHEMISTRY","CS","ENGLISH","PHYSICS"]
    days=["Mon","Tue",'Wed','Thu','Fri','Sat']
    canvas=Canvas(nw3,width=1000,height=500)
    img=ImageTk.PhotoImage(Image.open('bg5.jpg'))
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack()

    def dayw():
         table=Label(nw3,text=s.daywise(variable.get(),variable2.get()),font=('Courier',10,"bold"),bg="yellow",fg="#050747")
         table.place(x=33,y=250)
    
    head=Label(nw3,text='Select subject and day!!!',font=('Courier',20,"bold","italic",),bg='#70e0d5',fg='#050747')  
    head.place(x=200,y=40) 
    variable=StringVar(nw3)
    variable2=StringVar(nw3)
    variable.set(subjects[0])
    variable2.set(days[0])
    sub=OptionMenu(nw3,variable,*subjects)
    sub.place(x=300,y=115)
    sub.configure(bg='#050747',fg='white')
    per=OptionMenu(nw3,variable2,*days)
    per.place(x=450,y=115)
    per.configure(bg='#050747',fg='white')
    Button(nw3,text="PROCEED",command=dayw,font=('Courier',15,"bold"),bg='#70e0d5',fg='#050747').place(x=365,y=150)
    subh=Label(nw3,text='SUBJECT',font=('Courier',13,"bold"),bg='#70e0d5',fg='#050747')
    subh.place(x=300,y=90)
    dyh=Label(nw3,text='DAY',font=('Courier',13,"bold"),bg='#70e0d5',fg='#050747')
    dyh.place(x=450,y=90)
    nw3.title('DAYWISE TIMETABLE')
    nw3.resizable(0,0)
    label1=Label(nw3,text="Here will be table",font=('Courier',14,"bold"),bg='#70e0d5',fg='#050747')
    label1.place(x=325,y=200)
    nw3.geometry('850x400')
    nw3.mainloop()

def fordelete():
   import timetech as s
   from PIL import ImageTk,Image
   nw4=Toplevel(root)
    
   canvas=Canvas(nw4,width=1000,height=500)
   img=ImageTk.PhotoImage(Image.open('bg2.jpg'))
   canvas.create_image(0,0,anchor=NW,image=img)
   canvas.pack()
   subjects=["MATHS","HINDI","CHEMISTRY","CS","ENGLISH","PHYSICS"]
   days=["MON","TUE",'WED','THU','FRI','SAT']
   def dele():
       s.delete(var1.get(),var2.get())
   head=Label(nw4,text='Enter subject and day to delete entire row!!!',font=('Courier',20,"bold"),fg='#050747',bg='#96e0db')
   head.place(x=50,y=40)    
   var1=StringVar(nw4)
   var2=StringVar(nw4)
   var1.set(subjects[0])
   var2.set(days[0])
   subh=Label(nw4,text='SUBJECT',font=('Courier',13,"bold"),fg='#050747',bg='white')
   subh.place(x=250,y=85)
   dyh=Label(nw4,text='DAY',font=('Courier',13,"bold"),fg='#050747',bg='white')
   dyh.place(x=400,y=85)
   sub=OptionMenu(nw4,var1,*subjects)
   sub.place(x=250,y=110)
   sub.configure(bg='#96e0db',fg='#050747')
   dy=OptionMenu(nw4,var2,*days)
   dy.place(x=400,y=110)
   dy.configure(bg='#96e0db',fg='#050747')
   Button(nw4,text="PROCEED",command=dele,font=('Courier',15,"bold"),bg='#96e0db',fg='#050747').place(x=325,y=170)
   nw4.geometry('840x250')
   nw4.resizable(0,0)
   nw4.title('DELETION')
   nw4.mainloop()

def forupdate():
    import timetech as s
    from PIL import ImageTk,Image
    nw5=Toplevel(root) 
    canvas=Canvas(nw5,width=1150,height=500)
    img=ImageTk.PhotoImage(Image.open('bg4.jpg'))
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack()

    subjects=["MATHS","HINDI","CHEMISTRY","CS","ENGLISH","PHYSICS"]
    days=["MON","TUE",'WED','THU','FRI','SAT']
    period=["I",'II','III','IV','V','VI','VII','VIII']
    clas=["IXA",'IXB','XA','XB','XIA','XIB','XIIA','XIIB','FREE']
    
    def upd():
         s.update(var1.get(),var3.get(),var4.get(),var2.get())
    
    head=Label(nw5,text='Select subject,day,period and class to proceed!!!',font=('Courier',20,"bold","italic",),fg="#050747")
    head.place(x=20,y=45)   
    var1=StringVar(nw5)
    var2=StringVar(nw5)
    var3=StringVar(nw5)
    var4=StringVar(nw5)
    var1.set(subjects[0])
    var2.set(days[0])
    var3.set(period[0])
    var4.set(clas[0])
    subh=Label(nw5,text='SUBJECT',font=('Courier',13,"bold"),bg="#050747",fg="white")
    subh.place(x=150,y=85)
    dyh=Label(nw5,text='DAY',font=('Courier',13,"bold"),bg="#050747",fg="white")
    dyh.place(x=300,y=85)
    perh=Label(nw5,text='PERIOD',font=('Courier',13,"bold"),bg="#050747",fg="white")
    perh.place(x=450,y=85)
    clh=Label(nw5,text='CLASS',font=('Courier',13,"bold"),bg="#050747",fg="white")
    clh.place(x=600,y=85)
    sub=OptionMenu(nw5,var1,*subjects)
    sub.place(x=150,y=110)
    sub.configure(bg='#7ab1e6')
    dy=OptionMenu(nw5,var2,*days)
    dy.place(x=300,y=110)
    dy.configure(bg='#7ab1e6')
    per=OptionMenu(nw5,var3,*period)
    per.place(x=450,y=110)
    per.configure(bg='#7ab1e6')
    cl=OptionMenu(nw5,var4,*clas)
    cl.place(x=600,y=110)
    cl.configure(bg='#7ab1e6')
    nw5.geometry('830x300')
    Button(nw5,text="PROCEED",command=upd,font=('Courier',15,"bold"),bg="#0a3f73",fg="white").place(x=350,y=200)
    nw5.title('update timetable')
    nw5.resizable(0,0)
    nw5.mainloop()

def forinsert():
   nw6=Toplevel(root)
   canvas=Canvas(nw6,width=990,height=400)
   img=ImageTk.PhotoImage(Image.open('efgh.jpg'))
   canvas.create_image(0,0,anchor=NW,image=img)
   canvas.pack()

   def inr():
        s.insert(var1.get(),sri.get(),dayi.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get()
        ,var10.get())
   head=Label(nw6,text="Select subject,day,period ,class and srno. to enter data!!!",fg='#050747',bg='#bbdbf0',
   font=('Courier',20,"bold","italic")) 
   head.place(x=20,y=45)   
   subjects=["MATHS","HINDI","CHEMISTRY","CS","ENGLISH","PHYSICS"]
   
   clas=["IXA",'IXB','XA','XB','XIA','XIB','XIIA','XIIB','FREE']
   days=["MON","TUE",'WED','THU','FRI','SAT']
   sr=[1,2,3,4,5,6]
   
   var1=StringVar(nw6)
   dayi=StringVar(nw6)
   sri=IntVar(nw6)
   var3=StringVar(nw6)
   var4=StringVar(nw6)
   var5=StringVar(nw6)
   var6=StringVar(nw6)
   var7=StringVar(nw6)
   var8=StringVar(nw6)
   var9=StringVar(nw6)
   var10=StringVar(nw6)
   dayi.set(days[0])
   sri.set(sr[0])
   var3.set(clas[-1])
   var4.set(clas[-1])
   var5.set(clas[-1])
   var6.set(clas[-1])
   var7.set(clas[-1])
   var8.set(clas[-1])
   var9.set(clas[-1])
   var10.set(clas[-1])
   var1.set(subjects[0])
   
   subo=OptionMenu(nw6,var1,*subjects)
   subo.place(x=400,y=117)
   subo.configure(bg='#050747',fg='white')
   IO=OptionMenu(nw6,var3,*clas)
   IO.place(x=270,y=187)
   IO.configure(bg='#050747',fg='white')
   IIO=OptionMenu(nw6,var4,*clas)
   IIO.place(x=370,y=187)
   IIO.configure(bg='#050747',fg='white')
   IIIO=OptionMenu(nw6,var5,*clas)
   IIIO.place(x=470,y=187)
   IIIO.configure(bg='#050747',fg='white')
   IVO=OptionMenu(nw6,var6,*clas)
   IVO.place(x=570,y=187)
   IVO.configure(bg='#050747',fg='white')
   VO=OptionMenu(nw6,var7,*clas)
   VO.place(x=270,y=257)
   VO.configure(bg='#050747',fg='white')
   VIO=OptionMenu(nw6,var8,*clas)
   VIO.place(x=370,y=257)
   VIO.configure(bg='#050747',fg='white')
   VIIO=OptionMenu(nw6,var9,*clas)
   VIIO.place(x=470,y=257)
   VIIO.configure(bg='#050747',fg='white')
   VIIIO=OptionMenu(nw6,var10,*clas)
   VIIIO.place(x=570,y=257)
   VIIIO.configure(bg='#050747',fg='white')
   sro=OptionMenu(nw6,sri,*sr)
   sro.place(x=300,y=117)
   sro.configure(bg='#050747',fg='white')
   dayo=OptionMenu(nw6,dayi,*days)
   dayo.place(x=530,y=117)
   dayo.configure(bg='#050747',fg='white')
   subh=Label(nw6,text='Subject',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   dayh=Label(nw6,text='Day',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
  
   I=Label(nw6,text='I',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   II=Label(nw6,text='II',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   III=Label(nw6,text='III',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   IV=Label(nw6,text='IV',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   V=Label(nw6,text='V',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   VI=Label(nw6,text='VI',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   VII=Label(nw6,text='VII',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   VIII=Label(nw6,text='VIII',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   srh=Label(nw6,text='Srno.',font=('Courier',14,"bold"),bg='#bbdbf0',fg='#050747')
   subh.place(x=400,y=90)
   
   I.place(x=270,y=160)
   II.place(x=370,y=160)
   III.place(x=470,y=160)
   IV.place(x=570,y=160)
   V.place(x=270,y=230)
   VI.place(x=370,y=230)
   VII.place(x=470,y=230)
   VIII.place(x=570,y=230)
   srh.place(x=300,y=90)
   dayh.place(x=530,y=90)
   nw6.geometry('990x400')
   nw6.title('INSERT DATA')
   nw6.resizable(0,0)
   Button(nw6,text="PROCEED",command=inr,font=('Courier',15,"bold"),bg='#050747',fg='white').place(x=400,y=300)
   nw6.mainloop()
   
#=================================packing homepage buttons==========================================================================#   
   
Button(root,text='View fulltable',command=forfulltable,background='#00cccc',font=('Courier',12,"bold"),height='2',width='20',
cursor="hand2").place(x=100,y=100)
Button(root,text=' particular period',command=forparticularday,background='#00cccc',font=('Courier',12,"bold"),
height='2',width='20',cursor="hand2").place(x=340,y=100)
Button(root,text='View daywise',command=fordaywise,background='#00cccc',font=('Courier',12,"bold"),
height='2',width='20',cursor="hand2").place(x=590,y=100)
Button(root,text='To delete',command=fordelete,background='#00cccc',font=('Courier',12,"bold"),
height='2',width='20',cursor="hand2").place(x=100,y=155)
Button(root,text='To update',command=forupdate,background='#00cccc',font=('Courier',12,"bold"),
height='2',width='20',cursor="hand2").place(x=340,y=155)
Button(root,text='To insert',command=forinsert,background='#00cccc',font=('Courier',12,"bold"),
height='2',width='20',cursor="hand2").place(x=590,y=155)
root.mainloop()
