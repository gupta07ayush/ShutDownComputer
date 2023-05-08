from tkinter import Tk, Button, Entry
import os

root = Tk()
root.title("ShutDown")
root.geometry('600x600')
root.config(bg='#ffba08')


def restart():
    os.system('shutdown /r /t 1')


def restart_in():
    time = timer.get()
    os.system('shutdown /r /t time')


shutdown = Button(root, text="ShutDown", bg="#9d0208", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised')
shutdown.place(x=150, y=100, width=200, height=50)

logout = Button(root, text="Log out", bg="#9d0208", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised')
logout.place(x=150, y=200, width=200, height=50)

restart = Button(root, text="Restart", bg="#9d0208", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised', command=restart)
restart.place(x=150, y=300, width=200, height=50)

restart_in = Button(root, text="Restart  in ", bg="#9d0208", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised', command=restart_in)
restart_in.place(x=150, y=400, width=200, height=50)

timer = Entry(root, bg="#ffd000", fg='black', font=(
    'arial', 20, 'bold'), border=7, relief='raised')
timer.place(x=380, y=401, width=60, height=48)
timer.insert(0, '10')
timer.focus_set()

root.mainloop()
