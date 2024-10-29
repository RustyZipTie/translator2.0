import tkinter as tk
from tkinter import  ttk

from language.Dictionary import Dictionary


class DictionaryWidget(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.to_wylie = Dictionary("./json-data/tibetan-wylie.json")
        self.translator = Dictionary(data_location="./json-data/dictionaries.json", pre_processing=self.to_wylie.define)

        self.def_text = tk.StringVar(self, value="Enter a tibetan term above")

        self.enter_text = ttk.Entry(self)
        self.enter_text.pack(expand=True)

        self.enter_text.bind("<KeyRelease>", self.define)

        self.definition = ttk.Label(self, textvariable=self.def_text, wraplength=400)
        self.definition.pack(expand=True)


    def define(self, event):
        tibetan = self.enter_text.get()
        self.def_text.set(self.translator.define(tibetan))
        self.definition.update()

