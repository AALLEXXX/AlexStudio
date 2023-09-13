from mainwindow import Window


if __name__ == "__main__":
    handle = Window()
    handle.title('Alexandria')
    handle.geometry('1280x720')
    handle.configure(bg='white')
    handle.mainloop()