# --------------------------------------
# *ARGS:- You can give positional arguments as much as you want, Return a tuple of elements. 
# ======

# def sum(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum

# result = sum(1,2,3,4,5,6,7,8,9,10)
# print(result)

# KWARGS:- You can give keyword argument as much as you want, Return a dictionary.
# =======

# def calculate(n,**kwargs):
    # print(kwargs)
    # print(kwargs['add'])
    # print(kwargs['multiply'])
    # n += kwargs['add']
    # n *= kwargs['multiply']
    # print(n)

# calculate(2,add=3,multiply=5)
# ---------------------------------------


# TKINTER MODULE IN PYTHON:-
#=========================

from email.mime import image
import tkinter

# WINDOW:

window = tkinter.Tk()
# window.title('My First GUI')
# window.minsize(width=500,height=500)

# LABEL:

# my_label = tkinter.Label(text='I am a Label',font=('Arial',24),bg='yellow')
# my_label['text'] = 'NEW' # You can change the text using the key of kwargs.
# my_label.config(text='NEW TEXT') # you can also used config method to change the text.
# my_label.pack()

# BUTTON:

# def button_clicked():
#    my_label.config(text='Button Was Clicked!')

# button = tkinter.Button(text='Click Me',command=button_clicked)
# button.pack()

# ENTRY:

# input = tkinter.Entry(width=30)
# input.pack()

# def clicked():
#     my_label.config(text=input.get())
# button.config(command=clicked)    

# PACK ---> align elements automatically in an organized format normally starts from top to bottom.
# PLACE ---> align the elements using x and y positions.
# GRID ---> align the elements using grid of columns and rows. 
# label = tkinter.Label(text="This is a Label",font=('Arial',18))
# btn = tkinter.Button(text='Click Me')
# inp = tkinter.Entry()

# label.pack()
# btn.pack()
# inp.pack()

# label.place(x=0,y=0)
# btn.place(x=100,y=100)
# inp.place(x=200,y=200)

# label.grid(column=0,row=0)
# btn.grid(column=1,row=1)
# inp.grid(column=2,row=2)

# MILES TO METER CONVERTER PROGRAM:-
#======================================

# def miles_to_km():
#     miles = float(input.get())
#     km = round(miles * 1.609)
#     km_lable.config(text=km)

# window.title('Miles to Km Converter')
# window.config(padx=20,pady=20)
# button = tkinter.Button(text='Calculate',command=miles_to_km)
# input = tkinter.Entry()
# miles_lable = tkinter.Label(text='Miles')
# equal_to_lable = tkinter.Label(text='is equal to')
# km_lable = tkinter.Label(text='0')
# km_lable_text = tkinter.Label(text='Km')

# input.grid(column=1,row=0)
# miles_lable.grid(column=2,row=0)
# equal_to_lable.grid(column=0,row=1)
# km_lable.grid(column=1,row=1)
# km_lable_text.grid(column=2,row=1)
# button.grid(column=1,row=2)


# BMI CALCULATOR:-
# =================

# def bmi_calc():
#     width = float(w.get())
#     height = float(h.get()) 
#     bmi = round(width / height ** 2,2)
#     bmi_value.config(text=bmi)

# window.title('BMI Calculator')
# window.config(padx=100,pady=100)
# w = tkinter.Entry(width=30)
# h = tkinter.Entry(width=30)
# width_text = tkinter.Label(text='Width in Kg:',font=('Arial',11,'bold'))
# height_text = tkinter.Label(text='Height in Meter:',font=('Arial',11,'bold'))
# btn = tkinter.Button(text='Calculate',font=('Helvetica',12,'bold'),command=bmi_calc)
# bmi_text = tkinter.Label(text='BMI:',font=('Courier',15,'bold'))
# bmi_value = tkinter.Label(text='0',font=('Courier',15,'bold'))
# width_text.grid(column=0,row=0)
# height_text.grid(column=0,row=1)
# w.grid(column=1,row=0)
# h.grid(column=1,row=1)
# btn.grid(column=1,row=2)
# bmi_text.grid(column=0,row=3)
# bmi_value.grid(column=1,row=3)


# Pomodoro App:-
# =============

# ---------- CONSTANTS ------------
BG = '#fcfce3'                   
FONT = 'Courier'  
GREEN = '#32CD32' 
WORK_MIN = 1
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20  
reps = 0    
timer = None

# --------------- RESET TIMER -----------------

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text='00:00')
    title_lable.config(text='Timer')
    check_mark.config(text='')

# ---------------------------------------------

# ---------------------------------

# ----------- TIMER MECHANISM -----------
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text='Break',fg='red')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lable.config(text='Break',fg='pink')
    else:
        count_down(work_sec)
        title_lable.config(text='Work',fg=GREEN)


# -------------------------------------------

# ----------- COUNTDOWN MECHANISM -----------
import math

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(canvas_text,text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        check_mark.config(text=marks)

# -------------------------------------------

# ----------- UI SETUP ---------------

window.config(padx=100,pady=100,bg=BG)
window.title('Pomodoro')
canvas = tkinter.Canvas(width=225,height=225,bg=BG,highlightthickness=0)
heart_image = tkinter.PhotoImage(file='C:\\Users\\Laptop Valley\\Desktop\\PYTHON MODULES\\heart.png')
canvas.create_image(112,112,image=heart_image)
canvas_text = canvas.create_text(112,112,text='00:00',fill='white',font=(FONT,20,'bold'))
canvas.grid(column=1,row=1)

title_lable = tkinter.Label(text='Timer',font=(FONT,'50'),fg=GREEN,bg=BG)
title_lable.grid(column=1,row=0)


start_button = tkinter.Button(text='Start',bg=BG,highlightthickness=0,command=start_timer)
reset_button = tkinter.Button(text='Reset',bg=BG,highlightthickness=0,command=reset_timer)
start_button.grid(column=0,row=2)
start_button.config(padx=20,pady=2)
reset_button.grid(column=2,row=2)
reset_button.config(padx=20,pady=2)

check_mark = tkinter.Label(fg=GREEN,font=(FONT,12),bg=BG)
check_mark.grid(column=1,row=3)

# ------------------------------------------



window.mainloop()
