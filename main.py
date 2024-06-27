from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
rep = 0
# ---------------------------- TIMER RESET ------------------------------- #



# ---------------------------- TIMER MECHANISM ------------------------------- # 



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def startTimer():
    global rep
    rep += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    if rep % 2 == 1:
        countDown(work_sec)
        label.config(text="Work",fg=GREEN)

    elif rep == 8:
        countDown(long_break_sec)
        checkLabel["text"] += "✔"
        label.config(text="Finish",fg=PINK)
    elif rep % 2 == 0:
        countDown(short_break_sec)
        checkLabel["text"] += "✔"
        label.config(text="Break",fg=RED)





def countDown(time):
    count_minute = int(time / 60)
    count_second = int(time % 60)
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if time > 0:
        window.after(1000,countDown,time-1)
    else:
        startTimer()
        if rep == 8:
            return

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")

checkLabel = Label(text="",fg=GREEN,bg=YELLOW)
checkLabel.grid(row=4,column=1)

canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(row= 1,column = 1)

label = Label(text="Timer",foreground=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW)
label.grid(row=0,column = 1)

rep = 0
start_button = Button(text="Start", highlightthickness=0,command=startTimer)
start_button.grid(row=2, column = 0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2,column = 2)

label = Label(text="Timer",foreground=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW)
label.grid(row=0,column = 1)


window.mainloop()