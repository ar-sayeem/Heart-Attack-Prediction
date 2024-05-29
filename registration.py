import pyrebase
import subprocess
from tkinter import *
from tkinter import messagebox
import ast
window = Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

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


### - - - - - - - - - - - - - - - Data - - - - - - - - - - - - - - - ###


def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            user_info = auth.create_user_with_email_and_password(
                username, password)

            messagebox.showinfo("Signup", "Successfully signed up")
        except Exception as e:
            messagebox.showerror("Error", "Signup failed")
    else:
        messagebox.showerror('Invalid', "Both passwords should match")


### - - - - - - - - - - - - - - - Image - - - - - - - - - - - - - - - ###


img = PhotoImage(file='Images/reg2.png')   # file='reg2.png'
Label(window, image=img, border=0, bg='white').place(x=50, y=90)
frame = Frame(window, width=350, height=390, bg='white')  # bg='#77C3EC'
frame.place(x=480, y=50)


heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white',
                font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


### - - - - - - - - - - - - - - - User Name - - - - - - - - - - - - - - - ###

def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Enter your gmail')


user = Entry(frame, width=25, fg='#474747', border=0,   #  fg='white'   #B3B3B3
             bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)          # Location
user.insert(0, 'user@gmail.com')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


### - - - - - - - - - - - - - - - Password - - - - - - - - - - - - - - - ###


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Enter your password')


code = Entry(frame, width=25, fg='#474747', border=0,   # #B3B3B3
             bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)          # Change 70
code.insert(0, 'password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)    # Change 70


### - - - - - - - - - - - - - Confirm Password - - - - - - - - - - - - - ###


def on_enter(e):
    confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm your password')


confirm_code = Entry(frame, width=25, fg='#474747', border=0,   # #B3B3B3
                     bg='white', font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=30, y=220)     # Change 70
confirm_code.insert(0, 'confirm password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)    # Change 70


### - - - - - - - - - - - - - - - Button - - - - - - - - - - - - - - - ###

# Button(frame, width=39, pady=7, text='Sign up',
#        bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
# label = Label(frame, text='Already have an account!', fg='black',
#               bg='white', font=('Microsoft YaHei UI Light', 9))
# label.place(x=79, y=340)
# signin = Button(frame, width=6, text='Sign in', border=0,
#                 bg='white', cursor='hand2', fg='#57a1f8')
# signin.place(x=221, y=340)

def open_login_script():
    subprocess.Popen(["python", "Login.py"])
    window.destroy()


signin_button = Button(frame, width=39, pady=7, text='Sign up',
                       bg='#57a1f8', fg='white', border=0, command=signup)
signin_button.place(x=35, y=280)

label = Label(frame, text='Already have an account!', fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=79, y=340)

# Create a Sign-in button
signin = Button(frame, width=6, text='Sign in', border=0,
                bg='white', cursor='hand2', fg='#57a1f8', command=open_login_script)
signin.place(x=221, y=340)


window.mainloop()
