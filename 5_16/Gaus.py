import copy
from tkinter import *
import numpy as np

matrix = [[10, 1, 1, 12], [2, 10, 1, 13], [2, 2, 10.0, 14]]


def check(a):
    diag = np.diag(np.abs(a))

    off_diag = np.sum(np.abs(a), axis=1) - diag

    if np.all(diag > off_diag):
        return True
    else:
        return False


def Gaus(matrix):
    index = 0
    max_int = matrix[0][0]

    for i in range(len(matrix)):
        if max_int < matrix[i][0]:
            max_int = matrix[i][0]
            index = i

    temp = matrix[0]
    matrix[0] = matrix[index]
    matrix[index] = temp

    n = len(matrix)
    m = n + 1
    c = []
    for i in range(n):
        c.append(matrix[i][i])
    for i in range(n):
        for j in range(m):
            if j == m - 1:
                print(matrix[i][j])
                matrix[i][j] = matrix[i][j] / c[i]
            else:
                matrix[i][j] = matrix[i][j] / c[i] * -1

        matrix[i][i] = matrix[i][j]
        del matrix[i][j]


    t = []

    for i in range(n):
        t.append(0)


    while True:
        r = copy.deepcopy(t)
        tmp_matrix = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                if i != j:
                    tmp_matrix[i][j] *= t[j]


            c = sum(tmp_matrix[i])

            t[i] = c

        y = []
        for i in range(n):
            y.append(abs(t[i] - r[i]))
        if sum(y) < 0.000001:
            break


    for i in range(len(t)):
        t[i] = round(t[i], 3)


    return t


def etry_make():
    y = 0
    for i in range(3):
        entry_list.append([])
        y += 50
        x = 0
        for j in range(4):
            if j != 3:
                Label(root, text="x" + str(j + 1) + " *", font=("Times", 14), bg="#00FFFF").place(x=x + 80, y=y)
            if j == 3:
                x += 150
            else:
                x += 120
            entry = Entry(root, width=6, font=("Times", 14))
            entry.insert(0, 0)
            entry_list[i].append(entry)
            entry.place(x=x, y=y)
        Label(root, text="=", font=("Times", 14), bg="#00FFFF").place(x=x - 60, y=y)


def new_win():
    main_list = []
    no_b = []
    for i in range(3):
        no_b.append([])
        for j in range(3):
            no_b[i].append(float(entry_list[i][j].get()))
    for i in range(3):
        main_list.append([])
        for j in range(4):
            main_list[i].append(float(entry_list[i][j].get()))
    if check(no_b) == True:
        t = Gaus(main_list)
    else:
        t = ["Помилка", "Помилка", "Помилка"]
    win = Toplevel(root)
    win["bg"] = "#FFD700"
    win.title("Результат")
    win.geometry("230x180")
    x, y = 30, 30
    for i in range(3):
        Label(win, text="x" + str(i + 1) + " = " + str(t[i]), font=("Times", 20), bg="#FFD700").place(x=x, y=y)
        y += 50


def primer():
    for i in range(3):
        for j in range(4):
            entry_list[i][j].delete(0, END)
            entry_list[i][j].insert(0, matrix[i][j])


def clear():
    global main_list
    main_list = []
    for i in range(3):
        for j in range(4):
            entry_list[i][j].delete(0, END)
            entry_list[i][j].insert(0, 0)


if __name__ == '__main__':
    main_list = []
    entry_list = []

    root = Tk()
    root.geometry("650x270")
    root.title("Головне вікно")
    root["bg"] = "#00FFFF"

    Button(root, font=("Times", 14), text="Результат", bg="#800080", command=new_win, width=12).place(x=120, y=200)
    Button(root, font=("Times", 14), text="Приклад", bg="#800080", command=primer, width=12).place(x=270, y=200)
    Button(root, font=("Times", 14), text="Обнулити", bg="#800080", command=clear, width=12).place(x=420, y=200)
    Label(root, text="Виконав Мельник Антон, ІВ-93", font=("Times", 20), bg="#00FFFF").place(x=140, y=0)

    etry_make()
    root.mainloop()
