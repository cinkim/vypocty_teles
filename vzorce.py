import tkinter as tk
from tkinter import ttk, StringVar,  N, E, W, S, PhotoImage
from tkinter import NO, VERTICAL
from tkinter.constants import NORMAL
import tkinter.messagebox
from tkinter import messagebox


def ctverec(self):
    self.top_ctverec = tk.Toplevel()
    self.top_ctverec.title("Čtverec")
    self.ctverec_foto=PhotoImage(file="obr/ctverec.gif")
    self.ctverec = tk.Label(self.top_ctverec, image=self.ctverec_foto) 
    self.ctverec.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    self.mez_ctverec1 = tk.Label(self.top_ctverec)
    self.mez_ctverec1.grid(row=4, column=0)

    self.Entry_ctverec_strana_a = StringVar()
    self.strana_ctverce_a = ttk.Entry(self.top_ctverec, textvariable=self.Entry_ctverec_strana_a, width=20)
    self.strana_ctverce_a.config(state=NORMAL)
    self.strana_ctverce_a.grid(row=5, column=0)
    self.delka_strany_ctverce = tk.Label(self.top_ctverec, text="Zadej délku strany čtverce.", font="Arial 11")
    self.delka_strany_ctverce.grid(row=5, column=1, sticky = W+E)

    self.vypocitej_ctverec = tk.Button(self.top_ctverec, text="Vypočítej", command=lambda:vypocet_ctverce(self, self.strana_ctverce_a.get()))
    self.vypocitej_ctverec.grid(row=6, column=0, columnspan=2, sticky=W+E)

    self.mez_ctverec2 = tk.Label(self.top_ctverec)
    self.mez_ctverec2.grid(row=7, column=0)

    self.obvod_ctverec = tk.LabelFrame(self.top_ctverec, text="O = 4 x a", font="Arial 11")
    self.obvod_ctverec.grid(row=8, column=0, columnspan=2, sticky=W+E)
    self.obvod_ctverce_Label = StringVar()
    self.obvod_ctverce = tk.Label(self.obvod_ctverec, textvariable=self.obvod_ctverce_Label, width=20)
    self.obvod_ctverce.grid(row=9, column=0)
    self.obvod_ctverce1 = tk.Label(self.obvod_ctverec, text="Výsledný obvod čtverce.", width=20)
    self.obvod_ctverce1.grid(row=9, column=1)

    self.mez_ctverec3 = tk.Label(self.top_ctverec)
    self.mez_ctverec3.grid(row=10, column=0)

    self.obsah_ctverec = tk.LabelFrame(self.top_ctverec, text="S = a x a", font="Arial 11")
    self.obsah_ctverec.grid(row=11, column=0, columnspan=2, sticky=W+E)
    self.obsah_ctverce_Label = StringVar()
    self.obsah_ctverce = tk.Label(self.obsah_ctverec, textvariable=self.obsah_ctverce_Label, width=20)
    self.obsah_ctverce.grid(row=12, column=0)
    self.obsah_ctverce1 = tk.Label(self.obsah_ctverec, text="Výsledný obsah čtverce.", width=20)
    self.obsah_ctverce1.grid(row=12, column=1)

def vypocet_ctverce(self, strana):
    try:
        self.obvod_ctverce_Label.set(4*int(strana))
        self.obsah_ctverce_Label.set(int(strana)**2)
    except ValueError:
        tk.messagebox.showwarning("ERROR", "Vyplň délku strany.")
        return


def obdelnik(self):
    self.top_obdelnik = tk.Toplevel()
    self.top_obdelnik.title("Obdélník")
    self.obdelnik_foto=PhotoImage(file="obr/obdelnik.gif")
    self.obdelnik = tk.Label(self.top_obdelnik, image=self.obdelnik_foto) 
    self.obdelnik.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    self.mez_obdelnik1 = tk.Label(self.top_obdelnik)
    self.mez_obdelnik1.grid(row=4, column=0)

    self.Entry_obdelnik_strana_a = StringVar()
    self.strana_obdelnik_a = ttk.Entry(self.top_obdelnik, textvariable=self.Entry_obdelnik_strana_a, width=20)
    self.strana_obdelnik_a.config(state=NORMAL)
    self.strana_obdelnik_a.grid(row=5, column=0)
    self.delka_strany_obdelniku = tk.Label(self.top_obdelnik, text="Zadej délku strany 'a' obdélníku.", font="Arial 11")
    self.delka_strany_obdelniku.grid(row=5, column=1, sticky = W+E)

    self.Entry_obdelnik_strana_b = StringVar()
    self.strana_obdelnik_b = ttk.Entry(self.top_obdelnik, textvariable=self.Entry_obdelnik_strana_b, width=20)
    self.strana_obdelnik_b.config(state=NORMAL)
    self.strana_obdelnik_b.grid(row=6, column=0)
    self.delka_strany_obdelniku = tk.Label(self.top_obdelnik, text="Zadej délku strany 'b' obdélníku.", font="Arial 11")
    self.delka_strany_obdelniku.grid(row=6, column=1, sticky = W+E)

    self.vypocitej_obdelnik = tk.Button(self.top_obdelnik, text="Vypočítej", command=lambda:vypocet_obdelniku(self, self.strana_obdelnik_a.get(), self.strana_obdelnik_b.get()))
    self.vypocitej_obdelnik.grid(row=7, column=0, columnspan=2, sticky=W+E)

    self.mez_ctverec2 = tk.Label(self.top_obdelnik)
    self.mez_ctverec2.grid(row=8, column=0)
    
    self.obvod_obdelnik = tk.LabelFrame(self.top_obdelnik, text="O = 2 x (a + b)", font="Arial 11")
    self.obvod_obdelnik.grid(row=9, column=0, columnspan=2, sticky=W+E)
    self.obvod_obdelniku_Label = StringVar()
    self.obvod_obdelniku = tk.Label(self.obvod_obdelnik, textvariable=self.obvod_obdelniku_Label, width=20)
    self.obvod_obdelniku.grid(row=10, column=0)
    self.obvod_obdelniku1 = tk.Label(self.obvod_obdelnik, text="Výsledný obvod obdélníku.", width=20)
    self.obvod_obdelniku1.grid(row=10, column=1)

    self.mez_obdelnik3 = tk.Label(self.top_obdelnik)
    self.mez_obdelnik3.grid(row=11, column=0)

    self.obsah_obdelnik = tk.LabelFrame(self.top_obdelnik, text="S = a x b", font="Arial 11")
    self.obsah_obdelnik.grid(row=12, column=0, columnspan=2, sticky=W+E)
    self.obsah_obdelniku_Label = StringVar()
    self.obsah_obdelniku = tk.Label(self.obsah_obdelnik, textvariable=self.obsah_obdelniku_Label, width=20)
    self.obsah_obdelniku.grid(row=13, column=0)
    self.obsah_obdelniku1 = tk.Label(self.obsah_obdelnik, text="Výsledný obsah obdélníku.", width=20)
    self.obsah_obdelniku1.grid(row=13, column=1)
    

def vypocet_obdelniku(self, a, b):
    try:
        self.obvod_obdelniku_Label.set((int(a) + int(b)) * 2)
        self.obsah_obdelniku_Label.set(int(a) * int(b))
        if a == b:
            tk.messagebox.showwarning("???", "Tak jako spočítal jsem to.\nAle jen pro pořádek, tohle není obdélník.")
    except ValueError:
        tk.messagebox.showwarning("ERROR", "Vyplň délky stran.")
        return


def krychle(self):
    self.top_krychle = tk.Toplevel()
    self.top_krychle.title("Obdélník")
    self.krychle_foto=PhotoImage(file="obr/krychle.gif")
    self.krychle = tk.Label(self.top_krychle, image=self.krychle_foto) 
    self.krychle.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    self.mez_krychle1 = tk.Label(self.top_krychle)
    self.mez_krychle1.grid(row=4, column=0)

    self.Entry_krychle_strana_a = StringVar()
    self.strana_krychle_a = ttk.Entry(self.top_krychle, textvariable=self.Entry_krychle_strana_a, width=20)
    self.strana_krychle_a.config(state=NORMAL)
    self.strana_krychle_a.grid(row=5, column=0)
    self.delka_strany_krychle = tk.Label(self.top_krychle, text="Zadej délku strany krychle.", font="Arial 11")
    self.delka_strany_krychle.grid(row=5, column=1, sticky = W+E)

    self.vypocitej_krychly = tk.Button(self.top_krychle, text="Vypočítej", command=lambda:vypocet_krychle(self, self.strana_krychle_a.get()))
    self.vypocitej_krychly.grid(row=7, column=0, columnspan=2, sticky=W+E)

    self.mez_krychle2 = tk.Label(self.top_krychle)
    self.mez_krychle2.grid(row=8, column=0)
    
    self.obvod_krychle = tk.LabelFrame(self.top_krychle, text="O = 12 x a", font="Arial 11")
    self.obvod_krychle.grid(row=9, column=0, columnspan=2, sticky=W+E)
    self.obvod_krychle_Str = StringVar()
    self.obvod_krychle_Label = tk.Label(self.obvod_krychle, textvariable=self.obvod_krychle_Str, width=20)
    self.obvod_krychle_Label.grid(row=10, column=0)
    self.obvod_krychle1 = tk.Label(self.obvod_krychle, text="Výsledná hrana krychle.", width=30)
    self.obvod_krychle1.grid(row=10, column=1)

    self.mez_krychle3 = tk.Label(self.top_krychle)
    self.mez_krychle3.grid(row=11, column=0)

    self.plocha_krychle = tk.LabelFrame(self.top_krychle, text="Q = (a x a) * 6", font="Arial 11")
    self.plocha_krychle.grid(row=12, column=0, columnspan=2, sticky=W+E)
    self.plocha_krychle_Str = StringVar()
    self.plocha_krychle_Label = tk.Label(self.plocha_krychle, textvariable=self.plocha_krychle_Str, width=20)
    self.plocha_krychle_Label.grid(row=13, column=0)
    self.plocha_krychle1 = tk.Label(self.plocha_krychle, text="Výsledná plocha krychle.", width=30)
    self.plocha_krychle1.grid(row=13, column=1)

    self.mez_krychle5 = tk.Label(self.top_krychle)
    self.mez_krychle5.grid(row=14, column=0)

    self.objem_krychle = tk.LabelFrame(self.top_krychle, text="V = a x a x a", font="Arial 11")
    self.objem_krychle.grid(row=15, column=0, columnspan=2, sticky=W+E)
    self.objem_krychle_Str = StringVar()
    self.objem_krychle_Label = tk.Label(self.objem_krychle, textvariable=self.objem_krychle_Str, width=20)
    self.objem_krychle_Label.grid(row=16, column=0)
    self.objem_krychle1 = tk.Label(self.objem_krychle, text="Výsledný objem krychle.", width=30)
    self.objem_krychle1.grid(row=16, column=1)


def vypocet_krychle(self, a):
    try:
        self.obvod_krychle_Str.set(int(a) * 12)
        self.plocha_krychle_Str.set((int(a) * int(a)) * 6)
        self.objem_krychle_Str.set(int(a) * int(a) * int(a))
    except ValueError:
        tk.messagebox.showwarning("ERROR", "Vyplň délku strany.")
        return

def kvadr(self):
    self.top_kvadr = tk.Toplevel()
    self.top_kvadr.title("Obdélník")
    self.kvadr_foto=PhotoImage(file="obr/kvadr.gif")
    self.kvadr = tk.Label(self.top_kvadr, image=self.kvadr_foto) 
    self.kvadr.grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
    self.mez_kvadr1 = tk.Label(self.top_kvadr)
    self.mez_kvadr1.grid(row=4, column=0)

    self.Entry_kvadr_strana_a = StringVar()
    self.strana_kvadr_a = ttk.Entry(self.top_kvadr, textvariable=self.Entry_kvadr_strana_a, width=20)
    self.strana_kvadr_a.config(state=NORMAL)
    self.strana_kvadr_a.grid(row=5, column=0)
    self.delka_strany_kvadru_a = tk.Label(self.top_kvadr, text="Zadej délku strany 'a' kvádru.", font="Arial 11")
    self.delka_strany_kvadru_a.grid(row=5, column=1, sticky = W+E)

    self.Entry_kvadr_strana_b = StringVar()
    self.strana_kvadr_b = ttk.Entry(self.top_kvadr, textvariable=self.Entry_kvadr_strana_b, width=20)
    self.strana_kvadr_b.config(state=NORMAL)
    self.strana_kvadr_b.grid(row=6, column=0)
    self.delka_strany_kvadru_b = tk.Label(self.top_kvadr, text="Zadej délku strany 'b' kvádru.", font="Arial 11")
    self.delka_strany_kvadru_b.grid(row=6, column=1, sticky = W+E)

    self.Entry_kvadr_strana_c = StringVar()
    self.strana_kvadr_c = ttk.Entry(self.top_kvadr, textvariable=self.Entry_kvadr_strana_c, width=20)
    self.strana_kvadr_c.config(state=NORMAL)
    self.strana_kvadr_c.grid(row=7, column=0)
    self.delka_strany_kvadru_c = tk.Label(self.top_kvadr, text="Zadej délku strany 'c' kvádru.", font="Arial 11")
    self.delka_strany_kvadru_c.grid(row=7, column=1, sticky = W+E)

    self.vypocitej_kvadr = tk.Button(self.top_kvadr, text="Vypočítej", command=lambda:vypocet_kvadru(self, self.strana_kvadr_a.get(), self.strana_kvadr_b.get(), self.strana_kvadr_c.get()))
    self.vypocitej_kvadr.grid(row=8, column=0, columnspan=2, sticky=W+E)

    self.mez_kvadr2 = tk.Label(self.top_kvadr)
    self.mez_kvadr2.grid(row=9, column=0)
    
    self.obvod_kvadr = tk.LabelFrame(self.top_kvadr, text="O = 2 x (a + b + c)", font="Arial 11")
    self.obvod_kvadr.grid(row=10, column=0, columnspan=2, sticky=W+E)
    self.obvod_kvadr_Str = StringVar()
    self.obvod_kvadr_Label = tk.Label(self.obvod_kvadr, textvariable=self.obvod_kvadr_Str, width=20)
    self.obvod_kvadr_Label.grid(row=11, column=0)
    self.obvod_kvadr1 = tk.Label(self.obvod_kvadr, text="Výsledná hrana kvádru.", width=30)
    self.obvod_kvadr1.grid(row=11, column=1, sticky=W)

    self.mez_kvadr3 = tk.Label(self.top_kvadr)
    self.mez_kvadr3.grid(row=12, column=0)

    self.plocha_kvadr = tk.LabelFrame(self.top_kvadr, text="Q = 2 x (ab + bc + ac)", font="Arial 11")
    self.plocha_kvadr.grid(row=13, column=0, columnspan=2, sticky=W+E)
    self.plocha_kvadr_Str = StringVar()
    self.plocha_kvadr_Label = tk.Label(self.plocha_kvadr, textvariable=self.plocha_kvadr_Str, width=20)
    self.plocha_kvadr_Label.grid(row=14, column=0)
    self.plocha_kvadr1 = tk.Label(self.plocha_kvadr, text="Výsledná plocha kvádru.", width=30)
    self.plocha_kvadr1.grid(row=14, column=1, sticky=W)

    self.mez_kvadr4 = tk.Label(self.top_kvadr)
    self.mez_kvadr4.grid(row=15, column=0)

    self.objem_kvadr = tk.LabelFrame(self.top_kvadr, text="V = a x b x c", font="Arial 11")
    self.objem_kvadr.grid(row=16, column=0, columnspan=2, sticky=W+E)
    self.objem_kvadr_Str = StringVar()
    self.objem_kvadr_Label = tk.Label(self.objem_kvadr, textvariable=self.objem_kvadr_Str, width=20)
    self.objem_kvadr_Label.grid(row=17, column=0)
    self.objem_kvadr1 = tk.Label(self.objem_kvadr, text="Výsledný objem kvádru.", width=30)
    self.objem_kvadr1.grid(row=17, column=1, sticky=W)

def vypocet_kvadru(self, a, b, c):
    try:
        self.obvod_kvadr_Str.set(4 * (int(a)+int(b)+int(c)))
        self.plocha_kvadr_Str.set(2 * (int(a)*int(c)) + 4 * (int(c)*int(b)))
        self.objem_kvadr_Str.set(int(a) * int(b) * int(c))
    except ValueError:
        tk.messagebox.showwarning("ERROR", "Vyplň délku strany.")
        return