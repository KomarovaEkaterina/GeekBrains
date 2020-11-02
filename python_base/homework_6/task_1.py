from itertools import cycle
from tkinter import *


class TrafficLights(Frame):
    __colors = cycle(['red', 'white', 'white', 'white'])
    __colors_1 = cycle(['red', 'white', 'white', 'white'])
    __colors_2 = cycle(['white', 'yellow', 'white', 'yellow'])
    __colors_3 = cycle(['white', 'white', 'green', 'white'])
    __time_waiting = cycle([7000, 2000])

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Traffic Lights")
        self.grid()

        self.canvas = Canvas(self, width=300, height=400, bg="lightblue")
        self.canvas.grid(row=0, column=0)
        self.canvas.create_rectangle(100, 50, 200, 350, fill="black")

        self.first = self.canvas.create_oval(100, 50, 200, 150, fill='white')
        self.second = self.canvas.create_oval(100, 150, 200, 250, fill='white')
        self.third = self.canvas.create_oval(100, 250, 200, 350, fill='white')

    def running(self):
        self.canvas.itemconfig(self.first, fill=next(self.__colors_1))
        self.canvas.itemconfig(self.second, fill=next(self.__colors_2))
        self.canvas.itemconfig(self.third, fill=next(self.__colors_3))
        self.canvas.after(next(self.__time_waiting), self.running)

        mainloop()


a = TrafficLights()
a.running()

