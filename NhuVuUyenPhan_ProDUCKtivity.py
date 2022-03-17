from tkinter import *
import tkinter.messagebox
import pickle
import time
from playsound import playsound

#### NOTE: To start program, enter in terminal: #####
#### py NhuVuUyenPhan_ProDUCKtivity.py (WINDOWS) #####
#### python NhuVuUyenPhan_ProDUCKtivity.py (Mac) #####
# To-do List Window
class TodoList:

    def __init__(self, main):
        #Displays of the pop-up window
        self.main = main
        self.main.geometry('400x600') #sets the default size of the window

        #Displays "To-do List" title
        self.list_label = Label(main, text="TO-DO LIST", font="helvetica 25")

        #Creates an empty list to store tasks in
        self.todo_list = []

        #Creates listbox widget to display tasks
        self.tasks_listbox = Listbox(main, height=20, width=50, bg="LemonChiffon2", font= "helvetica")
        self.tasks_listbox.pack()

        #Creates a typable space for user entry
        self.enter_task = Entry(main, width=50, bd= "2", bg="DodgerBlue4",fg="white")
        self.enter_task.pack()

        #Creates a button for user to add task into To-do list
        self.add_task_button = Button(main, text="Add task", width=30, command=self.add_task, bg="DarkSlategray4",highlightbackground="DarkSlategray4")
        self.add_task_button.pack()

        #Button to delete task upon selection
        self.delete_task_button = Button(main, text="Delete task", width=30, command=self.delete_task, bg="DarkSlategray4", highlightbackground="DarkSlategray4")
        self.delete_task_button.pack()

        #Button that, upon selecting a task, leads to a timer for user to start their focus session.
        self.timer_button = Button(main, text="Focus Timer", width=30, bg="DarkSlategray4", highlightbackground="DarkSlategray4", command=lambda: self.to_timer(Timer)) #calls the countdown timer window to pop up
        self.timer_button.pack()

        #Button to clear all tasks
        self.clear_tasks_button = Button(main, text="Clear list", width=30, bg="DarkSlategray4", highlightbackground="DarkSlategray4", command=self.clear_tasks)
        self.clear_tasks_button.pack()

        #Button to save tasks in current to-do list
        self.save_tasks_button = Button(main, text="Save list",highlightbackground="DarkSlategray4", bg="DarkSlategray4", width=30, command=self.save_tasks)
        self.save_tasks_button.pack()

        #Loads saved tasks to to-do list after clearing list
        self.load_tasks_button = Button(main, text="Load recent list", width=30, bg="DarkSlategray4", highlightbackground="DarkSlategray4",command=self.load_tasks)
        self.load_tasks_button.pack()

    #Updates the listbox whenever any addition or deletion to self.todo_list is made.
    def update_list(self):
        self.tasks_listbox.delete(0, END)
        for task in self.todo_list:
            self.tasks_listbox.insert(END, task)

    #Function for "add task" button command. Adds user entry onto to-do list
    def add_task(self):
        task = self.enter_task.get()
        if task != "":
            self.todo_list.append(task)
            self.update_list()
            self.enter_task.delete(0, END)
        else:
            tkinter.messagebox.showwarning(title="QUACK!", message="Task cannot be empty!")

    #Deletes a cursor selected task.
    def delete_task(self):
        try:
            task = self.tasks_listbox.get(self.tasks_listbox.curselection()[0])
            if task in self.todo_list:
                self.todo_list.remove(task)
                self.update_list()
        except:
            tkinter.messagebox.showwarning(title="QUACK!", message="Must select a task to delete!")

    #Leads to timer page
    def to_timer(self, _class):
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = Toplevel(self.main)
            _class(self.new)

    #Clears current to-do list
    def clear_tasks(self):
        del self.todo_list[:]
        self.update_list()

    #Saves current to-do list
    def save_tasks(self):
        all_tasks = self.todo_list[0:len(self.todo_list)]
        pickle.dump(all_tasks, open('savedtasks.dck', 'wb'))


    #Loads recently saved to-do list after closing and reopening application
    def load_tasks(self):
        self.clear_tasks()
        with open('savedtasks.dck', 'rb') as pickle_file:
            self.todo_list = pickle.load(pickle_file)
            for task in self.todo_list:
                self.tasks_listbox.insert(END, task)


# Countdown Timer Window
class Timer:

    def __init__(self, main):

        #Display of the window
        print(mainpage.new.state())
        self.main = main
        self.main.geometry('400x500') #sets the default size of the window
        self.main.maxsize(400, 500)
        self.main.minsize(400, 500)

        #Displays "To-do List" title
        self.list_label = Label(main, text="Countdown Timer", font="helvetica 30")
        self.list_label.pack()

        #Frame of the time list
        self.my_frame= Frame(main)
        self.my_frame.pack()

        #Box with list of time
        self.time_listbox = Listbox(self.my_frame, bg="LemonChiffon2", width=25, height=13)
        self.time_listbox.pack(side=LEFT, fill=BOTH)

        #List containing time intervals
        self.time_list = ["1","5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60"]
        for item in self.time_list:
            self.time_listbox.insert(END, item)

        #Display of "00" seconds
        self.second = StringVar()
        self.second.set("00")
        self.seconds_entry = Entry(self.main, width = 2, font="helvetica 30", bg="DodgerBlue4", textvariable = self.second, fg="white")
        self.seconds_entry.place(x = 227, y = 275)

        #Display of "00" minutes
        self.minute = StringVar()
        self.minute.set("00")
        self.minute_entry = Entry(self.main, width = 2, font="helvetica 30", bg="DodgerBlue4", textvariable = self.minute, fg="white")
        self.minute_entry.place(x = 177, y = 275)

        #Display of "00" hours
        self.hour = StringVar()
        self.hour.set("00")
        self.hour_entry = Entry(self.main, width = 2, font="helvetica 30", bg="DodgerBlue4", textvariable = self.hour, fg="white")
        self.hour_entry.place(x = 127, y = 275)

        #Labeling where hour, minute, and second are underneath the timer
        self.display_label = Label(self.main, text = "   hour    minute   second",  bg="DarkSlategray4")
        self.display_label.place(x=132, y=330)

        #Button SELECT
        self.button_select= Button(self.main, text= "SELECT", highlightbackground="DarkSlategray4", font= "helvetica 10", width=10, bd="10", command=self.select, bg="DarkSlategray4")
        self.button_select.place(x=150, y=360)

        #Button START
        self.button_start = Button(self.main, text = "START", highlightbackground="DarkSlategray4", font= "helvetica 10", width=10, bd= "10", bg="red", command=self.countdown)
        self.button_start.place(x=150, y=400)

        #Button EXIT
        self.button_exit = Button(self.main,  bg="DarkSlategray4", highlightbackground="DarkSlategray4", text = "EXIT", font= "helvetica 10", width=10, bd= "10", command=self.exit_timer)
        self.button_exit.place(x=150, y=440)

        #Select time to put into the timer
    def select(self):
        selected_time = self.time_listbox.get(self.time_listbox.curselection()[0])
        if selected_time != '60':
            self.hour.set('00')
            self.minute.set(selected_time)
            self.second.set('00')
        else:
            self.hour.set('01')
            self.minute.set('00')
            self.second.set('00')

        #Start the timer to count down the selected time
    def countdown(self):

        times = int(self.hour.get())*3600+ int(self.minute.get())*60 + int(self.second.get())
        while times > -1:
            minute, second = (times // 60 , times % 60)

            hour = 0
            if minute >= 60:
                hour , minute = (minute // 60 , minute % 60)

            self.second.set("{0:02d}".format(second))
            self.minute.set("{0:02d}".format(minute))
            self.hour.set("{0:02d}".format(hour))

            self.main.update()
            time.sleep(1)
            times -= 1

            if times == 0:
                playsound("quack.mp3")
                tkinter.messagebox.showinfo(title="QUACK!", message="Congratulations! You should take a break now!")
                self.second.set('00')
                self.minute.set('00')
                self.hour.set('00')

        #Exit countdown timer window to go back to to-do list
    def exit_timer(self):
        self.main.destroy()


main = Tk()
mainpage = TodoList(main)
icon = PhotoImage(file = 'icon.png')
mainpage.main.iconphoto(False, icon) #Sets an icon image for application
mainpage.main.title("ProDUCKtivity")
main.mainloop()
