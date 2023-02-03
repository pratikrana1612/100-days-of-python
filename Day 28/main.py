from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1
    if (reps % 8 == 0):
        title.config(text='BREAK', fg=RED)
        count_down(long_break_sec)
    elif (reps % 2 == 0):
        title.config(text='BREAK', fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text='WORK', fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title['text']='Timer'
    check_mark.config(text='')
    global reps
    reps=0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro ")
window.config(padx=100, pady=50, bg=YELLOW)


def count_down(count):
    if (count < 0):
        if (reps % 2 == 0):
            marks = ''
            for _ in range(int(reps/2)):
                marks += '✔'
            check_mark.config(text=marks)
        start_timer()
        return
    count_min = math.floor(count/60)
    count_sec = count % 60
    if (count_sec <= 9):
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    global timer
    timer=window.after(1000, count_down, count-1)


# def say_something(something):
#     print(something)
# window.after(1000,say_something,"Hello")

title = Label(text="Timer", bg=YELLOW, foreground=GREEN,
              font=(FONT_NAME, 34, 'bold'))
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tommato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tommato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
# count_down(5)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="reset", highlightthickness=0,command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark = Label(text='', fg=GREEN, bg=YELLOW, padx=20, pady=20)
check_mark.grid(row=2, column=1)
window.mainloop()
