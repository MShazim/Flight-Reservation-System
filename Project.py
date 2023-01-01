#importing tkinter and pyodbc
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tk import *
import pyodbc 

#Connecting Database
connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-4LORV5Q\SQLEXPRESS;' 
'Database=FRS;' 'Trusted_connection=yes;')
cursor = connection.cursor()

#Main Menu
root = Tk()
root.wm_title("FLIGHT RESERVATION SYSTEM")
root['background']='#21618C'
Label(root,text="Flight Reservation System", font=('{Product Sans} 30 bold underline'), fg='#ffffff', bg= '#21618C').grid()

#main menu text
Label(root,text="\nWelcome to our Airline Reservation!\nWe are glad to have you here and are\nexcited to help you plan your next trip.\n", 
font=('{Product Sans} 20 italic '), fg='#ffffff', bg= '#21618C').grid(row=3,column=0, padx=10, pady=10,sticky=E)
root.geometry('490x550')

#Search Function
def fun1():
    root.destroy()
    root1=Tk()
    root1.title("FLIGHT SEARCHING")
    root1.geometry('480x300')
    root1['background']='#21618C'
    Label(root1,text="Search your Flight", font=('{Product Sans}  30 bold underline'),fg='#ffffff', bg= '#21618C').grid(sticky=W)
    Label(root1,text="\nPlease enter the following details to search your flight.\n", font=('{Product Sans} 15 italic '), fg='#ffffff', bg= '#21618C').grid(sticky=W)

    ## Creating a Boarding Dropdown
    Label(root1,text="Boarding: ", font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=2,column=0,sticky=W)
    def place_dropdown():
        cur = connection.cursor()
        cur.execute("select PlaceName from Places")
        data = []
        for Place in cur.fetchall():
            data.append(Place[0])
        return data
    q1 = StringVar()
    w1=ttk.Combobox(root1, height=10,width=20,textvariable=q1, state = 'readonly')
    w1['values'] = place_dropdown()
    w1.grid(row=2,column=0)

    ##Creating a Destination 
    Label(root1,text="Destination: ", font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=3,column=0,sticky=W)
    q2 = StringVar()
    w2=ttk.Combobox(root1, height=10,width=20,textvariable=q2, state = 'readonly')
    w2['values'] = place_dropdown()
    w2.grid(row=3,column=0)

    ## Creating a Day of Travel
    Label(root1,text="Day of travel: ", font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=4,column=0,sticky=W)
    w3=ttk.Combobox(root1,height=10,width=20,values=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
    w3.grid(row=4,column=0)

    #Search Button Functions
    def  search_function():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        cur=connection.cursor()
        if a=='' or b=='' or c=='':
            messagebox.showerror("Error","Cant leave any field empty")
        else:
            if a!=b:
                cur.execute("select FlightName , Dep_time , Arr_time , Source , Destination from Flight where source=? and destination=?",(a,b))
                z = cur.fetchall()

                #creating a searched flight window
                root1.destroy()
                root2=Tk()
                root2.title("SEARCHED FLIGHT")
                root2.geometry('480x300')
                root2['background']='#21618C'
                Label(root2,text="Available Flights", font=('{Product Sans}  30 bold underline'),fg='#ffffff', bg= '#21618C').grid(sticky=W)
                Label(root2,text="\nThese are the available flights", font=('{Product Sans} 15 italic '), fg='#ffffff', bg= '#21618C').grid(sticky=W)
                T = tk.Text(root2, height=5, width=55)
                T.grid(row=2,column=0)
                T.insert(tk.END, z)

                #book flight button
                B2=Button(root2,text="Book Flight", font=('Poppins 10 bold'),height=0,width=12,fg='#21618C', borderwidth=3, relief="flat",
                bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff',command=fun2).grid(row=4,column=0, padx=10, pady=10,sticky=N)
                root2.mainloop()           
            else:
                messagebox.showerror("Oops","Boarding and Destination can't be same")  
    
    #search button
    Bs=Button(root1,text="Search", font=('Poppins 10 bold'), height=0,width=10,fg='#21618C', borderwidth=3, relief="flat",
    bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff', command=search_function).grid(row=5,column=0,padx=5, pady=5,sticky=N)
    root1.mainloop()

#Booking Button Function
def fun2():
    root3=Tk()
    root3.title('FLIGHT BOOKING')
    root3.geometry('490x600')
    root3['background']='#21618C'
    Label(root3,text="Book your Flight", font=('{Product Sans}  30 bold underline'),fg='#ffffff', bg= '#21618C').grid(sticky=W)
    Label(root3,text="\nPlease enter the following details to book your flight.\n", font=('{Product Sans} 15 italic '), fg='#ffffff', bg= '#21618C').grid(sticky=W)

    #creating boarding field
    Label(root3,text="Boarding",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=2,column=0,sticky=W)
    def place_dropdown():
        cur = connection.cursor()
        cur.execute("select PlaceName from Places")
        data = []
        for Place in cur.fetchall():
            data.append(Place[0])
        return data
    q1 = StringVar()
    w1=ttk.Combobox(root3, height=10,width=20,textvariable=q1, state = 'readonly')
    w1['values'] = place_dropdown()
    w1.grid(row=2,column=0)

    #creating destination field
    Label(root3,text="Destination:",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=3,column=0,sticky=W)
    q2 = StringVar()
    w2=ttk.Combobox(root3, height=10,width=20,textvariable=q2, state = 'readonly')
    w2['values'] = place_dropdown()
    w2.grid(row=3,column=0)
    
    #creating class field
    #function for class dropdown menu
    def class_dropdown():
        cur = connection.cursor()
        cur.execute("select Class_type from Class")
        data1 = []
        for classes in cur.fetchall():
            data1.append(classes[0])
        return data1
    Label(root3,text="Class:",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=4,column=0,sticky=W)
    q3 = StringVar()
    w3=ttk.Combobox(root3, height=10,width=20,textvariable=q3, state = 'readonly')
    w3['values'] = class_dropdown()
    w3.grid(row=4,column=0)

    #creating FirstName field
    Label(root3,text="First Name: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=5,column=0,sticky=W)
    firstname = Entry(root3, width=23)
    firstname.grid(row=5, column=0) 
    
    #creating LastName field
    Label(root3,text="Last Name: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=6,column=0,sticky=W)
    lastname = Entry(root3, width=23)
    lastname.grid(row=6, column=0)
    
    #creating Email field
    Label(root3,text="Email: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=7,column=0,sticky=W)
    email = Entry(root3, width=23)
    email.grid(row=7, column=0)
    
    #creating MobileNo field
    Label(root3,text="Mobile No: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=8,column=0,sticky=W)
    mobile = Entry(root3, width=23)
    mobile.grid(row=8, column=0)
    
    #creating PassportNo field
    Label(root3,text="Passport No: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=9,column=0,sticky=W)
    passport = Entry(root3, width=23)
    passport.grid(row=9, column=0)

    #creating DOB field
    Label(root3,text="Date of Birth: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=10,column=0,sticky=W)
    dob = Entry(root3, width=23)
    dob.grid(row=10, column=0)
    Label(root3,text="(YYYY-MM-DD)", font=('{Product Sans} 10  '), fg='#ffffff', bg= '#21618C').grid(row=10,column=0,sticky=E)

    #creating Address field
    Label(root3,text="Address ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=11,column=0,sticky=W)
    address = Entry(root3, width=23)
    address.grid(row=11, column=0)
    
    #creating Gender field
    Label(root3,text="Gender: ", font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=12,column=0,sticky=W)
    g1=ttk.Combobox(root3,height=10,width=20,values=["Male","Female"])
    g1.grid(row=12,column=0)

    #creating Day field
    Label(root3,text="Day of travel: ", font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=13,column=0,sticky=W)
    w4=ttk.Combobox(root3,height=10,width=20,values=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
    w4.grid(row=13,column=0)
    
    #fuction to book flight
    def book():
        a = w1.get()
        b = w2.get()
        c = w3.get()
        d = firstname.get()
        e = lastname.get()
        f = email.get()
        g = mobile.get()
        h = passport.get()
        i = dob.get()
        j = address.get()
        k = g1.get()
        l = w4.get()
        cur=connection.cursor()
        if a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='' or i=='' or j=='' or k==''  or l=='':
            messagebox.showerror("Error","Cant leave any field empty")
        else:
            if a!=b:
                cur.execute("insert into Passenger (F_Name,L_Name,Email,DOB,Gender,[Address],Source, Destination, Class,[Day],PassportNo,MobileNo) values(?,?,?,?,?,?,?,?,?,?,?,?)",(d,e,f,i,k,j,a,b,c,l,h,g))
                connection.commit()
                root3.destroy()
                root6=Tk()
                root6.title('TICKET')
                root6.geometry('480x300')
                root6['background']='#21618C'
                Label(root6,text="YOUR TICKET", font=('{Product Sans}  30 bold underline'),fg='#ffffff', bg= '#21618C').grid(sticky=W)

                cur.execute("insert into Ticket (Source,Destination,PassportNo,F_Name,L_Name,[Day],Class,MobileNo) values(?,?,?,?,?,?,?,?)",(a,b,h,d,e,l,c,g))
                connection.commit()
                cur.execute("select F_Name,L_Name,Source, Destination, Class,[Day],PassportNo from Passenger where PassportNo=?",h)
                z1 = cur.fetchall()
                T1 = tk.Text(root6, height=5, width=55)
                T1.grid(row=2,column=0)
                T1.insert(tk.END, z1)

                Label(root6,text="TICKET ID", font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=3,column=0,sticky=W)
                cur.execute("select Ticket_id from Ticket where PassportNo=?",h)
                z2 = cur.fetchall()
                T2 = tk.Text(root6, height=5, width=55)
                T2.grid(row=4,column=0)
                T2.insert(tk.END, z2)
                root6.mainloop()
            else:
                messagebox.showerror("Oops","Boarding and Destination can't be same") 
                
                
    #Inserting/book flight button
    B4=Button(root3,text="Book Flight", font=('Poppins 10 bold'),height=0,width=12,fg='#21618C', borderwidth=3, relief="flat",
    bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff',command=book).grid(row=14,column=0, padx=10, pady=10,sticky=N)

#Cancel Button Fuction
def fun3():
    root.destroy()
    root4=Tk()
    root4.title("FLIGHT CANCELLATION")
    root4.geometry('480x350')
    root4['background']='#21618C'
    Label(root4,text="Cancel your Flight", font=('{Product Sans}  30 bold underline'),fg='#ffffff', bg= '#21618C').grid(sticky=W)
    Label(root4,text="\nPlease enter the following details to cancel your flight.\n", font=('{Product Sans} 15 italic '), fg='#ffffff', bg= '#21618C').grid(sticky=W)\

    #creating PassportNo field
    Label(root4,text="Passport No: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=2,column=0,sticky=W)
    passport = Entry(root4, width=23)
    passport.grid(row=2, column=0)

    #creating TicketNo field
    Label(root4,text="Ticket No: ",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=3,column=0,sticky=W)
    ticket  = Entry(root4, width=23)
    ticket.grid(row=3, column=0)

    #creating boarding field
    Label(root4,text="Boarding",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=4,column=0,sticky=W)
    def place_dropdown():
        cur = connection.cursor()
        cur.execute("select PlaceName from Places")
        data = []
        for Place in cur.fetchall():
            data.append(Place[0])
        return data
    q1 = StringVar()
    w1=ttk.Combobox(root4, height=10,width=20,textvariable=q1, state = 'readonly')
    w1['values'] = place_dropdown()
    w1.grid(row=4,column=0)

    #creating Class field
    def class_dropdown():
        cur = connection.cursor()
        cur.execute("select Class_type from Class")
        data1 = []
        for classes in cur.fetchall():
            data1.append(classes[0])
        return data1
    Label(root4,text="Class:",font=('{Product Sans} 15 bold '), fg='#ffffff', bg= '#21618C').grid(row=5,column=0,sticky=W)
    q3 = StringVar()
    w3=ttk.Combobox(root4, height=10,width=20,textvariable=q3, state = 'readonly')
    w3['values'] = class_dropdown()
    w3.grid(row=5,column=0)

    #cancel button operation
    def cancel():
        a = passport.get()
        b = ticket.get()
        c = w1.get()
        d = w3.get()
        cur=connection.cursor()
        if a=='' or b=='' or c=='' or d=='':
            messagebox.showerror("Oops","You can't Enter the leave any field empty")
        else:
            if a!=b:
                cur.execute('Delete From Ticket where PassportNo = ? and Ticket_id = ?',(a,b))
                cur.execute('Delete From Passenger where PassportNo = ?',a)
                connection.commit()
                messagebox.showinfo("RESERVATION CANCEL","Your Reservation is Cancelled!")
            else:
                messagebox.showerror("Oops","PassportNo and TicketNo Can't be same Enter Again!")

    #Cancel Reservation button
    B4=Button(root4,text="Cancel Reservation", font=('Poppins 10 bold'),height=0,width=17,fg='#21618C', borderwidth=3, relief="flat",
    bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff',command=cancel).grid(row=6,column=0, padx=10, pady=10,sticky=N)


#Button Of Search Flight in Main Menu
B1=Button(root,text="Search Flight", font=('Poppins 15 bold'),height=0,width=15,fg='#21618C', borderwidth=3, relief="flat",
bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff', command=fun1).grid(row=4,column=0, padx=10, pady=10,sticky=N)

#Button Of Book Flight in Main Menu
B2=Button(root,text="Book Flight", font=('Poppins 15 bold'),height=0,width=15,fg='#21618C', borderwidth=3, relief="flat",
bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff', command=fun2).grid(row=5,column=0, padx=10, pady=10,sticky=N)

#Button Of Cancel Booking in Main Menu
B3=Button(root,text="Cancel Booking", font=('Poppins 15 bold'),height=0,width=15,fg='#21618C', borderwidth=3,relief="flat",  
bg='#ffffff', activebackground='#21618C',activeforeground='#ffffff', command=fun3).grid(row=6,column=0, padx=10, pady=10,sticky=N)
root.mainloop()