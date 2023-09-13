from tkinter import *
from tkinter.messagebox import askquestion
from structural.facade import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('400x720')
        self.title('Render')
        self.configure(bg='lightblue')

        self.button = Button(self, text='Start rendering', command= self.start_rendering)
        self.button.pack(expand=True)

    def start_rendering(self):
        renderTrack = Render()
        askquestion('....', message='Start rendering?')
        renderTrack.startRendering()


