from tkinter import *
import random
import matplotlib.pyplot as plt
from time import process_time as clock
import numpy as np


def rand():
    global main_mass
    lenght = int(entry.get())
    main_mass = []
    for i in range(lenght):
        main_mass.append(random.randint(0, 1000))
    text1.delete(1.0, END)
    text1.insert(1.0, main_mass)


def clear():
    global main_mass
    main_mass = []
    text1.delete(1.0, END)
    text1.insert(1.0, main_mass)


def read():
    global main_mass
    t = open("new_read.txt", mode="r")
    read = t.read()
    main_mass = read.split(" ")
    for i in range(len(main_mass)):
        main_mass[i] = int(main_mass[i])
    text1.delete(1.0, END)
    text1.insert(1.0, main_mass)


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = int((start + end) / 2)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


def sort():
    global main_mass, sorted_mass
    t1 = clock()
    sorted_mass = insertion_sort(main_mass)
    t2 = clock()
    T = t2 - t1
    text2.delete(1.0, END)
    text2.insert(1.0, sorted_mass)
    text3.delete(1.0, END)
    text3.insert(1.0, "Час - " + str(T))


def graphic():
    int_mass = [1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250]
    t_mass, t_mass2 = [], []
    for i in range(10):
        mass = []
        for j in range(int_mass[i]):
            mass.append(random.randint(-10000, 10000))

        t1 = clock()
        sort_mass = insertion_sort(mass)
        t2 = clock()
        T = t2 - t1
        t_mass.append(round(T, 10))
        t_mass2.append(int_mass[i] * np.log(int_mass[i]))
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    print(t_mass)
    ax.plot(int_mass, t_mass, color="C3")
    ax.set_xlabel("Практично", color="C3")
    ax.tick_params(axis='x', colors="C3")
    ax.tick_params(axis='y', colors="C3")
    ax2.plot(int_mass, t_mass2, color="C5")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('Теоретично', color="C5")
    ax2.xaxis.set_label_position('top')
    ax2.tick_params(axis='x', colors="C5")
    ax2.tick_params(axis='y', colors="C5")
    plt.show()


root = Tk()
root["bg"] = "magenta"
root.geometry("875x500")
root.title("Main Window")
entry = Entry(root, width=77, font=("Times", 15))
entry.place(x=50, y=100)

text1 = Text(root, width=77, height=3, bd=2, font=('Times', 15))
text1.place(y=150, x=50)
Button(root, command=rand, font=("Times", 15), bg='chartreuse', width=15, text="Random").place(y=250, x=50)
Button(root, command=clear, font=("Times", 15), bg='chartreuse', width=15, text="Clear").place(y=250, x=250)
Button(root, command=read, font=("Times", 15), bg='chartreuse', width=15, text="Read").place(y=250, x=450)
Button(root, command=sort, font=("Times", 15), bg='chartreuse', width=15, text="Sort").place(y=250, x=650)
Button(root, command=graphic, font=("Times", 15), bg='chartreuse', width=15, text="Graphic").place(y=410, x=450)
text2 = Text(root, width=77, height=3, bd=2, font=('Times', 15))
text2.place(y=320, x=50)
text3 = Text(root, width=20, height=1, bd=2, font=('Times', 15))
label = Label(root, text="{:^30}".format("Виконав") + "\n" + "{:^30}".format("Мельник Антон") + "\n" + "{:^30}".format(
    "Студент групи ІВ-93") + "\n" + "{:^30}".format("Варіант 16"), bg='magenta', font=("Times", 15)).place(x=330, y=0)

text3.place(y=420, x=50)
text3.insert(1.0, "Час - ")
root.mainloop()
