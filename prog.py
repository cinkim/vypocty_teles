import tkinter as tk
from tkinter import ttk, StringVar,  N, E, W
from tkinter import NO, VERTICAL
import tkinter.messagebox
from tkinter import messagebox

import vzorce

class Vzorecky:

    def __init__(self):
        ...


class VzoreckyGUI(tk.Frame):

    def __init__(self, parent, Vzorecky):
        super().__init__(parent)
        self.parent = parent
        self.Vzorecky = Vzorecky
        self.parent.title("Seznam vzorečků")
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_nabidku()

    def create_nabidku(self):      

        self.nabidka = tk.LabelFrame(root, text="Nabídka tvarů", font="Arial 11")
        self.nabidka.grid(row=1, column=1, sticky=N)

        self.D2 = tk.Radiobutton(self.nabidka, indicatoron=0, text="2 D", command=self.D2_objekty, width = 30)
        self.D2.grid(row=2, column=0, sticky=W)

        self.D3 = tk.Radiobutton(self.nabidka, indicatoron=0, text="3 D", command=self.D3_objekty, width = 30)
        self.D3.grid(row=2, column=1, sticky=W)
        self.mez1 = tk.Label(root)
        self.mez1.grid(row=3, column=0)


    def D2_objekty(self):
        try:
            self.D3_tvary.destroy()
        except AttributeError:
            pass
        self.D2_tvary = tk.LabelFrame(root, text="2D tvary", font="Arial 9")
        self.D2_tvary.grid(row=4, column=1, sticky=N)

        self.ctverec = tk.Radiobutton(self.D2_tvary, indicatoron=0, text="Čtverec", command=self.ctverec, width = 30)
        self.ctverec.grid(row=5, column=0, sticky=N)
        self.obdelnik = tk.Radiobutton(self.D2_tvary, indicatoron=0, text="Obdélník", command=self.obdelnik, width = 30)
        self.obdelnik.grid(row=5, column=1, sticky=N)


    def D3_objekty(self):
        try:
            self.D2_tvary.destroy()
        except AttributeError:
            pass
        self.D3_tvary = tk.LabelFrame(root, text="3D tvary", font="Arial 11")
        self.D3_tvary.grid(row=4, column=1, sticky=N)

        self.krychle = tk.Radiobutton(self.D3_tvary, indicatoron=0, text="Krychle", command=self.krychle, width = 30)
        self.krychle.grid(row=5, column=0, sticky=N)
        self.kvadr = tk.Radiobutton(self.D3_tvary, indicatoron=0, text="Kvádr", command=self.kvadr, width = 30)
        self.kvadr.grid(row=5, column=1, sticky=N)

    def ctverec(self):
        vzorce.ctverec(self)

    def obdelnik(self):
        vzorce.obdelnik(self)

    def krychle(self):
        vzorce.krychle(self)

    def kvadr(self):
        vzorce.kvadr(self)


    def on_close(self):
       self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    Vzorecky = Vzorecky()
    app = VzoreckyGUI(root, Vzorecky)
    app.mainloop()


