from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import operator
from functools import reduce
import math

text2 = "{:^30}".format("Виконав") + "\n" + "{:^30}".format("Бернадін Олександр") + "\n" + "{:^30}".format(
    "Студент групи ІО-93") + "\n" + "{:^30}".format("Варіант 1")


def first_graph():
    x, y = points(0, 2, 10, 1)
    x_int, y1 = points(0, 2, 100, 1)
    y_int = []
    for i in x_int:
        y_int.append(lagrang(i, x, y))
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    ax.plot(x, y, color="C1")
    ax.set_xlabel("sin(x)", color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")
    ax2.plot(x_int, y_int, color="C10")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('sin(x) Interpolation', color="C10")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C10")
    ax2.tick_params(axis='y', colors="C10")
    plt.show()


def second_graph():
    x, y = points(0, 2, 10, 0)
    x_int, y1 = points(0, 2, 100, 0)
    y_int = []
    for i in x_int:
        y_int.append(lagrang(i, x, y))
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    ax.plot(x, y, color="C3")
    ax.set_xlabel("sin(x)^2", color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")
    ax2.plot(x_int, y_int, color="C10")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('sin(x)^2 Interpolation', color="C10")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C10")
    ax2.tick_params(axis='y', colors="C10")
    plt.show()


def third_graph():
    x, y = points(0, 2, 10, 1)
    x_int, y1 = points(0, 2, 100, 1)
    y_int = []

    for i in x_int:
        y_int.append(lagrang(i, x, y))

    def f(x):
        return np.sin(x)

    list_constants_sin = []
    a = len(x_int) - 1

    while a >= 0:
        constant = 0
        for i in range(len(x) - a):
            znam = 1
            for j in range(len(x) - a):
                if i != j:
                    znam *= (x[i] - x[j])
            constant += y[i] / znam
        list_constants_sin.append(constant)
        a -= 1

    y_arg = f(list_constants_sin) - y_int
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(x_int, y_arg, color="C1")
    ax.set_xlabel("Похибка sin(x)", color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")

    plt.show()


def fourth_graph():
    x, y = points(0, 2, 10, 0)
    x_int, y1 = points(0, 2, 100, 0)
    y_int = []

    for i in x_int:
        y_int.append(lagrang(i, x, y))

    def f(x):
        return np.cos(x[i] + pow(np.cos(x[i]), 3))

    list_constants_sin = []
    a = len(x_int) - 1

    while a >= 0:
        constant = 0
        for i in range(len(x) - a):
            znam = 1
            for j in range(len(x) - a):
                if i != j:
                    znam *= (x[i] - x[j])
            constant += y[i] / znam
        list_constants_sin.append(constant)
        a -= 1

    pol = y_int
    y_arg = f(list_constants_sin) - y_int

    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(x_int, y_arg, color="C10")
    ax.set_xlabel("Похибка sin(x)^2", color="C10")
    ax.tick_params(axis='x', colors="C10")
    ax.tick_params(axis='y', colors="C10")

    plt.show()


def points(a, b, n, var):
    h = (b - a) / n
    x = []
    y = []
    for i in range(0, n + 1):
        x.append(a + (h * i))
        if var == 0:
            y.append(np.sin(x[i]) ** 2)
        else:
            y.append(math.sin(x[i]))
    return (x, y)


def lagrang(x, x_values, y_values):
    def _basis(j):
        p = [(x - x_values[m]) / (x_values[j] - x_values[m]) for m in range(k) if m != j]
        return reduce(operator.mul, p)

    assert len(x_values) != 0 and (
            len(x_values) == len(y_values)), 'x and y cannot be empty and must have the same length'
    k = len(x_values)
    return sum(_basis(j) * y_values[j] for j in range(k))


window = Tk()
window.title("Main Window")
window["bg"] = "pink"
window.geometry("850x300")
Button(window, text="Interpolation функції sin(x)", command=first_graph, font=("Times", 15), width=30).place(x=50,
                                                                                                             y=50)
Button(window, text="Interpolation функції sin(x)^2", command=second_graph, font=("Times", 15), width=30).place(x=50,
                                                                                                                y=100)
Button(window, text="Error sin(x)", command=third_graph, font=("Times", 15), width=30).place(x=50,
                                                                                             y=150)
Button(window, text="Error sin(x)^2", command=fourth_graph, font=("Times", 15), width=30).place(x=50,
                                                                                                y=200)
label3 = Label(window, text=text2, font="Ariel 18", width=20, height=15, bg="pink").place(x=500,
                                                                                          y=-80)

window.mainloop()
