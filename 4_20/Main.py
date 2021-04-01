from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3 + 6 * x - 5


def f1(x):
    return 3 * x ** 2 + 6


def f2(x):
    return 6 * x


def eqt(a, b, e):
    counter = 0
    if f(a) < 0 and f(b) > 0:
        while True:
            counter += 1
            a = a - (f(a) * (b - a)) / (f(b) - f(a))
            b = b - (f(b) / f1(b))
            if abs(b - a) <= e:
                return (b + a) / 2, counter
    else:
        return 0, 0


class Main:
    def __init__(self):
        self.s = 0
        self.counter = 0

        self.root = Tk()

        self.entry1 = Entry(self.root, width=6, font=("Times", 15))
        self.entry2 = Entry(self.root, width=6, font=("Times", 15))
        self.entry3 = Entry(self.root, width=6, font=("Times", 15))

        Label(self.root, text="Розв'язок нелінійного рівняння", bg="#FF4500", font=("Times", 20)).place(x=50, y=10)
        Label(self.root, text="комбінованим методом x^3+6x-5", bg="#FF4500", font=("Times", 20)).place(x=50, y=45)
        Label(self.root, text="Початок", font=("Times", 15), bg="#FF4500").place(x=50, y=115)
        Label(self.root, text="Кінець", font=("Times", 15), bg="#FF4500").place(x=150, y=115)
        Label(self.root, text="Точність", font=("Times", 15), bg="#FF4500").place(x=250, y=115)
        Label(self.root, text="Межі для рівнняня\n [0, 1]", font=("Times", 15), bg="#FF4500").place(x=360, y=200)

        Button(self.root, width=12, text="Обрахувати", bg='#FFA07A', font=("Times", 15), command=self.result).place(
            x=350, y=88)
        Button(self.root, width=12, text="Графік", bg='#FFA07A', font=("Times", 15), command=self.graphic).place(x=350,
                                                                                                                 y=138)

        self.text1 = Text(self.root, width=30, height=1, bd=1, font=('Times', 15))
        self.text2 = Text(self.root, width=30, height=1, bd=1, font=('Times', 15))

        self.menu = Menu(self.root)
        self.mainmenu = Menu(self.menu, tearoff=0)

        self.entry()
        self.text()
        self.menu_func()
        self.root_cong()

    def entry(self):
        self.entry1.insert(END, 0)
        self.entry1.place(x=50, y=150)
        self.entry2.insert(END, 1)
        self.entry2.place(x=150, y=150)
        self.entry3.insert(END, 0.001)
        self.entry3.place(x=250, y=150)

    def menu_func(self):
        self.menu.add_cascade(label="Меню", menu=self.mainmenu)
        self.mainmenu.add_command(label="Інформація", command=self.info)

    def info(self):
        window = Toplevel(self.root)
        window.title("Інфо")
        window.geometry("280x180")
        Label(window, text="{:^30}".format("Автор") + "\n" + "{:^30}".format(
            "Рустамов Арсен") + "\n" + "{:^30}".format(
            "Група ІВ-93") + "\n" + "{:^30}".format("20"), font="Ariel 18", width=20, height=15, bg="#FF4500").place(
            x=0,
            y=-115)

    def text(self):
        self.text1.insert(1.0, "Відповідь:")
        self.text2.insert(1.0, "Кількість ітерацій:")
        self.text1.place(x=50, y=200)
        self.text2.place(x=50, y=230)

    def root_cong(self):
        self.root.geometry("540x280")
        self.root.title("Лабораторна 4")
        self.root["bg"] = "#FF4500"
        self.root.configure(menu=self.menu)
        self.root.mainloop()

    def graphic(self):
        if self.s != 0:
            x = np.arange(-3, 3, float(self.entry3.get()))
            y = x ** 3 + 6 * x - 5
            fig = plt.figure()
            ax = fig.add_subplot(111, label="3")
            ax.plot(x, y, color="C3")
            ax.set_xlabel("x^3+6x-5", color="C3")
            ax.tick_params(axis='x', colors="C3")
            ax.tick_params(axis='y', colors="C3")
            if self.s != 0:
                plt.scatter(self.s, f(self.s), c="r")
            plt.show()

    def result(self):
        self.s, self.counter = eqt(int(self.entry1.get()), int(self.entry2.get()), float(self.entry3.get()))
        if self.s != 0:
            self.text1.delete(1.0, END)
            self.text2.delete(1.0, END)
            self.text1.insert(1.0, "Відповідь:" + str(self.s))
            self.text2.insert(1.0, "Кількість ітерацій:" + str(self.counter))
        else:
            self.text1.delete(1.0, END)
            self.text2.delete(1.0, END)
            self.text1.insert(1.0, "Відповідь:" + " Помилка")
            self.text2.insert(1.0, "Кількість ітерацій:" + " Помилка")


if __name__ == "__main__":
    t = Main()
