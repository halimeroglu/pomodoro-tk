import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Pomodoro')
root.geometry('350x400')
root.config(bg='#fab1a0')

minute = StringVar()
second = StringVar()

minute.set("00")
second.set("00")

minute_entry = Entry(root,width=3,font=('Arial',14),textvariable=minute).place(x=125, y=90)
second_entry = Entry(root,width=3,font=('Arial',14),textvariable=second).place(x=175, y=90)


def countdown():
    t = 25 * 60

    while t > -1:
        mins, secs = divmod(t, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        time.sleep(1)
        root.update()
        if (t == 0):
            messagebox.showinfo(title="Time's up ", message="Take a break")
            time.sleep(5 * 60)
            messagebox.showinfo(title="Time's up ", message="Go to work")
        t -= 1



title_label = Label(root, text='POMODORO', font=('Arial', 18, 'bold'), fg='#d63031', bg='#fab1a0').place(x=100, y=30)
start_button = Button(root, text='Start', font=('Arial', 14), width=18, command=countdown).place(x=75, y=150)

root.mainloop()