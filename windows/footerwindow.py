from tkinter import *
from creational.factorymethod import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Footer bar')
        self.geometry('1280x200')
        self.configure(bg='lightblue')

        self.entry = Entry(self, width=15, textvariable=StringVar(),highlightbackground='lightblue' )
        self.entry.pack()

        self.button = Button(self, text='Drug plugin here', command=self.show_plugin,highlightbackground='lightblue')
        self.button.pack(expand=True)

    def show_plugin(self):
        drop = self.entry.get()
        effect = Creator().Factory(drop)
        if effect:
            l = Label(self, text= f'You dropped {effect.type}')
            l.pack()