from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


def secant(x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    if f_x0 * f_x1 < 0:
        while abs(f_x1) > eps and iteration_counter < 100:
            try:
                denominator = float(f_x1 - f_x0) / (x1 - x0)
                x = x1 - float(f_x1) / denominator
            except ZeroDivisionError:
                return None
            x0 = x1
            x1 = x
            f_x0 = f_x1
            f_x1 = f(x1)
            iteration_counter += 1
        if abs(f_x1) > eps:
            iteration_counter = -1
        return x
    else:
        return None


def f(x):
    return x * x * x - 12 * x - 8


def result():
    global entry1, entry2, entry3, t, label

    t = secant(int(entry1.get()), int(entry2.get()), float(entry3.get()))
    if t != None:

        label.place_forget()
        label = Label(root, text="Відповідь:" + str(t), font=("Times", 15), bg="yellow")
        label.place(x=50, y=230)

    else:
        label.place_forget()
        label = Label(root, text="Method fails", font=("Times", 15), bg="yellow")
        label.place(x=50, y=230)


def graphic():
    first = t
    x = np.arange(-4, 4, float(entry3.get()) * 10)
    y = x * x * x - 12 * x - 8
    fig = plt.figure()
    ax = fig.add_subplot(111, label="3")
    ax.plot(x, y, color="C1")
    ax.set_xlabel("x^3-12x-8", color="C3")
    ax.tick_params(axis='x', colors="C3")
    ax.tick_params(axis='y', colors="C3")
    plt.scatter(first, first * first * first - 12 * first - 8, c="r")
    plt.show()


def new_window():
    window = Toplevel(root)
    window.title("Інфо")
    window.geometry("280x180")
    label3 = Label(window, text=text2, font="Ariel 18", width=20, height=15, bg="yellow").place(x=0,
                                                                                                y=-115)


if __name__ == "__main__":
    text2 = "{:^30}".format("Виконав") + "\n" + "{:^30}".format("Мельник Антон") + "\n" + "{:^30}".format(
        "Студент групи ІВ-93") + "\n" + "{:^30}".format("Варіант 16")
    root = Tk()
    root.title("Головне вікно")
    root.geometry("600x300")
    root["bg"] = "yellow"

    menu = Menu(root)
    mainmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Меню", menu=mainmenu)
    mainmenu.add_command(label="Інфо", command=new_window)
    root.configure(menu=menu)

    entry1 = Entry(root, width=6, font=("Times", 12))
    entry1.insert(END, -4)
    entry1.place(x=50, y=75)
    entry2 = Entry(root, width=6, font=("Times", 12))
    entry2.insert(END, -3)
    entry2.place(x=150, y=75)
    entry3 = Entry(root, width=6, font=("Times", 12))
    entry3.insert(END, 0.001)
    entry3.place(x=250, y=75)
    Label(root, text="Від", font=("Times", 15), bg="yellow").place(x=50, y=40)
    Label(root, text="До", font=("Times", 15), bg="yellow").place(x=150, y=40)
    Label(root, text="Точність", font=("Times", 15), bg="yellow").place(x=250, y=40)
    Label(root, text="Межі для рівняння [-4, -3], [-1, 0], [3, 4]", font=("Times", 15), bg="yellow").place(x=50, y=125)
    label = Label(root, text="Відповідь:", font=("Times", 15), bg="yellow")
    label.place(x=50, y=230)
    Button(root, width=12, text="Обрахувати", bg='pink', font=("Times", 15), command=result).place(x=50, y=175)
    Button(root, width=12, text="Графік", bg='pink', font=("Times", 15), command=graphic).place(x=250, y=175)

    root.mainloop()
