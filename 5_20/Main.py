from tkinter import *
import copy


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


def sec_win():
    global entry_list

    win = Toplevel(root)
    win["bg"] = "#4B0082"
    win.title("Matrix")

    entry_list = []

    x, y = form_entry(int(entry1.get()), int(entry1.get()) + 1, win)

    Button(win, font=("Times", 14), text="Отримати результат", bg="#DC143C", command=res_win, width=18).place(x=x + 70,
                                                                                                              y=42)
    Button(win, font=("Times", 14), text="Вставити", bg="#DC143C", command=paste, width=18).place(x=x + 70, y=92)
    Button(win, font=("Times", 14), text="Очистити", bg="#DC143C", command=clear, width=18).place(x=x + 70, y=142)

    win.geometry(str(x + 320) + "x" + str(y + 80))


def form_entry(n, m, window, y=0, ):
    for i in range(n):
        x = 0
        y += 50
        entry_list.append([])
        for j in range(m):

            if j == m - 1:
                x += 100
            else:
                x += 75

            entry = Entry(window, width=6, font=("Times", 14))
            entry_list[i].append(entry)
            entry_list[i][j].insert(0, 0)
            entry.place(x=x, y=y)

    return x, y


def paste():
    if int(entry1.get()) == 3:
        for i in range(int(entry1.get())):
            for j in range(int(entry1.get()) + 1):
                entry_list[i][j].delete(0, END)
                entry_list[i][j].insert(0, matrix[i][j])


def clear():
    for i in range(int(entry1.get())):
        for j in range(int(entry1.get()) + 1):
            entry_list[i][j].delete(0, END)
            entry_list[i][j].insert(0, 0)


def res_win():
    win_res = Toplevel(root)
    win_res.title("Result")

    try:
        mass = []
        for i in range(int(entry1.get())):
            mass.append([])
            for j in range(int(entry1.get()) + 1):
                mass[i].append(float(entry_list[i][j].get()))

        new_mass = gaus(mass)
        x = 50
        y = 20

        for i in range(int(entry1.get())):
            Label(win_res, font=("Times", 14),
                  text="x" + str(i + 1) + " = " + str(new_mass[i][int(entry1.get())])).place(x=x, y=y)
            y += 50
        win_res.geometry("180x" + str(y))

    except (ZeroDivisionError, IndexError, ValueError):
        Label(win_res, font=("Times", 14), text="Помилка").place(x=50, y=50)
        win_res.geometry("180x130")


if __name__ == "__main__":
    matrix = [[1.14, -2.15, -5.11, 2.05], [0.42, -1.13, 7.05, 0.80], [-0.71, 0.81, -0.02, -1.07]]
    entry_list = []

    root = Tk()
    root["bg"] = "yellow"
    root.title("Lab5")
    root.geometry("480x230")

    Label(root, font=("Times", 20), text="Розв'язування лінійного рівняння", bg="yellow").place(x=50, y=0)
    Label(root, font=("Times", 20), text="Методом Гаусса", bg="yellow").place(x=140, y=30)
    Label(root, font=("Times", 20), text="Одиничних коефіцієнтів", bg="yellow").place(x=90, y=60)
    Label(root, font=("Times", 17), text="Кількість невідомих", bg="yellow").place(x=150, y=110)

    Button(root, font=("Times", 14), text="Сформувати", bg="#DC143C", command=sec_win).place(x=300, y=150)

    entry1 = Entry(root, width=6, font=("Times", 20))
    entry1.insert(0, 3)
    entry1.place(x=110, y=150)

    root.mainloop()
