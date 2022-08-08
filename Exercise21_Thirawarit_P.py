from cProfile import label
from tkinter import *
from math import *

def leftClickButton(event) :
    result = float(textBoxWeight.get())/pow(float(textBoxHight.get())/100,2)
    if result <= 18.5 :
        labelResult.configure(text="ผอมเกินไป")
    elif 18.6 <= result <= 22.9 :
        labelResult.configure(text="น้ำหนักปกติเหมาะสม")
    elif 23.0 <= result <= 24.9 :
        labelResult.configure(text="น้ำหนักเกิน")
    elif 25.0 <= result <= 29.9 :
        labelResult.configure(text="อ้วน")
    else :
        labelResult.configure(text="อ้วนมาก")
MainWindow = Tk()
labelHight = Label(MainWindow,text= "ส่วนสูง (cm.)").grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text= "น้ำหนัก (kg.)").grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text= "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text= "ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()