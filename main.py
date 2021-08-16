# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:31:33 2021

@author: annice

Description: According to the Vision Council, 75% of adults use glasses 
or contact lenses. Staring at computer, smartphone and other digital screens 
is known to play an important factor in permanently damaging you eyes and 
increasing the need to use corrective glasses or contact lenses. It is 
suggested that after looking at digital screens for 20 minutes you take a 20 
second break to look 20 meters away. 
In the following program we make an application that warns you every 20 mins
to look 20 meters away for 20 secs. The application lets you know when 20 mins
or 20 secs has passed by showing a message using the messagebox module. 
"""

###############################SOLUTION#####################################

import math
import tkinter
from tkinter import messagebox
# ---------------------------- Constants ------------------------------- #
#The color scheme has been defined for you below. Feel free to play around 
#with it later. You can explore other color schemes on colorhunt.co

TEAL = "#79A3B1"
LIGHTTEAL = "#D0E8F2"
DARKTEAL = "#456268"
BEIGE = "#FCF8EC"
GREEN = "#7FC8A9"
FONT_NAME = "Atkinson"
WORK_MIN = 20
SHORT_BREAK_SEC = 20
# ---------------------------- Variables ------------------------------- #
reps=0
timer = None
# ---------------------------- write a function for resetting timer below ------------------------------- # 
def reset_timer():
    '''
    Returns nothing. Changes the text shown on the top to "Timer" and sets the 
    timer equal to 00:00.
    
    '''
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0
    my_label.config(text="Timer", fg=DARKTEAL)
# ---------------------------- write a function to start the timer below------------------------------- # 
def start_btn_clicked():
    '''
    Returns nothing. Changes the text shown on the top to either "Work" or 
    "Break! Look Away" and calls the count_down function.
    
    '''
    global reps 
    reps = reps + 1
    short_break_sec = SHORT_BREAK_SEC 
    work_sec = WORK_MIN * 60
    
    
    
    if not reps%2 == 0:
      my_label.config(text="Work", fg=DARKTEAL) 
      count_down(work_sec)
      if reps>1:
          messagebox.showinfo(title="Warning", message="Get back to work!")
    else:
      messagebox.showinfo(title="Warning", message="Please look 20 meters away!")
      my_label.config(text="Break! Look Away", fg=TEAL)  
      count_down(short_break_sec)
      
# ---------------------------- write a function for counting down ------------------------------- # 
def count_down(count):
    '''
    Returns nothing. Changes the text showing the time remaining. 

    Parameters:
        count (int):The string which is to be reversed.
  
    '''
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_min = format(count_min, '02d')
    count_sec = format(count_sec, '02d')
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}") 
    if count >0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_btn_clicked()
# ---------------------------- UI ------------------------------- #

window = tkinter.Tk()

window.title("20:20:20 Rule")
window.config(padx=50, pady=10, bg=BEIGE)
window.iconbitmap("favicon.ico")

canvas = tkinter.Canvas(width = 600, height = 450, bg=BEIGE, highlightthickness=0)
eye_img =tkinter.PhotoImage(file ="iris.png")
canvas.create_image(300, 300, image =eye_img)
timer_text = canvas.create_text(300, 290, text="00:00", fill='red', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


my_label = tkinter.Label(text = "Timer", font=(FONT_NAME, 40, "bold"), fg=DARKTEAL, bg=BEIGE)
my_label.grid(row=0, column=1)


start_btn = tkinter.Button(text="Start", highlightthickness=0, command=start_btn_clicked)
start_btn.grid(row=2, column=0)

reset_btn = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)


window.mainloop()


'''

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNN+/++++++++++++++++++++++++++/+NNNNNNNNNN
NNNNNNNNNN. .........................```NNNNNNNNNN
NNNNNNNNNN.     ``````   .. ``````   .-`NNNNNNNNNN
NNNNNNNNNN.    `hhhhhh`  .-`hhhhhh   `-`NNNNNNNNNN
NNNNNNNNNN:....-mNNNNN`  .-`NNNNNm-----:NNNNNNNNNN
NNNNNNNNNNyyyyyymNNNNN`  .-`NmyyyydNNNNdyyyymNNNNN
NNNNNNNNNN-    `mNNNNN`  .-`Nd    -mNNd.    hNNNNN
NNNNNNNNNNo    :mNNNNN`  .-`Nmy    -mm.    ymNNNNN
NNNNNNNNNy  -+  +NNNNN`  .-`NNh  .  --  .  dNNNNNN
NNNNNNNNh`  .-   sNNNN`  .-`NNh  /s    y/  dNNNNNN
NNNNNNNd. `////. `hNNN`  .-`NNh  /ms  sm/  dNNNNNN
NNNNNm:.  `dmmm-  `-hN`  .-`Nd-  `+mosmo`  -dNNNNN
NNNNNm/////dNNN/////hN`  .-`Nd////oNmmNo////dNNNNN
NNNNNNmmmmmNNNNmmmmooo`  .- ooodmmmNNNNmmmmmNNNNNN
NNNNNNNNNNNNNNNNNNd      ``  . hNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNd          . hNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNd++++++++++++dNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

Fall 2021
'''










