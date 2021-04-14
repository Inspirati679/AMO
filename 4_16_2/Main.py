from tkinter import *
from functions_all import *
import numpy as np
import matplotlib.pyplot as plt


class Main:
    def __init__(self):
        self.res = 0

        self.root = Tk()

        self.entry1 = Entry(self.root, width=6, font=("Times", 14))
        self.entry2 = Entry(self.root, width=6, font=("Times", 14))
        self.entry3 = Entry(self.root, width=6, font=("Times", 14))

        Button(self.root, command=self.result, font=("Times", 14), bg="#b2f3ba", text="Показати результат",
               width=16).place(x=230, y=60)
        Button(self.root, command=self.graphic, font=("Times", 14), bg="#b2f3ba", text="Показати графік",
               width=16).place(x=230, y=105)
        Button(self.root, command=self.clear, font=("Times", 14), bg="#b2f3ba", text="Стерти данні", width=16).place(
            x=230, y=150)

        Label(self.root, text="Розв'язок нелінійного рівняння", font=("Times", 20), bg="#8f4f87").place(x=420, y=55)
        Label(self.root, text="методом хорд x^3-12x-8=0", font=("Times", 20), bg="#8f4f87").place(x=420, y=85)
        Label(self.root, text="Проміжок", font=("Times", 15), bg="#8f4f87").place(x=75, y=65)
        Label(self.root, text="Від", font=("Times", 15), bg="#8f4f87").place(x=10, y=95)
        Label(self.root, text="До", font=("Times", 15), bg="#8f4f87").place(x=115, y=95)
        Label(self.root, text="Точність", font=("Times", 15), bg="#8f4f87").place(x=10, y=145)
        Label(self.root, text="Виконав: Куцурайс Георгій", font=("Times", 16), bg="#8f4f87").place(x=10, y=10)
        Label(self.root, text="Межі для рівняння [-4, -3], [-1, 0], [3, 4]", font=("Times", 16), bg="#8f4f87").place(
            x=420, y=195)

        self.text = Text(self.root, font=("Times", 15), width=38, height=1, bd=1)

        self.entry_func()
        self.text_func()
        self.root_func()

    def root_func(self):
        self.root.geometry("800x250")
        self.root.title("Программа")
        self.root["bg"] = "#8f4f87"
        self.root.mainloop()

    def entry_func(self):
        self.entry1.insert(0, 3)
        self.entry2.insert(0, 4)
        self.entry3.insert(0, 0.001)

        self.entry1.place(x=50, y=100)
        self.entry2.place(x=150, y=100)
        self.entry3.place(x=100, y=150)

    def text_func(self):
        self.text.insert(1.0, "Результат:")
        self.text.place(x=15, y=200)

    def result(self):
        if self.entry1.get() != '' and self.entry2.get() != '' and self.entry3.get() != '':
            self.res = secant(int(self.entry1.get()), int(self.entry2.get()), float(self.entry3.get()))
            if self.res is not None:
                self.text.delete(1.0, END)
                self.text.insert(1.0, "Результат: " + str(self.res))
            else:
                self.text.delete(1.0, END)
                self.text.insert(1.0, "Результат: Помилка")

    def graphic(self):
        if self.entry1.get() != '' and self.entry2.get() != '' and self.entry3.get() != '':
            x = np.arange(-4, 4, float(self.entry3.get()) * 10)
            y = x ** 3 - 12 * x - 8
            fig = plt.figure()

            ax = fig.add_subplot(111, label="3")
            ax.plot(x, y, color="C1")
            ax.set_xlabel("x^3-12x-8", color="C3")
            ax.tick_params(axis='x', colors="C3")
            ax.tick_params(axis='y', colors="C3")

            plt.scatter(self.res, self.res ** 3 - 12 * self.res - 8, c="r")
            plt.show()

    def clear(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)

        self.text.delete(1.0, END)
        self.text.insert(1.0, "Результат:")


if __name__ == "__main__":
    t = Main()
