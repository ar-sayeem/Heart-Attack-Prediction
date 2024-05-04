from tkinter import *

icon_window=Tk()
icon_window.title("Info")
icon_window.geometry("700x600+400+100")


### icon_image ###

icon_image=PhotoImage(file="Images/info25x25.png")
icon_window.iconphoto (False, icon_image)


### Heading ###

Label(icon_window, text="Information Related to dataset", font="robot 19 bold").pack (padx=20, pady=20)


### info ###

Label(icon_window,text="age      - age in years",font="arial 11").                                                                                      place(x=20,y=100)
Label(icon_window,text="sex      - sex (1 = male; 0 = female",font="arial 11").                                                                         place(x=20,y=130)
Label(icon_window,text="cp       - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)",font="arial 11"). place(x=20,y=160)
Label(icon_window,text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").                                    place(x=20,y=190)
Label(icon_window,text="chol     - serum cholestoral in mg/dl",font="arial 11").                                                                        place(x=20,y=220)
Label(icon_window,text="fbs      - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)",font="arial 11").                                             place(x=20,y=250)
Label(icon_window,text="restecg  - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)",font="arial 11").               place(x=20,y=280)
Label(icon_window,text="thalach  - maximum heart rate achieved",font="arial 11").                                                                       place(x=20,y=310)
Label(icon_window,text="exang    - exercise induced angina (1 = yes; 0 = no)",font="arial 11").                                                         place(x=20,y=340)
Label(icon_window,text="oldpeak  - ST depression induced by exercise relative to rest",font="arial 11").                                                place(x=20,y=370)
Label(icon_window,text="slope    - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)",font="arial 11").              place(x=20,y=400)
Label(icon_window,text="ca       - number of major vessels (0-3) colored by flourosopy",font="arial 11").                                               place(x=20,y=430)
Label(icon_window,text="thal     - 0 = normal; 1 = fixed defect; 2 = reversable defect",font="arial 11").                                               place(x=20,y=460)


icon_window.mainloop()