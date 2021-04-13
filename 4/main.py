from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
print("Моя")
class Main:
    def __init__(self):
        self.window()
    def window(self):
        self.root=Tk()
        self.root["bg"]="yellow"
        self.root.geometry("700x300")
        self.root.title("Main")
        Label(self.root, text="Розв'язок нелінійного рівняння", bg="yellow", font=("Times", 20)).place(x=50, y=25)
        Label(self.root, text="методом дотичних sin^2(x+pi/2)-x^2/4", bg="yellow", font=("Times", 20)).place(x=50, y=60)
        Label(self.root, text="Від", bg="yellow", font=("Times", 15)).place(x=50,y=100)
        Label(self.root, text="До", bg="yellow", font=("Times", 15)).place(x=200, y=100)
        Label(self.root, text="Точність", bg="yellow", font=("Times", 15)).place(x=350, y=100)
        self.main_label = Label(self.root, text="", bg="yellow", font=("Times", 15))
        self.main_label.place(y=250, x=50)
        self.entry1=Entry(self.root, width=10, font=("Times", 15))
        self.entry1.insert(END,-2)
        self.entry1.place(x=50,y=125)
        self.entry2=Entry(self.root, width=10, font=("Times", 15))
        self.entry2.insert(END, 2)
        self.entry2.place(x=200,y=125)
        self.entry3 = Entry(self.root, width=10, font=("Times", 15))
        self.entry3.insert(END, 0.001)
        self.entry3.place(x=350, y=125)
        Button(self.root, width=12,text="Обрахувати",bg='chartreuse', font=("Times", 15),command=self.result).place(x=50,y=175)
        Button(self.root, width=12,text="Графік",bg='chartreuse', font=("Times", 15),command=self.graphic).place(x=250,y=175)
        self.root.mainloop()

    def graphic(self):
        x = np.arange(int(self.entry1.get()), int(self.entry2.get()), float(self.entry3.get()))
        y=(np.sin(x+np.pi/2)**2)-(x**2)/4
        fig = plt.figure()
        ax = fig.add_subplot(111, label="1")
        ax.plot(x, y, color="C1")
        ax.set_xlabel("sin^2(x+pi/2)-x^2/4", color="C1")
        ax.tick_params(axis='x', colors="C1")
        ax.tick_params(axis='y', colors="C1")
        if float(self.entry1.get())<self.second:
            plt.scatter(self.second, (np.sin(self.second+np.pi/2)**2)-(self.second**2)/4,c="r")
        if float(self.entry2.get())>self.first:
            plt.scatter(self.first, (np.sin(self.first + np.pi / 2) ** 2) - (self.first ** 2) / 4, c="r")
        plt.show()



    def yrav(self,x):
        y = (np.sin(x + np.pi / 2) ** 2) - (x ** 2) / 4
        return y

    def proz(self,x):
        f_ = -x / 2 - 2 * np.sin(x) * np.cos(x)
        return f_

    def counts(self,t):
        while True:
            f=self.yrav(t)
            f_=self.proz(t)
            h=f/f_
            t=t-h
            if h<0.001:
                return t

    def result(self):
        self.first=self.counts(1)
        self.second=self.counts(3)

        if float(self.entry1.get()) < self.second:
            self.main_label=Label(self.root, text="Відповідь:"+str(self.second), bg="yellow", font=("Times", 15))
            self.main_label.place(y=250, x=50)
        if float(self.entry2.get()) > self.first:
            self.main_label=Label(self.root, text="Відповідь:" + str(self.first), bg="yellow", font=("Times", 15))
            self.main_label.place(y=250, x=50)
        if float(self.entry2.get()) > self.first and float(self.entry1.get()) < self.second:
            self.main_label=Label(self.root, text="Відповідь:" + str(self.first)+", "+str(self.second), bg="yellow", font=("Times", 15))
            self.main_label.place(y=250, x=50)

if __name__ =="__main__":
   t=Main()