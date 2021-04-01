import math
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


def first_func(a, b, n, var):
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


def second_func(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = \
                (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef


def third_func(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


def graphic(x, y, x_int, y_int, text1, text2):
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="4", frame_on=False)
    ax.plot(x, y, color="C1")
    ax.set_xlabel(text1, color="C1")
    ax.tick_params(axis='x', colors="C1")
    ax.tick_params(axis='y', colors="C1")
    ax2.plot(x_int, y_int, color="C4")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel(text2, color="C4")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C4")
    ax2.tick_params(axis='y', colors="C4")
    plt.show()


def graph1():
    x, y = first_func(0, 1, 10, 0)
    x_int, y1 = np.array(first_func(0, 1, 100, 0))

    a_s = second_func(x, y)[0, :]
    x_new = x_int
    y_new = third_func(a_s, x, x_new)

    graphic(x, y, x_int, y_new, "sin^2(x)", "sin^2(x) інтерполяція")


def graph2():
    x, y = first_func(0, 1, 10, 1)
    x_int, y1 = np.array(first_func(0, 1, 100, 1))

    a_s = second_func(x, y)[0, :]
    x_new = x_int
    y_new = third_func(a_s, x, x_new)

    graphic(x, y, x_int, y_new, "sin(x)", "sin(x) інтерполяція")


def fault1():
    x, y = first_func(0, 1, 100, 0)
    x_int, y1 = np.array(first_func(0, 1, 100, 0))

    a_s = second_func(x, y)[0, :]
    x_new = x_int
    y_new = third_func(a_s, x, x_new)

    ylist_f = y
    flist_f = y_new

    def funcy(i):
        y = (ylist_f[i] - flist_f[i])
        return y

    suby = [funcy(i) for i in range(len(x_int))]
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(x_int, suby, color="C1")
    ax.set_xlabel("Похибка sin(x)", color="C1")
    ax.tick_params(axis='x', colors="C1")

    plt.show()


def fault2():
    x, y = first_func(0, 1, 100, 1)
    x_int, y1 = np.array(first_func(0, 1, 100, 1))

    a_s = second_func(x, y)[0, :]
    x_new = x_int
    y_new = third_func(a_s, x, x_new)

    ylist_f = y
    flist_f = y_new

    def funcy(i):
        y = (ylist_f[i] - flist_f[i])
        return y

    suby = [funcy(i) for i in range(len(x_int))]
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax.plot(x_int, suby, color="C1")
    ax.set_xlabel("Похибка sin^2(x)", color="C1")
    ax.tick_params(axis='x', colors="C1")

    plt.show()


if __name__ == "__main__":
    root = Tk()
    root.title("Вікно")
    root["bg"] = "turquoise"
    root.geometry("825x290")
    Button(root, text="Інтерполяція функції sin(x)^2", command=graph1, font=("Gothic", 11), width=42,
           bg="#F0E68C").place(
        x=50, y=50)
    Button(root, text="Інтерполяція функції sin(x)", command=graph2, font=("Gothic", 11), width=42, bg="#F0E68C").place(
        x=50, y=100)
    Button(root, text="Похибка функції sin^2(x)", command=fault2, font=("Gothic", 11), width=42, bg="#F0E68C").place(
        x=430,
        y=50)
    Button(root, text="Похибка функції sin(x)", command=fault1, font=("Gothic", 11), bg="#F0E68C", width=42).place(
        x=430,
        y=100)
    Label(root, text="Куцурайс Георгій\n ІО-93\n Варіант 16", font=("Times", 25), bg="turquoise", fg="#FF4500").place(
        x=280, y=150)
    root.mainloop()
