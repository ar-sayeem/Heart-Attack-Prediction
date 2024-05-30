from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox

import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from backend import *

# - - - changes - - - #
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter.filedialog import asksaveasfilename
# - - - changes - - - #


# Need to increase
# from sklearn.linear_model import LogisticRegression


background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

mroot = Tk()
mroot.title("Healthy Heart")
mroot.geometry("1450x730+60+80")
mroot.resizable(False, False)
mroot.config(bg=background)


### - - - - - - - - - - - - - - - - - - - - - ANALYSIS - - - - - - - - - - - - - - - - - - - - - ###

def analysis():

    global prediction

    name = Name.get()
    D1 = Date.get()
    today = datetime.date.today()
    A = today.year-DOB.get()

    try:
         B = selection()
    except:
        messagebox.showerror("missing", "Please select gender!")
        return
    try:
         F = selection2()
    except:
        messagebox.showerror("missing", "Please select fbs!")
        return

    try:
         I = selection3()
    except:
        messagebox.showerror("missing", "Please select exang!")
        return
    
    try:
         C = int(selection4())
    except:
        messagebox.showerror("missing", "Please select cp!")
        return
    
    try:
         G = int(selection6())    #int(restecg_combobox.get())
    except:
        messagebox.showerror("missing", "Please select restecg!")
        return
    
    try:
         K = int(selection5())
    except:
        messagebox.showerror("missing", "Please select slope!")
        return

    try:
         L = int(ca_combobox.get())
    except:
        messagebox.showerror("missing", "Please select ca!")
        return

    try:
         M = int(selection7())  #int(thal_combobox.get())
    except:
        messagebox.showerror("missing", "Please select thal!")
        return

    try:
         D = int(trestbps.get())
         E = int(chol.get())
         H = int(thalach.get())
         J = float(oldpeak.get())
    except:
        messagebox.showerror("missing data", "Few missing data entry!")
        return

    
    ### - - - - - - - - - - - - - - - - - - - - - TESTING Data Entry - - - - - - - - - - - - - - - - - - - - - ###
    ### - - - - - - - - - - -- - - This will print if Analysis Button Clicked - - - - - - - - - - - - - - - - - ###
    
    # print("A is age: ",A)
    # print("B is gender: ",B)
    # print("C is cp: ",C)
    # print("D is trestbps: ",D)
    # print("E is chol: ", E)
    # print("F is fbs: ",F)
    # print("G is restcg: ",G)
    # print("H is thalach: ",H)
    # print("I is Exang: ",I)
    # print("J is oldpeak: ",J)
    # print("K is slop: ",K)
    # print("L is ca: ",L)
    # print("M is thal: ",M)


    ### - - - - - - - - - - - - - - - - - - - - - First Graph - - - - - - - - - - - - - - - - - - - - - ###
    
    f = Figure(figsize=(5,5), dpi=65)       #dpi-100
    a = f.add_subplot(111)      #f.add_subplot(111)
    a.plot(["Sex", "fbs", "exang"],[B,F,I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=600,y=230)        # G1 width=250,height=250,x=600,y=240


    #### - - - - - - - - - - - - - - - - - - - - - Second graph - - - - - - - - - - - - - - - - - - - - - ###

    f2 = Figure(figsize=(5,5), dpi=65)      #dpi-100
    a2 = f2.add_subplot(111)        #f.add_subplot(111)
    a2.plot(["age", "trestbps", "chol", "thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas2._tkcanvas.place(width=250, height=250,x=860,y=230)      # G2 width=250, height=250,x=860,y=240


    ### - - - - - - - - - - - - - - - - - - - - - Third graph - - - - - - - - - - - - - - - - - - - - - ###

    f3 = Figure(figsize=(5,5), dpi=65)      #dpi-100
    a3 = f3.add_subplot(111)        #f.add_subplot(111)
    a3.plot(["oldpeak", "resticg", "cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas3._tkcanvas.place(width=250,height=250,x=600,y=470)


    #### - - - - - - - - - - - - - - - - - - - - - Fourth graph - - - - - - - - - - - - - - - - - - - - - ###

    f4 = Figure(figsize=(5,5), dpi=65)      #dpi-100
    a4 = f4.add_subplot(111)        #f.add_subplot(111)
    a4.plot(["slope", "ca", "thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas4._tkcanvas.place(width=250,height=250,x=860, y=470)


    ### - - - - - - - - - - - - - - - - - - - - - Input DATA - - - - - - - - - - - - - - - - - - - - - ###
    
    input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)
    input_data_as_numpy_array=np.asanyarray(input_data)


    ### - - - - - - - - - - - - - - - - - - - - - Reshape the numpy array - - - - - - - - - - - - - - - - - - - - - ###

    input_data_reshape= input_data_as_numpy_array.reshape(1,-1)
    prediction= model.predict(input_data_reshape)
    print (prediction[0])

    if(prediction [0]==0):
        print('The Person does not have a Heart disease')
        report.config(text=f"Report: {0}",fg="#8dc63f")
        report1.config(text=f"{name}, \nyou do not have a heart disease")

    else:
        print('The Person has Heart disease')
        report.config(text=f"Report: {1}",fg="#ed1c24")
        report1.config(text=f"{name}, \nyou have a heart disease")


### - - - - - - - - - - - - - - - - - - - - - Info Window(Click window Button) - - - - - - - - - - - - - - - - - - - - - ###

def Info():
    icon_window=Toplevel(mroot)
    icon_window.title("Info")
    icon_window.geometry("700x600+400+100")


    ### - - - - - - - - - - - - - - - - - - - - - icon_image - - - - - - - - - - - - - - - - - - - - - ###

    icon_image=PhotoImage(file="Images/info25x25.png")
    icon_window.iconphoto (False, icon_image)


    ### - - - - - - - - - - - - - - - - - - - - - Heading - - - - - - - - - - - - - - - - - - - - - ###

    Label(icon_window, text="Information Related to dataset", font="robot 19 bold").pack (padx=20, pady=20)


    ### - - - - - - - - - - - - - - - - - - - - - info - - - - - - - - - - - - - - - - - - - - - ###

    Label(icon_window,text="Age - Age in years",font="arial 11").                                                                                      place(x=20,y=100)
    Label(icon_window,text="Sex  - Sex [Male / Female]",font="arial 11").                                                                         place(x=20,y=130)
    Label(icon_window,text="Cp - Chest pain type [Typical angina / Atypical angina / Non-anginal pain / Asymptomatic]",font="arial 11"). place(x=20,y=160)
    Label(icon_window,text="Trestbps - Resting blood pressure (in mm Hg [Normal BPS 60 to 100] on admission to the hospital)",font="arial 11").                                    place(x=20,y=190)
    Label(icon_window,text="Chol - Serum Cholestoral in mg/dl",font="arial 11").                                                                        place(x=20,y=220)
    Label(icon_window,text="Fbs - Fasting blood sugar > (Normal 120 mg/dl) [Yes / No]",font="arial 11").                                             place(x=20,y=250)
    Label(icon_window,text="Restecg - Resting electrocardiographic results [Normal / Having ST-T / Hypertrophy]",font="arial 11").               place(x=20,y=280)
    Label(icon_window,text="Thalach - Maximum heart rate is 220 minus your age. For a 50-year-old, it's 170 beats per minute.",font="arial 11").                                                                       place(x=20,y=310)
    Label(icon_window,text="Exang - Exercise induced angina [Yes / No]",font="arial 11").                                                         place(x=20,y=340)
    Label(icon_window,text="Oldpeak - ST depression induced by exercise relative to rest",font="arial 11").                                                place(x=20,y=370)
    Label(icon_window,text="Slope - The slope of the peak exercise ST segment [Upsloping / Flat / Downsloping]",font="arial 11").              place(x=20,y=400)
    Label(icon_window,text="Ca - Number of major vessels [0-3] colored by flourosopy",font="arial 11").                                               place(x=20,y=430)
    Label(icon_window,text="Thal(Thalassemia) - [Normal / Fixed defect / Reversable defect]",font="arial 11").                                               place(x=20,y=460)

    icon_window.mainloop()


### - - - - - - - - - - - - - - - - - - - - - LogOut - - - - - - - - - - - - - - - - - - - - - ###

def logout():
    mroot.destroy()  # Close the current Tkinter window
    os.system("python main.py")  # Reopen the main.py script



### - - - - - - - - - - - - - - - - - - - - - CLEAR - - - - - - - - - - - - - - - - - - - - - ###

def Clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.get('')
    oldpeak.get('')


### - - - - - - - - - - - - - - - - - - - - - Save - - - - - - - - - - - - - - - - - - - - - ###

def save():
    B2 = Name.get()
    C2 = Date.get()
    D2 = DOB.get()

    today = datetime.date.today()
    E2 = today.year - DOB.get()

    try:
        F2 = selection()
    except:
        messagebox.showerror("Missing Data", "Please select gender!")
    try:
        J2 = selection2()
    except:
        messagebox.showerror("Missing Data", "Please select fbs!")
    try:
        M2 = selection3()
    except:
        messagebox.showerror("Missing Data", "Please select exang!")
    try:
        G2 = selection4()
    except:
        messagebox.showerror("Missing Data", "Please select cp!")
    try:
        O2 = selection5()
    except:
        messagebox.showerror("Missing Data", "Please select slope!")
    try:
        K2 = restecg_combobox.get()
    except:
        messagebox.showerror("Missing Data", "Please select restcg!")
    try:
        P2 = ca_combobox.get()
    except:
        messagebox.showerror("Missing Data", "Please select ca!")
    try:
        Q2 = thal_combobox.get()
    except:
        messagebox.showerror("Missing Data", "Please select thal!")

    H2 = trestbps.get()
    I2 = chol.get()
    L2 = thalach.get()
    N2 = float(oldpeak.get())


    ### - - - - - - - - - - -- - - This will print if Save Button Clicked - - - - - - - - - - - - - - - - - ###

    print('Date: ', C2)

    print('Patient Name: ', B2)
    print('Year of Birth: ', D2)
    print('Age : ', E2)

    print('Gender: ', F2)
    print('Fbs(Fasting blood sugar): ', J2)
    print('Exang(exercise induced angina): ', M2)

    print('CP(Chest pain type): ', G2)

    print('Resecg(Resting electrocardiographic): ', K2)
    print('Trestbps(Resting blood pressure): ', H2)

    print('Slope(Peak exercise ST segment): ', O2)
    print('Chol(Serum Cholestoral in mg/dl): ', I2)

    print('CA(Number of major vessels): ', P2)
    print('Thalach(Maximum heart rate achieved): ', L2)
    
    print('Thalassemia: ', Q2)
    print('OldPeak(ST depression induced by exercise): ', N2)


    ### - - - - - - - - - - - - - - - Ask the user where to save the PDF file - - - - - - - - - - - - - - - ###
    file_path = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    # Create the PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.drawString(30, height - 30, f'Date: {C2}')
    c.drawString(30, height - 60, f'Patient Name: {B2}')
    c.drawString(30, height - 90, f'Year of Birth: {D2}')
    c.drawString(30, height - 120, f'Age : {E2}')
    c.drawString(30, height - 150, f'Gender: {F2}')
    c.drawString(30, height - 180, f'Fbs(Fasting blood sugar): {J2}')
    c.drawString(30, height - 210, f'Exang(Exercise induced angina): {M2}')
    c.drawString(30, height - 240, f'CP(Chest pain type): {G2}')
    c.drawString(30, height - 270, f'Resecg(Resting electrocardiographic): {K2}')
    c.drawString(30, height - 300, f'Trestbps(Resting blood pressure): {H2}')
    c.drawString(30, height - 330, f'Slope(Peak exercise ST segment): {O2}')
    c.drawString(30, height - 360, f'Chol(Serum Cholestoral in mg/dl): {I2}')
    c.drawString(30, height - 390, f'CA(Number of major vessels): {P2}')
    c.drawString(30, height - 420, f'Thalach(Maximum heart rate achieved): {L2}')
    c.drawString(30, height - 450, f'Thalassemia: {Q2}')
    c.drawString(30, height - 480, f'OldPeak(ST depression induced by exercise): {N2}')

    c.showPage()
    c.save()

    messagebox.showinfo("Saved", f"Data saved successfully to {file_path}")


### - - - - - - - - - - - - - - - - - - - - - icon - - - - - - - - - - - - - - - - - - - - - ###

image_icon = PhotoImage(file="Images/icon3.png")
mroot.iconphoto(False, image_icon)


### - - - - - - - - - - - - - - - - - - - - - Header section - - - - - - - - - - - - - - - - - - - - - ###

logo = PhotoImage(file="Images/header.png")      #Images/cover600x200.png
myimage = Label(image=logo, bg=background)
myimage.place(x=0, y=0)


### - - - - - - - - - - - - - - - - - - - - - Frame - - - - - - - - - - - - - - - - - - - - - ###

#mroot, width=800, height=190, bg="#df2d4b"
Heading_entry = Frame(mroot, width=849, height=200, bg="#df2d4b")
Heading_entry.place(x=600, y=2)     #x=600, y=0

Label(Heading_entry, text="Registration No.", font="arial 13",
      bg="#df2d4b", fg=framefg). place(x=30, y=0)
Label(Heading_entry, text="Date", font="arial 13",
      bg="#df2d4b", fg=framefg). place(x=430, y=0)

Label(Heading_entry, text="Patient Name", font="arial 13",
      bg="#df2d4b", fg=framefg). place(x=30, y=90)
Label(Heading_entry, text="Birth Year", font="arial 13",
      bg="#df2d4b", fg=framefg). place(x=430, y=90)


# NEET to ADD Pictute

Entry_image  = PhotoImage(file="Images/rec1.png")
Entry_image2 = PhotoImage(file="Images/rec2.png")
Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=20, y=30)
Label(Heading_entry, image=Entry_image, bg="#df2d4b"). place(x=430, y=30)

Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=20, y=120)
Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=430, y=120)


Registration = IntVar()
reg_entry = Entry(Heading_entry, textvariable=Registration,
                  width=30, font="arial 15", bg="#0e5363", fg="white", bd=0)
reg_entry.place(x=30, y=45)

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(Heading_entry, textvariable=Date, width=15,
                   font='arial 15', bg="#0e5363", fg="white", bd=0)
date_entry.place(x=500, y=45)
Date.set(d1)

Name = StringVar()
name_entry = Entry(Heading_entry, textvariable=Name, width=20,
                   font="arial 20", bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=30, y=130)

DOB = IntVar()
dob_entry = Entry(Heading_entry, textvariable=DOB, width=20,
                  font="arial 20", bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=450, y=130)


### - - - - - - - - - - - BODY - - - - - - - - - - - - ###

# mroot, width=490, height=260, bg="#dbe0e3"
Detail_entry = Frame(mroot, width=480, height=245, bg="#dbe0e3")
Detail_entry.place(x=30, y=450)  # x=30, y=450


### Radio button ###
Label(Detail_entry, text="sex:", font="arial 13",
      bg=framebg, fg=framefg).place(x=5, y=10)
Label(Detail_entry, text="fbs: ", font="arial 13",
      bg=framebg, fg=framefg).place(x=175, y=10)
Label(Detail_entry, text="exang: ", font="arial 13",
      bg=framebg, fg=framefg).place(x=330, y=10)


def selection():
    if gen.get() == 1:
        Gender = 1
        return (Gender)
    elif gen.get() == 2:
        Gender = 0
        return (Gender)
    else:
        print(Gender)


def selection2():
    if fbs.get() == 1:
        Fbs = 1
        return (Fbs)
        print(Fbs)
    elif fbs.get() == 2:
        Fbs = 0
        return (Fbs)
        print(Fbs)
    else:
        print(Fbs)


def selection3():
    if exang.get() == 1:
        Exang = 1
        return (Exang)
        print(Exang)
    elif exang.get() == 2:
        Exang = 0
        return (Exang)
        print(Exang)
    else:
        print(Exang)


gen = IntVar()
R1 = Radiobutton(Detail_entry, text='Male', variable=gen,
                 value=1, command=selection)
R2 = Radiobutton(Detail_entry, text="Female",
                 variable=gen, value=2, command=selection)
R1.place(x=43, y=10)
R2.place(x=93, y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry, text='Yes', variable=fbs,
                 value=1, command=selection2)
R4 = Radiobutton(Detail_entry, text="No", variable=fbs,
                 value=2, command=selection2)
R3.place(x=213, y=10)
R4.place(x=258, y=10)   #R4.place(x=260, y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text='Yes', variable=exang,
                 value=1, command=selection3)
R6 = Radiobutton(Detail_entry, text="No", variable=exang,
                 value=2, command=selection3)
R5.place(x=387, y=10)   #R5.place(x=387, y=10)
R6.place(x=430, y=10)

### Combobox ###

Label(Detail_entry, text="cp: ", font="arial 11",
      bg=framebg, fg=framefg). place(x=5, y=50)
Label(Detail_entry, text="restecg: ", font="arial 11",
      bg=framebg, fg=framefg). place(x=5, y=90)
Label(Detail_entry, text="slope: ", font="arial 11",
      bg=framebg, fg=framefg). place(x=5, y=130)
Label(Detail_entry, text="ca: ", font="arial 11",
      bg=framebg, fg=framefg). place(x=5, y=170)
Label(Detail_entry, text="thal: ", font="arial 11",
      bg=framebg, fg=framefg). place(x=5, y=210)

# Label(Detail_entry, text="oldpeak: ", font="arial 13",
# width=7, bg=framebg, fg=framefg).place(x=240, y=210)


def selection4():
    input = cp_combobox.get()
    if input == "Typical angina":
        return (0)
    elif input == "Atypical angina":
        return (1)
    elif input == "Non-anginal pain":
        return (2)
    elif input == "Asymptomatic":
        return (3)
    else:
        print(exang)


def selection5():
    input = slope_combobox.get()
    if input == "Upsloping":
        return (0)
    elif input == "Flat":
        return (1)
    elif input == "Downsloping":
        return (2)
    else:
        print(exang)


#-----------------------------------------------Two new combobox---------------------------------------------#
def selection6():
    input = restecg_combobox.get()
    if input == "Normal":
        return (0)
    elif input == "Having ST-T":
        return (1)
    elif input == "Hypertrophy":
        return (2)
    else:
        print(exang)


def selection7():
    input = thal_combobox.get()
    if input == "Normal":
        return (0)
    elif input == "Fixed defect":
        return (1)
    elif input == "Reversable defect":
        return (2)
    else:
        print(exang)
#-----------------------------------------------Two new combobox---------------------------------------------#


cp_combobox = Combobox(Detail_entry, values=['Typical angina', 'Atypical angina',
                       'Non-anginal pain', 'Asymptomatic'], font="arial 12", state="r", width=14)
restecg_combobox = Combobox(
    Detail_entry, values=['Normal', 'Having ST-T', 'Hypertrophy'], font="arial 12", state="r", width=11)        # 'Normal', 'Having ST-T', 'Hypertrophy'    #'0', '1', '2'
slope_combobox = Combobox(Detail_entry, values=[
                          'Upsloping', 'Flat', 'Downsloping'], font="arial 12", state="r", width=12)
ca_combobox = Combobox(Detail_entry, values=[
                       '0', '1', '2', '3'], font="arial 12", state="r", width=14)
thal_combobox = Combobox(Detail_entry, values=[
                         'Normal', 'Fixed defect', 'Reversable defect'], font="arial 12", state="r", width=14)  # 'Normal', 'Fixed defect', 'Reversable defect' #'0', '1', '2'

cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=80, y=90)
slope_combobox.place(x=70, y=130)
ca_combobox.place(x=50, y=170)
thal_combobox.place(x=50, y=210)


### DATA ETRY BOX ###

# font="arial 11, width=7

Label(Detail_entry, text="Smoking: ", font="arial 11",
      width=11, bg="#dbe0e3", fg="black"). place(x=240, y=50)
Label(Detail_entry, text="trestbps(mm): ", font="arial 11",
      width=11, bg=framebg, fg=framefg). place(x=240, y=90)
Label(Detail_entry, text="chol(mg/dl): ", font="arial 11",
      width=11, bg=framebg, fg=framefg). place(x=240, y=130)
Label(Detail_entry, text="thalach(max): ", font="arial 11",
      width=11, bg=framebg, fg=framefg). place(x=240, y=170)
Label(Detail_entry, text="oldpeak(0-3.0): ", font="arial 11",
      width=11, bg=framebg, fg=framefg).place(x=240, y=210)


trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(Detail_entry, textvariable=trestbps,
                       width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
chol_entry = Entry(Detail_entry, textvariable=chol, width=10,
                   font="arial 15", bg="#ededed", fg="#222222", bd=0)
thalach_entry = Entry(Detail_entry, textvariable=thalach,
                      width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak,
                      width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)

# x=320
trestbps_entry.place(x=350, y=90)
chol_entry.place(x=350, y=130)
thalach_entry.place(x=350, y=170)
oldpeak_entry.place(x=350, y=210)


### Analysis Image ###
# Need to edit pictures

square_report_image = PhotoImage(file="Images/report1.png")   #Images/doc220x330.png  #Images/report1.png
report_background = Label(image=square_report_image, bg=background)
report_background.place(x=1120, y=320)         # x=1120,y=340
report = Label(mroot, font="arial 25 bold", bg="white", fg="#8dc63f")
report.place(x=1170, y=550)
report1 = Label(mroot, font="arial 10 bold", bg="white")
report1.place(x=1130, y=610)


### Analysis Button ###

analysis_button = PhotoImage(file="Images/button220x60.png")
Button(mroot, image=analysis_button, bd=0, bg=background,
       cursor='hand2', command=analysis). place(x=1120, y=240)


### GRAPH ###
# Need to edit pictures

graph_image = PhotoImage(file="Images/graph220x220.png")
Label(image=graph_image).place(x=600, y=270)
Label(image=graph_image).place(x=860, y=270)
Label(image=graph_image).place(x=600, y=500)
Label(image=graph_image).place(x=860, y=500)


### info button ###

info_button = PhotoImage(file="Images/info25x25.png")
Button(mroot, image=info_button, bd=0, bg=background,
       cursor='hand2', command=Info). place(x=10, y=240)


### save button ###

save_button = PhotoImage(file="Images/save40x40.png")
Button(mroot, image=save_button, bd=0, bg=background,
       cursor='hand2', command=save). place(x=1370, y=250)


### Smoking and Non smoking Button ###
button_mode = True
choice = "smoking"


def changemode():
    global button_mode
    global choice
    if button_mode:
        choice = "non_smoking"
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode = False
    else:
        choice = "smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = True

    print(choice)


smoking_icon = PhotoImage(file="Images/smoker.png")        #Images/smoker35x35.png
non_smoking_icon = PhotoImage(file="Images/non-smoker.png")        #Images/non-smoker35x35.png
mode = Button(mroot, image=smoking_icon, bg="#dbe0e3",
              bd=0, cursor="hand2", command=changemode)
mode.place(x=350, y=495)


### LogOut Button ###

logout_icon = PhotoImage(file="Images/restart35x35.png")     #logout35x35.pn
logout_button = Button(mroot, image=logout_icon,
                       bg="#df2d4b", cursor="hand2", bd=0, command=logout)
logout_button.place(x=1390, y=87)   #x=1390, y=60


mroot.mainloop()