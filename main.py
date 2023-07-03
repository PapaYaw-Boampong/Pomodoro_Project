

import tkinter as tk
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
run = True
checkmark = ""
symbol = "✔"
timer_mech = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(timer_mech)
    canvas.itemconfig(timer, text="00:00")
    l1.config(text="Timer", fg=GREEN)
    l2.config(text=" ")
    reps = 0


def end():
    reset()
    l1.config(text="Good Job", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global checkmark
    reps += 1

    if reps == 8:

        checkmark += symbol
        l2.config(text=f"{checkmark}")
        l1.config(text="  Break ", fg=PINK)
        count_down(LONG_BREAK_MIN*60)
        end()

    elif reps % 2 == 0:
       
        checkmark += symbol
        l1.config(text="Break ", fg=RED)
        l2.config(text=checkmark)
        count_down(SHORT_BREAK_MIN*60)

    else:
        l1.config(text="Work",fg=GREEN)
        count_down(WORK_MIN*60)

#---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global timer_mech
    minn = str(count//60)
    sec = str(count % 60)

    if len(sec) == 1:
        sec = "0"+sec
    if len(minn) == 1:
        minn = "0"+minn
    canvas.itemconfig(timer, text=f"{minn}:{sec}")
    if count > 0:
        timer_mech = window.after(1000, count_down, count-1)
    else:

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=75, pady=30, bg=YELLOW)

l1 = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), highlightthickness=0, bg=YELLOW, fg=GREEN)
l1.grid(column=2, row=1)


l2 = tk.Label(font=(FONT_NAME, 15, "bold"), highlightthickness=0, bg=YELLOW, fg=GREEN)
l2.config(pady=10)
l2.grid(column=2, row=4)


canvas = tk.Canvas(width=202, height=223, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 111, image=img)
canvas.grid(column=2, row=2)

timer = canvas.create_text(102, 128, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")

start_button = tk.Button(text="start", font=("Maiandra", 11, "bold"), highlightthickness=0, command=start_timer)
start_button .grid(column=1, row=3)

rest_button = tk.Button(text="reset", font=("Maiandra", 11, "bold"), highlightthickness=0, command=reset)
rest_button.grid(column=3, row=3)


window.mainloop()


"""
░█▀█░█▀█░█░█
░█▀▀░█▀▀░░█░
░▀░░░▀░░░░▀░
"""