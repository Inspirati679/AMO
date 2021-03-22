import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *


def make(a, b, n, var):
    h = (b - a) / n
    x = []
    y = []
    for i in range(0, n + 1):
        x.append(a + (h * i))
        if var == 0:
            y.append(np.sin(x[i]) * np.sin(x[i]))
        else:
            y.append(math.sin(x[i]))
    return (x, y)


def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = \
                (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef


def newton_poly(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


def graphic(x, y, x_int, y_int, text1, text2):
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    ax.plot(x, y, color="C1")
    ax.set_xlabel(text1, color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")
    ax2.plot(x_int, y_int, color="C2")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel(text2, color="C2")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C2")
    ax2.tick_params(axis='y', colors="C2")
    plt.show()


def graph1():
    x, y = make(0, 1, 10, 0)
    x_int, y1 = np.array(make(0, 1, 100, 0))

    a_s = divided_diff(x, y)[0, :]
    x_new = x_int
    y_new = newton_poly(a_s, x, x_new)


    graphic(x, y, x_int, y_new, "sin^2(x)", "sin^2(x) інтерполяція")


def graph2():
    x, y = make(0, 1, 10, 1)
    x_int, y1 = np.array(make(0, 1, 100, 1))

    a_s = divided_diff(x, y)[0, :]
    x_new = x_int
    y_new = newton_poly(a_s, x, x_new)


    graphic(x, y, x_int, y_new, "sin(x)", "sin(x) інтерполяція")


def pohib1():
    x, y = make(0, 1, 100, 0)
    x_int, y1 = np.array(make(0, 1, 100, 0))

    a_s = divided_diff(x, y)[0, :]
    x_new = x_int
    y_new = newton_poly(a_s, x, x_new)

    ylist_f = y
    flist_f = y_new

    def funcy(i):
        y = (ylist_f[i] - flist_f[i])
        return y

    suby = [funcy(i) for i in range(len(x_int))]
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(x_int, suby, color="C5")
    ax.set_xlabel("Похибка sin(x)", color="C5")
    ax.tick_params(axis='x', colors="C5")
    plt.show()


def pohib2():
    x, y = make(0, 1, 100, 1)
    x_int, y1 = np.array(make(0, 1, 100, 1))

    a_s = divided_diff(x, y)[0, :]
    x_new = x_int
    y_new = newton_poly(a_s, x, x_new)

    ylist_f = y
    flist_f = y_new

    def funcy(i):
        y = (ylist_f[i] - flist_f[i])
        return y

    suby = [funcy(i) for i in range(len(x_int))]
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(x_int, suby, color="C5")
    ax.set_xlabel("Похибка sin^2(x)", color="C5")
    ax.tick_params(axis='x', colors="C5")
    plt.show()


def new_window():
    window = Toplevel(root)
    window.title("Інфо")
    window.geometry("280x180")
    label3 = Label(window, text=info, font="Ariel 18", width=20, height=15, bg="yellow").place(x=0,
                                                                                               y=-115)


info = "{:^30}".format("Виконав") + "\n" + "{:^30}".format("Мельник Антон") + "\n" + "{:^30}".format(
    "Студент групи ІВ-93") + "\n" + "{:^30}".format("Варіант 16")
root = Tk()
root.title("Вікно")
root["bg"] = "pink"
root.geometry("470x290")
menu = Menu(root)
mainmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Меню", menu=mainmenu)
mainmenu.add_command(label="Інфо", command=new_window)
root.configure(menu=menu)
Button(root, text="Інтерполяція функції sin(x)^2", command=graph1, font=("Courier", 15), width=30, bg="yellow").place(
    x=50, y=50)
Button(root, text="Інтерполяція функції sin(x)", command=graph2, font=("Courier", 15), width=30, bg="yellow").place(
    x=50, y=100)
Button(root, text="Похибка функції sin^2(x)", command=pohib2, font=("Courier", 15), width=30, bg="yellow").place(x=50,
                                                                                                                 y=150)
Button(root, text="Похибка функції sin(x)", command=pohib1, font=("Courier", 15), bg="yellow", width=30).place(x=50,
                                                                                                               y=200)
root.mainloop()
