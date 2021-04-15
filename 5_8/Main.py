from tkinter import *
import copy

m_list = [[1.84, 2.25, 2.58, -6.09],
          [2.32, 2, 2.82, -6.96],
          [1.83, 2.06, 2.24, -5.52]]

text = "{:^30}".format("Виконав") + "\n" + "{:^30}".format("Калайда Тарас") + "\n" + "{:^30}".format(
    "Студент групи ІВ-93") + "\n" + "{:^30}".format("Варіант 8")


def vidnim(a, b, index):
    for i in range(len(a)):
        tmp = a[i][index] / b[index]
        for j in range(len(a[0])):
            a[i][j] = a[i][j] - b[j] * tmp

    a.insert(index, b)
    return a


def gaus(matrix):
    index = 0
    new_tmp = 0
    max_int = matrix[0][0]

    for i in range(len(matrix)):
        if max_int < matrix[i][0]:
            max_int = matrix[i][0]
            index = i

    temp = matrix[0]
    matrix[0] = matrix[index]
    matrix[index] = temp

    for t in range(len(matrix)):
        delen = matrix[new_tmp][new_tmp]
        for i in range(len(matrix[new_tmp])):
            matrix[new_tmp][i] = matrix[new_tmp][i] / delen
        matrix_copy = copy.deepcopy(matrix)
        virez = matrix_copy.pop(new_tmp)
        matrix = vidnim(matrix_copy, virez, new_tmp)
        new_tmp += 1

    for i in range(len(matrix)):
        matrix[i][-1] = round(matrix[i][-1], 3)
    return matrix


class Main:
    def __init__(self):
        self.n, self.m = 3, 4
        self.entry_list = []
        self.new_list = []
        self.koef_list = []

        self.root = Tk()

        Button(self.root, width=12, text="Обрахувати", font=("Times", 13), command=self.result).place(x=400, y=45)
        Button(self.root, width=12, text="Стерти", font=("Times", 13), command=self.clear).place(x=400, y=95)
        Button(self.root, width=12, text="Варіант", font=("Times", 13), command=self.variant).place(x=400, y=145)

        Label(self.root, text="Розв'язування СЛАР", font=("Times", 20), bg="#90EE90").place(x=550, y=50)
        Label(self.root, text="Методом одиничних коефіцієнтів", font=("Times", 20), bg="#90EE90").place(x=550, y=90)

        self.text = Text(self.root, font=("Times", 15), width=32, height=1, bd=1)

        self.menu = Menu(self.root)
        self.mainmenu = Menu(self.menu, tearoff=0)

        self.entry_func()
        self.text_func()
        self.menu_func()

        self.root_func()

    def new_win(self):
        self.window = Toplevel(self.root)
        self.window.title("Інфо")
        self.window.geometry("280x180")

        self.label3 = Label(self.window, text=text, font="Ariel 18", width=20, height=15, bg="yellow").place(x=0,
                                                                                                             y=-115)

    def root_func(self):
        self.root.title("Lab5")
        self.root.geometry("1000x250")
        self.root["bg"] = "#90EE90"
        self.root.mainloop()

    def variant(self):
        for i in range(self.n):
            for j in range(self.m):
                self.entry_list[i][j].delete(0, END)
                self.entry_list[i][j].insert(0, m_list[i][j])

    def entry_func(self):
        x1, y1 = 0, 0

        for i in range(self.n):
            y1 += 50
            x1 = 0
            self.entry_list.append([])
            for j in range(self.m):
                x1 += 75
                self.entry = Entry(self.root, width=6, font=("Times", 14))
                self.entry.place(x=x1, y=y1)
                self.entry_list[i].append(self.entry)

        self.variant()

    def menu_func(self):
        self.menu.add_cascade(label="Меню", menu=self.mainmenu)
        self.mainmenu.add_command(label="Інфо", command=self.new_win)
        self.root.configure(menu=self.menu)

    def result(self):
        try:

            self.new_list = []

            for i in range(self.n):
                self.new_list.append([])
                for j in range(self.m):
                    self.new_list[i].append(float(self.entry_list[i][j].get()))

            final = gaus(self.new_list)
            self.text.delete(1.0, END)

            for i in range(len(final)):
                self.text.insert(1.0, " x" + str(i + 1) + " = " + str(final[i][3]) + ",")

        except(ZeroDivisionError, IndexError):

            self.text.delete(1.0, END)
            self.text.insert(1.0, "Помилка")

    def text_func(self):
        self.text.insert(1.0, "Відповідь:")
        self.text.place(x=75, y=200)

    def clear(self):
        self.new_list = []

        for i in range(self.n):
            for j in range(self.m):
                self.entry_list[i][j].delete(0, END)
                self.entry_list[i][j].insert(0, 0)

        self.text.delete(1.0, END)
        self.text.insert(1.0, "Відповідь:")


if __name__ == "__main__":
    t = Main()
