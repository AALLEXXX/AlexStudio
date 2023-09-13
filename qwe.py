import tkinter as tk
from tkinter import PhotoImage

def button_click():
    label.config(text="Кнопка нажата")

root = tk.Tk()

# Загрузка изображения
image = PhotoImage(file='img_but/play.png')

# Создание кнопки с изображением
button = tk.Button(root, image=image, command=button_click)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
