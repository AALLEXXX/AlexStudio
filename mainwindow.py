from tkinter import *
from tkinter import ttk
from creational.singleton import Singleton
from tkinter import PhotoImage

from behavior.audio_module import *

from windows import renderwindow, decoratorwindow, eqswindow, \
    footerwindow, converterwindow, iteratorwindow, groupwindow, strategywindow


class Window(Tk, Singleton):
    def init(self):
        super().__init__()
        self.color_top_frame = 'grey'
        self.top_frame = Frame(self, bg=self.color_top_frame)
        self.top_frame.place(x=300, y=0, width=1280, height=100)

        self.color_left_frame = '#696969'
        self.left_frame = Frame(self, bg=self.color_left_frame)
        self.left_frame.place(x=0, y=0, width=300, height=720)

        self.color_frame = '#A9A9A9'
        self.bottom_frame = Frame(self, bg=self.color_frame)
        self.bottom_frame.place(x=300, y=100, width=980, height=620)

        self.eqs_btn_l = Button(self.left_frame, text='open eqs window', command=self.create_window_eqs,
                             highlightbackground=self.color_left_frame)
        self.eqs_btn_l.pack(padx=10, expand=True)

        self.footer_btn_l = Button(self.left_frame, text='open footer', command=self.create_footer_eqs,
                             highlightbackground=self.color_left_frame)
        self.footer_btn_l.pack(padx=10, expand=True)

        self.converter_btn_t = Button(self.top_frame, text='converter', command=self.create_converter_window,
                             highlightbackground=self.color_top_frame)
        self.converter_btn_t.pack(side='left', padx=10, pady=10)

        self.decorator_btn_t = Button(self.top_frame, text='decorator', command=self.create_decorator_window,
                             highlightbackground=self.color_top_frame)
        self.decorator_btn_t.pack(side='left', padx=10, pady=10)

        self.play_image = PhotoImage(file='img_but/play.png')

        self.audio_manager = AudioManager()

        self.load_img = PhotoImage(file='img_but/load.png')

        self.load_btn_t = Button(self.top_frame, text="Load Audio", command=self.audio_manager.load_audio,
                                   bd=0, highlightbackground=self.color_top_frame)
        self.load_btn_t.configure(image=self.load_img,width=50, height=50)
        self.load_btn_t.pack(side='left', padx=10, pady=10)

        self.play_btn_t = Button(self.top_frame, command=self.audio_manager.play_audio,
                                  width=50, height=50, bd=0, highlightthickness=0)
        self.play_btn_t.config(image=self.play_image)
        self.play_btn_t.pack(side='left', padx=10, pady=10)

        self.button_frame = Frame(self.bottom_frame, bg=self.color_frame)
        self.button_frame.pack(side='bottom')

        self.render_btn_b = Button(self.button_frame, text='render', command=self.create_export_window,
                             highlightbackground=self.color_frame)
        self.render_btn_b.pack(side='left', padx=10)

        self.search_btn_b = Button(self.button_frame, text='search', command=self.create_search_window,
                             highlightbackground=self.color_frame)
        self.search_btn_b.pack(side='left', padx=10)

        self.sampler_btn_b = Button(self.button_frame, text='sampler', command=self.create_group_window,
                             highlightbackground=self.color_frame)
        self.sampler_btn_b.pack(side='left', padx=10)

        self.strategy_btn_b = Button(self.button_frame, text='strategy', command=self.create_strategy_window,
                             highlightbackground=self.color_frame)
        self.strategy_btn_b.pack(side='left', padx=10)

        self.change_color_btn_t= Button(self.top_frame, text='white', highlightbackground=self.color_top_frame,
                                       command=self.set_white_theme)
        self.change_color_btn_t.pack(expand=True)
        self.is_white_theme = False

        self.top_buts = [self.play_btn_t, self.load_btn_t, self.converter_btn_t, self.change_color_btn_t, self.decorator_btn_t]
        self.left_buts = [self.footer_btn_l, self.eqs_btn_l]
        self.bottom_buts = [self.strategy_btn_b, self.sampler_btn_b, self.render_btn_b, self.search_btn_b]

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def create_footer_eqs(self):
        global extraWindow
        extraWindow = footerwindow.Extra()

    def create_convertndow(self):
        global extraWindow
        extraWindow = converterwindow.Extra()

    def create_decorator_window(self):
        global extraWindow
        extraWindow = decoratorwindow.Extra()

    def create_export_window(self):
        global extraWindow
        extraWindow = renderwindow.Extra()

    def create_search_window(self):
        global extraWindow
        extraWindow = iteratorwindow.Extra()

    def create_group_window(self):
        global extraWindow
        extraWindow = groupwindow.Extra()

    def create_strategy_window(self):
        global extraWindow
        extraWindow = strategywindow.Extra()

    def create_converter_window(self):
        global extraWindow
        extraWindow = converterwindow.Extra()


    def configure_buttons(self, buttons, color):
        for button in buttons:
            button.configure(
                highlightbackground=color
            )

    def set_white_theme(self):
        if self.is_white_theme:
            self.color_top_frame = 'grey'
            self.color_left_frame = '#696969'
            self.color_bottom_frame = '#A9A9A9'

            self.top_frame.configure(bg=self.color_top_frame)
            self.left_frame.configure(bg=self.color_left_frame)
            self.bottom_frame.configure(bg=self.color_bottom_frame)
            self.button_frame.configure(bg=self.color_bottom_frame)

            self.configure_buttons(self.top_buts, self.color_top_frame)
            self.configure_buttons(self.left_buts, self.color_left_frame)
            self.configure_buttons(self.bottom_buts, self.color_bottom_frame)

            self.is_white_theme = False

        else:
            self.color_top_frame = '#D3D3D3'
            self.color_left_frame = '#C0C0C0'
            self.color_bottom_frame = '#FFFFFF'

            self.left_frame.configure(bg=self.color_left_frame)
            self.top_frame.configure(bg=self.color_top_frame)
            self.bottom_frame.configure(bg=self.color_bottom_frame)
            self.button_frame.configure(bg=self.color_bottom_frame)

            self.configure_buttons(self.top_buts, self.color_top_frame)
            self.configure_buttons(self.left_buts, self.color_left_frame)
            self.configure_buttons(self.bottom_buts, self.color_bottom_frame)

            self.is_white_theme = True

    def __init__(self):
        pass
