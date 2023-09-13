from tkinter import *
from structural.decorator import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Decorator")
        self.geometry('640x480')
        self.configure(bg='lightblue')
        self.dry = Entity('sound')

        l = Label(self, bg='black', width=30, text=self.dry.play())
        l.pack()

        def result():
            actions = {
                (1, 0): (Compressor, self.dry),
                (0, 1): (EQ, self.dry),
                (1, 1): (EQ, Compressor(self.dry)),
            }

            action = actions.get((comp.get(), eq.get()), (Entity, self.dry.play()))
            wet = action[0](action[1])
            l.config(text=wet.play())


        comp = IntVar(value=0)
        eq = IntVar(value=0)
        first = Checkbutton(self, text='Compressor', variable=comp, command=result)
        first.pack()
        second = Checkbutton(self, text='EQ', variable=eq, command=result)
        second.pack()
