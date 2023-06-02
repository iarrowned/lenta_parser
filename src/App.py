from src.LentaParser import LentaParser
import tkinter as tk
from tkinter import filedialog


class App:
    def __init__(self, master):
        self.master = master
        master.title('Lenta.ru Parser')
        master.geometry('640x600')

        self.parser = LentaParser()
        cats = self.parser.get_categories()
        self.r_b = tk.StringVar()
        for i in cats:
            tk.Radiobutton(value=i, text=i, variable=self.r_b).pack()

        self.parse_button = tk.Button(master, text='Get news', command=self.parse_news)
        self.parse_button.pack()

    def parse_news(self):
        category = self.r_b.get()
        self.parser.set_category(category)
        self.parser.save_to_file()
        tk.messagebox.showinfo("Success", "Saved in " + self.parser.get_f_name())
