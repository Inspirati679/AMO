from tkinter import *
import random
from time import process_time as clock

text2 = "{:^30}".format("Виконав") + "\n" + "{:^30}".format("Калайда Тарас") + "\n" + "{:^30}".format(
    "Студент групи ІВ-93") + "\n" + "{:^30}".format("Варіант 8")
class Main:
    def __init__(self):
        self.main_window()


    def main_window(self):
        self.root = Tk()
        self.root["bg"] = "yellow"
        self.root.geometry("745x400")
        self.root.title("Головне вікно")
        self.entry = Entry(self.root, width=70, font=("Times", 15))
        self.entry.bind('<Button-1>', self.change)
        self.entry.place(x=20, y=50)
        self.entry.insert(0, "Введіть розмір")
        self.button_1 = Button(self.root, width=20, font=("Times", 15), text="Сформувати випадково",
                               command=self.make,bg='chartreuse').place(x=100, y=150)
        self.button_2 = Button(self.root, width=20, font=("Times", 15), text="Очистити",
                               command=self.clear,bg='chartreuse').place(x=100, y=300)
        self.button_3 = Button(self.root, width=20, font=("Times", 15), text="Посортувати",
                               command=self.sort,bg='chartreuse').place(x=100, y=220)
        self.button_4 = Button(self.root, width=20, font=("Times", 15), text="Зчитати",
                               command=self.read,bg='chartreuse').place(x=400, y=150)
        self.menu = Menu(self.root)
        self.mainmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Меню", menu=self.mainmenu)
        self.mainmenu.add_command(label = "Інфо", command = self.new_window)
        self.root.configure(menu=self.menu)
        self.label = Label(self.root, text="", bg="yellow")
        self.label.place(x=300, y=100)
        self.label2 = Label(self.root, text="Час = ", bg="yellow", font=("Times", 15))
        self.label2.place(x=400, y=300)

        self.root.mainloop()
    def new_window(self):
        self.window=Toplevel(self.root)
        self.window.title("Інфо")
        self.window.geometry("280x180")
        self.label3 = Label(self.window, text=text2, font="Ariel 18", width=20, height=15, bg="yellow").place(x=0,y=-115)


    def change(self, event):
        if self.entry.get() == "Введіть розмір":
            self.entry.delete(0, END)

    def make(self):
        try:
            self.N = int(self.entry.get())
            self.main_mass = []
            for i in range(self.N):
                self.main_mass.append(random.randint(-999, 999))
            self.entry.delete(0, END)
            self.entry.insert(0, self.main_mass)
        except ValueError:
            self.label.place_forget()
            self.label = Label(self.root, text="Помилка", font=("Times", 15), bg="yellow", fg="red")
            self.label.place(x=300, y=100)
        else:
            self.label.place_forget()
            self.label = Label(self.root, text="", font=("Times", 15), bg="yellow", fg="red")
            self.label.place(x=300, y=100)

    def clear(self):
        self.main_mass = []
        self.entry.delete(0, END)
        self.entry.insert(0, "Введіть розмір")

    def sort(self):
        try:
            self.main_mass = self.entry.get().split(" ")

            for i in range(len(self.main_mass)):
                self.main_mass[i] = int(self.main_mass[i])
            self.N = len(self.main_mass)

            t1 = clock()
            for i in range(self.N):
                self.max = max(self.main_mass[i:self.N])
                del self.main_mass[
                    self.main_mass[i:self.N].index(self.max) + i:self.main_mass[i:self.N].index(self.max) + i + 1]
                self.main_mass.insert(i, self.max)
            self.main_mass = list(reversed(self.main_mass))

            self.entry.delete(0, END)
            self.entry.insert(0, self.main_mass)
            t2 = clock()
            self.T = t2 - t1
            self.label2.place_forget()
            self.root.update()
            self.label2 = Label(self.root, text="Час = "+str(self.T), font=("Times", 15), bg="yellow", fg="red")
            self.label2.place(x=400, y=300)

            # self.new_mass=[]
            # for i in range(len(self.main_mass)):
            #     self.max=max(self.main_mass)
            #     self.new_mass.append(self.max)
            #     self.main_mass.remove(self.max)
            # print(list(reversed(self.new_mass)))new_mass
        except ValueError:
            self.label.place_forget()
            self.label = Label(self.root, text="Помилка", font=("Times", 15), bg="yellow", fg="red")
            self.label.place(x=300, y=100)
        else:
            self.label.place_forget()
            self.label = Label(self.root, text="", font=("Times", 15), bg="yellow", fg="red")
            self.label.place(x=300, y=100)

    def read(self):
        try:
            t = open("Read.txt", mode="r")
            read = t.read()
            self.main_mass = read.split(" ")
            for i in range(len(self.main_mass)):
                self.main_mass[i] = int(self.main_mass[i])
            self.entry.delete(0, END)
            self.entry.insert(0, self.main_mass)
            self.N = len(self.main_mass)
        except ValueError:
            self.label.place_forget()
            self.label = Label(self.root, text="Помилка", font=("Times", 15), bg="yellow", fg="red")
            self.label.place(x=300, y=100)
        else:
            self.label.place_forget()
            self.label = Label(self.root, text="", font=("Times", 15), bg="yellow", fg="red")
            self.label.place(x=300, y=100)



if __name__ == "__main__":
    t = Main()
