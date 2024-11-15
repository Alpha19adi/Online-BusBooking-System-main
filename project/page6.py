from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
img1=PhotoImage(file='.\\home.png')
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=13)
Label(frame1,image=img).grid(row=0,column=0,padx=w/2.5)
Label(frame1,text="Online Bus Booking System",font="Arial 20 bold",bg='light blue',fg='red').grid(row=1,column=0)
Label(frame1,text="Add Bus Details",font="Arial 18 bold",fg='green').grid(row=2,column=0,pady=20)
Label(root,text="Bus ID",font="Arial 11 bold").grid(row=3,column=0,padx=10)
bid=Entry(root,font="Arial 11 bold")
bid.grid(row=3,column=1)
Label(root,text="Bus Type",font="Arial 11 bold").grid(row=3,column=2)
bus_type=StringVar()
option=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1']
bus_type.set('Bus Type')
d_menue=OptionMenu(root,bus_type,*option)
d_menue.grid(row=3,column=3)
#Label(root,text=bus_type.get()).grid(row=4,column=1)
Label(root,text="Capacity",font="Arial 11 bold").grid(row=3,column=4)
capacty=Entry(root,font="Arial 11")
capacty.grid(row=3,column=5)
Label(root,text="Fare Rs",font="Arial 11 bold").grid(row=3,column=6)
fare=Entry(root,font="Arial 11 bold")
fare.grid(row=3,column=7)
Label(root,text="Operator ID",font="Arial 11 bold").grid(row=3,column=8)
oid=Entry(root,font="Arial 11 bold")
oid.grid(row=3,column=9)
Label(root,text="Route ID",font="Arial 11 bold").grid(row=3,column=10)
rid=Entry(root,font="Arial 11 bold")
rid.grid(row=3,column=11)
def add():
    if len(bid.get())==0 or len(capacty.get())==0 or len(fare.get())==0 or len(oid.get())==0 or len(rid.get())==0 or bus_type.get()=='Bus Type':
        showerror('Value Missing','Enter date')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
        cur=conn.cursor()
        cur.execute("""insert into bus(bus_id,bus_type,capacity,fare,op_id,route_id)values("{}","{}","{}","{}","{}","{}")""".format(bid.get(),bus_type.get(),capacty.get(),fare.get(),oid.get(),rid.get()))
        conn.commit()
        conn.close()
Button(root,text="Add Bus",font='Arial 14 bold',bg='light green',command=add).grid(row=4,column=5,pady=20)
Button(root,text="Edit Bus",font='Arial 14 bold',bg='light green').grid(row=4,column=6,pady=20)
Button(root,image=img1).grid(row=4,column=7,pady=20)
root.mainloop()