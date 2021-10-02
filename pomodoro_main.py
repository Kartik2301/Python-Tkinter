from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
checkmarks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global checkmarks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks = ""
    checkmark_lable.config(text=checkmarks)
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global  reps
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title_label.config(text="Working", fg=GREEN)
    else:
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text="Break", fg=RED)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text="Break", fg=PINK)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global checkmarks, timer
    count_mins = count // 60
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_seconds}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 1:
            checkmarks += "✔"
            checkmark_lable.config(text=checkmarks)
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "normal"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_lable = Label(fg=GREEN, font=(FONT_NAME, 11, "normal"))
checkmark_lable.grid(row=3, column=1)










window.mainloop()