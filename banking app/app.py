#imports
from tkinter import *
import os
from tkinter import font
from PIL import ImageTk, Image

#Main screeen
master = Tk()
master.title('Banking APP')

#functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    
    if name == " " or age == " " or gender == " " or password == " ":
        notif.config(fg="red",text="all fields are requierd")
        return
    
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="account already existe")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name='\n')
            new_file.write(password='\n')
            new_file.write(age='\n')
            new_file.write(gender='\n')
            new_file.close()
            notif.config(fg="green", text="account has been created")

def register():
    #vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #register screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    #lable
    Label(register_screen, text="please enter your details below to register",font=('Callirbi',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name",font=('Callirbi',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age",font=('Callirbi',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender",font=('Callirbi',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password",font=('Callirbi',12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=('Callirbi',12))
    notif.grid(row=6,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)

    #buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Calliri,12')).grid(row=5,sticky=N,pady=10)
def login():
    print("this is a login page")


#Image import
img = Image.open('img.jpg')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#lables
Label(master, text = "Custom Banking Beta", font = ('Callbri', 14)).grid(row=0,sticky=N )
Label(master, text = "the most sucure bank you will ever use", font = ('Callbri', 12)).grid(row=1,sticky=N )
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#buttons
Button(master, text="Register",font=('Callbri, 12'),width=20, command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
