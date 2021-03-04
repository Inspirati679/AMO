from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import operator
from functools import reduce
import math


def graphic1():
    x, y = make(0, 2, 10, 1)
    x_int, y1 = make(0, 2, 1000, 1)
    y_int = []
    for i in x_int:
        y_int.append(lagrang(i, x, y))
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    ax.plot(x, y, color="C3")
    ax.set_xlabel("sin(x)", color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")
    ax2.plot(x_int, y_int, color="C2")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('sin(x) інтерполяція', color="C2")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C2")
    ax2.tick_params(axis='y', colors="C2")
    plt.show()


def graphic2():
    x, y = make(0, 2, 10, 0)
    x_int, y1 = make(0, 2, 1000, 0)
    y_int = []
    for i in x_int:
        y_int.append(lagrang(i, x, y))
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    ax.plot(x, y, color="C3")
    ax.set_xlabel("sin(x)", color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")
    ax2.plot(x_int, y_int, color="C2")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('sin(x) інтерполяція', color="C2")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C2")
    ax2.tick_params(axis='y', colors="C2")
    plt.show()
def graphic3():
    w=[]
    x, y = make(0, 2, 10, 0)
    x_int, y1 = make(0, 2, 1000, 0)
    y_int = []
    print(x_int)
    for i in x_int:
        y_int.append(lagrang(i, x, y))
    for i in range(10):
        pass




def make(a, b, n, var):
    h = (b - a) / n
    x = []
    y = []
    for i in range(0, n + 1):
        x.append(a + (h * i))
        if var == 0:
            y.append(np.cos(x[i] + pow(np.cos(x[i]), 3)))
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


root = Tk()
root["bg"] = "yellow"
Button(root, text="Інтерполяція функції sin(x)", command=graphic1, font=("Times", 15), width=30).place(x=50,
                                                                                                       y=50)
Button(root, text="Інтерполяція функції cos(x+cosx^3)", command=graphic3, font=("Times", 15), width=30).place(x=50,
                                                                                                              y=100)

root.mainloop()
