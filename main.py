import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("8.2")
window.geometry('520x300')
window.maxsize(520, 300)
window.resizable(1, 1)

import random, math

label_p1 = Label(text="Вер. 1:")
label_p1.place(x=10, y=10)

entry_p1 = Entry()
entry_p1.insert(0, "0.15")
entry_p1.place(x=54, y=10)

label_p2 = Label(text="Вер. 2:")
label_p2.place(x=10, y=40)

entry_p2 = Entry()
entry_p2.insert(0, "0.25")
entry_p2.place(x=54, y=40)

label_p3 = Label(text="Вер. 3:")
label_p3.place(x=10, y=70)

entry_p3 = Entry()
entry_p3.insert(0, "0.1")
entry_p3.place(x=54, y=70)

label_p4 = Label(text="Вер. 4:")
label_p4.place(x=10, y=100)

entry_p4 = Entry()
entry_p4.insert(0, "0.2")
entry_p4.place(x=54, y=100)

label_p4 = Label(text="Вер. 5:")
label_p4.place(x=10, y=130)

label_res_p5 = Label(text="auto")
label_res_p5.place(x=54, y=130)

label_trials = Label(text="Вер. 4:")
label_trials.place(x=10, y=160)

entry_trials = Entry()
entry_trials.insert(0, 10)
entry_trials.place(x=54, y=160)


import matplotlib.pyplot as plt

def button_clicked():
    p1 = float(entry_p1.get())
    p2 = float(entry_p2.get())
    p3 = float(entry_p3.get())
    p4 = float(entry_p4.get())
    p5 = 1 - p1 - p2 - p3 - p4
    label_res_p5.configure(text=p5)
    prob_arr = [p1, p2, p3, p4, p5]

    num_trials = int(entry_trials.get())



    values = []

    for i in range(num_trials):
        rand_value = random.random()
        comp_value = 0
        number = 0
        for prob in prob_arr:
            number += 1
            comp_value += prob
            if rand_value < comp_value:
                values.append(number)
                break
    plt.clf()
    plt.hist(values, bins=range(1, 7), edgecolor='black')
    plt.xlabel('Значения')
    plt.ylabel('Количество')
    plt.title('Гистограмма значений')
    plt.show()
    print(values)

button = tk.Button(window,
                   text="Построить гистограмму",
                   command=button_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   font=("Arial", 18))
button.place(x=10, y=210)

window.mainloop()
