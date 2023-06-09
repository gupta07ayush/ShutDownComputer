from tkinter import Tk, Button, Entry
import os

root = Tk()
root.title("ShutDown Computer")
root.geometry('600x600')
root.config(bg='#ffba08')


def shutdown():
    os.system('shutdown /s /t 5')  # shutdown after 5 seconds
    print("System shutdown in 5 seconds......")


def logout():
    os.system('shutdown /l /t 5')  # signout after 5 seconds
    print("System signout in 5 seconds......")


def restart():
    os.system('shutdown /r /t 5')  # restart after 1 seconds
    print("System restart in 5 seconds......")


def restart_in():
    time = timer.get()
    os.system('shutdown /r /t 10')  # restart after 10 seconds
    print("System restart in 10 seconds......")


def abort():
    os.system('shutdown /a')


shutdown = Button(root, text="ShutDown", bg="#9d0208", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised')
shutdown.place(x=150, y=100, width=200, height=50)

logout = Button(root, text="Log out", bg="#9d0208", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised', command=logout)
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

abort = Button(root, text="Abort ", bg="#6a040f", fg='white', font=(
    'arial', 20, 'bold'), border=7, relief='raised', command=abort)
abort.place(x=150, y=500, width=200, height=50)


root.mainloop()
