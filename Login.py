import pyrebase     # firebase
import subprocess   # login->signup
from telnetlib import AUTHENTICATION    # usename | password checkup
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Sign In')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


### - - - - - - - - - - - - fire base start - - - - - - - - - - - - - - ###

firebaseConfig = {
    'apiKey': "AIzaSyCOpWi3_WbYCMkb7psfVshZUTxaYE_QkQI",
    'authDomain': "healthy-heart-24-7.firebaseapp.com",
    'databaseURL': "",
    'projectId': "healthy-heart-24-7",
    'storageBucket': "healthy-heart-24-7.appspot.com",
    'messagingSenderId': "209952531314",
    'appId': "1:209952531314:web:19fed23df6d50ee86c33eb"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def signin():
    email = user.get()  # username_entry.get()
    password = code.get()
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        messagebox.showinfo("Success", "Welcome back, " +
                            email + " Successfully logged in!")
        subprocess.Popen(["python", "main.py"])
        root.destroy()
        
    except Exception as e:
        messagebox.showerror("Error", "Invalid username & password")


img = PhotoImage(file="Images/login.png")   # Images/login.png
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


user = Entry(frame, font=('Segoe UI', 12))
user.place(x=50, y=100)
code = Entry(frame, font=('Segoe UI', 12), show='*')
code.place(x=50, y=150)


signin_button = Button(frame, text="Sign In", command=signin)
signin_button.place(x=50, y=200)


### - - - - - - - - - - - - - - - Image - - - - - - - - - - - - - - - ###


img = PhotoImage(file="Images/login.png")   # Images/login.png
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


### - - - - - - - - - - - - - - - User name - - - - - - - - - - - - - - - ###

def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):        # Shadow Username
    name = user.get()
    if name == '':
        user.insert(0, 'Enter your gmail')


user = Entry(frame, width=25, fg='#474747', border=0,   # #B3B3B3
             bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'user@gmail.com')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


### - - - - - - - - - - - - - - - Password - - - - - - - - - - - - - - - ###


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):        # Shadow Password
    name = code.get()
    if name == '':
        code.insert(0, 'Enter your password')


code = Entry(frame, width=25, fg='#474747', border=0,   # #B3B3B3
             bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


### - - - - - - - - - - - - - - - Buttons - - - - - - - - - - - - - - - ###

def open_login_script():
    subprocess.Popen(["python", "registration.py"])
    root.destroy()


signin_button = Button(frame, width=39, pady=7, text='Sign in',
                       bg='#57a1f8', fg='white', border=0, command=signin)
signin_button.place(x=35, y=220)

label = Label(frame, text='Already have an account!', fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=79, y=300)


### - - - - - - - - - - - - - - Create a Sign-in button - - - - - - - - - - - - - -###

signin = Button(frame, width=6, text='Sign up', border=0,
                bg='white', cursor='hand2', fg='#57a1f8', command=open_login_script)
signin.place(x=221, y=300)


root.mainloop()
