import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root['bg'] = "yellow"
root.title("Лабораторна робота №3")
root.geometry("400x220")
root.resizable(width=False, height=False)

font_default = 'Arial 14'
bg_default = "yellow"
but_bg_default = 'darkorange'
but_fg_default = 'black'


class Go():
    i = 10
    a = 0
    b = 4

    xi = []
    y_f = []
    y_sin = []
    list_constants = []
    list_constants_sin = []

    h = (b - a)/10

    for i in range(i+1):
        xi.append(round(a+h*i,12))
    print(xi)

    for i in range(len(xi)):
        y_f.append( (2*math.sin(xi[i]))-(3*math.cos(xi[i])) )
        y_sin.append( math.sin(xi[i]) )

    def __init__(self):

        inform = Label(root, text = "Бровченко Анастасія Вікторівна\n"
                                    "Група ІО-64\n"
                                    "Номер у списку - 3\n\n"
                                    "Тема:«Інтерполяція функцій", bg=bg_default,
                       font=font_default)
        inform.pack(side = TOP, fill=BOTH, expand = True)

        Button(root, text='Завдання за варіантом', bg=but_bg_default, fg=but_fg_default, font=font_default,
               command=self.condition).pack(side=BOTTOM)

    def condition(self):

        top = Toplevel(root, bg=bg_default)
        top.title("Варіант завдання")
        top.geometry("600x280")
        top.resizable(width=False, height=False)

        var = Label(top, text="Інтерполяція функції через многочлен Ньютона\n\n"
                              "f(x)=2sin(x)−3cos(x)\n"
                              "[a,b]=[{},{}]".format(self.a, self.b), bg=bg_default, font="Arial 16")

        button_f= Frame(top, bg=bg_default)
        button_f1= Frame(button_f, bg=bg_default)
        button_f2= Frame(button_f, bg=bg_default)

        empty_label1 = Label(top, bg=bg_default)
        empty_label2 = Label(button_f, bg=bg_default)

        empty_label3 = Label(button_f1, bg=bg_default)
        empty_label4 = Label(button_f2, bg=bg_default)

        self.interp_f = Button(button_f1, text = "Графік інтерполяції функції", width = 25, height = 2,
                               command = self.interpolation_f, bg=but_bg_default, fg=but_fg_default, font=font_default)
        self.infelicity_f = Button(button_f2, text = "Похибка інтерполяції функції", width = 25, height = 1,
                                   command = self.infelicity_f, bg=but_bg_default, fg=but_fg_default, font=font_default)
        self.interp_sin = Button(button_f1, text="Графік інтерполяції sin(x)", width = 25, height = 2,
                                 command = self.interpolation_sin, bg=but_bg_default, fg=but_fg_default, font=font_default)
        self.infelicity_sin = Button(button_f2, text="Похибка інтерполяції sin(x)", width = 25, height = 1,
                                     command = self.infelicity_sin, bg=but_bg_default, fg=but_fg_default, font=font_default)

        var.pack(side = TOP)
        empty_label1.pack(side=TOP)
        button_f.pack(side=TOP)
        button_f1.pack(side=TOP)
        empty_label2.pack(side=TOP)
        button_f2.pack(side=TOP)
        self.interp_f.pack(side=LEFT)
        empty_label3.pack(side=LEFT)
        self.interp_sin.pack(side=RIGHT)
        self.infelicity_f.pack(side=LEFT)
        empty_label4.pack(side=LEFT)
        self.infelicity_sin.pack(side=RIGHT)

        top.mainloop()

    def interpolation_sin(self):
        self.list_constants_sin = []

        a = len(self.xi)-1
        print(a)
        while a >= 0:
            constant = 0
            for i in range(len(self.xi)-a):
                znam = 1
                for j in range(len(self.xi)-a):
                    if i != j:
                        znam *= (self.xi[i]-self.xi[j])
                constant += self.y_sin[i]/znam
            self.list_constants_sin.append(constant)
            a -= 1

        self.graph_sin()

    def result_sin(self, x):
        g=1
        a = len(self.xi)-1
        listh = [1]

        for i in range(len(self.xi)):
            g *= (x - self.xi[i])
            listh.append(g)

        f0 = 0
        for i in range(len(self.list_constants_sin)):
            f0 += self.list_constants_sin[i]*listh[i]
        return f0

    def func_sin(self,x):
            sin = self.result_sin(x)
            return sin

    def graph_sin(self):
        self.xlist_sin = []
        for i in np.arange(Go().a, Go().b+0.1, 0.1):
            self.xlist_sin.append(i)

        def funcy(x):
            y = (math.sin(x))
            return y

        self.ylist_sin = [funcy(x) for x in self.xlist_sin]
        self.flist_sin = [self.func_sin(x) for x in self.xlist_sin]

        plt.subplot(311)
        plt.plot(self.xlist_sin,self.ylist_sin)
        plt.title(r'$sin(x)$')
        plt.grid(True)

        plt.subplot(313)
        plt.plot(self.xlist_sin,self.flist_sin,'g')
        plt.title(r'$інтерполяція$')
        plt.grid(True)

        plt.show()

    def infelicity_sin(self):

        plt.subplot(311)
        plt.plot(self.xlist_sin,self.ylist_sin,self.xlist_sin,self.flist_sin,"g")
        plt.title(r'$sin(x)$')
        plt.grid(True)

        ylist_sin = self.ylist_sin
        flist_sin = self.flist_sin

        def funcy(x):
            y = (ylist_sin[x] - flist_sin[x])
            return y

        suby = [funcy(x) for x in range(len(self.xlist_sin))]
        plt.subplot(313)
        plt.plot(self.xlist_sin,suby, "c")
        plt.title(r'$похибка$')
        plt.grid(True)

        plt.show()

    def interpolation_f(self):
        self.list_constants = []

        a = len(self.xi)-1
        while a >= 0:
            constant = 0
            for i in range(len(self.xi)-a):
                znam = 1
                for j in range(len(self.xi)-a):
                    if i != j:
                        znam *= (self.xi[i]-self.xi[j])
                constant += self.y_f[i]/znam
            self.list_constants.append(constant)
            a -= 1

        self.graph_f()

    def result_f(self, x):
        g=1
        a = len(self.xi)-1
        listh = [1]

        for i in range(len(self.xi)):
            print(x)
            g *= (x - self.xi[i])
            listh.append(g)

        f0 = 0
        for i in range(len(self.list_constants)):
            f0 += self.list_constants[i]*listh[i]
        return f0

    def func_f(self,x):
            f = self.result_f(x)
            return f

    def graph_f(self):
        slave = Toplevel(root)
        self.xlist_f = []

        for i in np.arange(Go().a, Go().b+0.1, 0.1):
            self.xlist_f.append(i)

        def funcy(x):
            y = (2*math.sin(x))-(3*math.cos(x))
            return y

        self.ylist_f = [funcy(x) for x in self.xlist_f]
        self.flist_f = [self.func_f(x) for x in self.xlist_f]

        f = Figure(figsize=(6, 6), dpi=100)
        a = f.add_subplot(311)
        a.plot(self.xlist_f, self.ylist_f)
        a.set_title(r'$2sin(x)−3cos(x)$')
        a.grid(True)

        b = f.add_subplot(313)
        b.plot(self.xlist_f,self.flist_f,'g')
        b.set_title(r'$інтерполяція$')
        b.grid(True)

        f.tight_layout()

        canvas = FigureCanvasTkAgg(f, slave)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    def infelicity_f(self):

        plt.subplot(311)
        plt.plot(self.xlist_f,self.ylist_f,self.xlist_f,self.flist_f,"r")
        plt.title(r'$2sin(x)−3cos(x)$')
        plt.grid(True)

        ylist_f = self.ylist_f
        flist_f = self.flist_f

        def funcy(x):
            y = (ylist_f[x] - flist_f[x])
            return y

        suby = [funcy(x) for x in range(len(self.xlist_f))]
        plt.subplot(313)
        plt.plot(self.xlist_f, suby, "k")
        plt.title(r'$похибка$')
        plt.grid(True)

        plt.show()


if __name__=="__main__":
    go = Go()
    root.mainloop()
