import tkinter
from tkinter import ttk
import random


class GUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Stand-Up Randomizer')

        window_height = 250
        window_width = 350

        screen_width  = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        style = ttk.Style(self.root)
        self.root.tk.call('source', 'Azure-ttk-theme-main/azure dark/azure_dark.tcl')
        style.theme_use('azure_dark')

        frame1 = ttk.LabelFrame(self.root, text="People")
        frame1.place(x=10, y=10)

        frame2 = ttk.LabelFrame(self.root, text="Results")
        frame2.place(x=95, y=10)

        self.people = sorted(['Stacy', 'Jacob', 'Sean', 'Jeff', 'Laura', 'Edward'])
        self.people_vars = {}

        for i, person in enumerate(self.people):
            self.people_vars[person] = tkinter.IntVar(value=1)
            ttk.Checkbutton(frame1, text=person, variable=self.people_vars[person], offvalue=0, onvalue=1).grid(row=i, sticky=tkinter.W)

        btn = ttk.Button(frame2, text="Randomize", command=self.shuffle_the_things).grid(row=0, sticky=tkinter.W)

        self.txt = tkinter.StringVar()
        self.txt.set("Hello, click to shuffle the team.")
        label = tkinter.Label(frame2, textvariable=self.txt).grid(row=1, sticky=tkinter.W)


    def shuffle_the_things(self):
        enabled_people = []

        for key, value in self.people_vars.items():
            if value.get() == 1:
                enabled_people.append(key)

        new_order = random.sample(enabled_people, len(enabled_people))
        self.txt.set(', '.join(new_order))

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    gui = GUI()
    gui.run()