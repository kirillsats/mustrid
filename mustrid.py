from tkinter import *
from tkinter import font  # vajalik teksti fondi muutmiseks
from random import choice
import tkinter as tk
import time

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.grid()

# üksik kriips (x0, y0, x1, y1)
tahvel.create_line(30, 40, 300, 40)

# ühendatud kriipsud (suvaline arv koordinaatide paare)
tahvel.create_line(30, 60, 300, 60, 300, 100, 60, 100)

# võimalik on muuta joone paksust (width) ja sisu värvi (fill)
tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

# teistsugune joone stiil
tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

# tõmbab kriipsud, ühendab otsapunktid ja värvib sisu
# värve saab määrata ka rgb komponentidena
# vt. http://www.colorpicker.com/
tahvel.create_polygon(30, 160, 300, 160, 300, 200, 60, 200, fill="#95BD9D")

# ristkülik
tahvel.create_rectangle(30, 260, 300, 300)

# ovaal
tahvel.create_oval(30, 260, 300, 300, width=2, outline="blue", fill="wheat")

# proovi liigutada hiirt selle ovaali kohale
tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

# kui soovid teksti esitamisel ise fonti valida, siis tuleb enne vastav font luua
suur_font = font.Font(family='Helvetica', size=32, weight='bold')
tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)

colors = ["black",
          "cyan",
          "magenta",
          "red",
          "blue",
          "gray",
          "yellow",
          "green",
          "lightblue",
          "pink",
          "gold"]

def ooval():
    root = tk.Tk()
    root.title("Oval")
    canvas = tk.Canvas(root, width=800, height=800, bg = "white")
    canvas.pack()

    x0 = 0
    y0 = 0
    x1 = 600
    y1 = 600
    p = 2
    for i in range(150):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors))
    root.mainloop()


import tkinter as tk

def Estonian_flag():
    root = tk.Tk()
    root.title("Estonian Flag")
    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()
    width = 300
    height = 200
    stripe_height = height // 3
    # sinine
    canvas.create_rectangle(0, 0, width, stripe_height, fill="#0072CE", outline="")
    # must
    canvas.create_rectangle(0, stripe_height, width, 2 * stripe_height, fill="#000000", outline="")
    # valge
    canvas.create_rectangle(0, 2 * stripe_height, width, height, fill="#FFFFFF", outline="")
    root.mainloop()

def Russia_flag():
    root = tk.Tk()
    root.title("Russian Flag")
    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()
    width = 300
    height = 200
    stripe_height = height // 3
    # valge
    canvas.create_rectangle(0, 0, width, stripe_height, fill="#FFFFFF", outline="")
    # sinine
    canvas.create_rectangle(0, stripe_height, width, 2 * stripe_height, fill="#0000FF", outline="")
    # punane
    canvas.create_rectangle(0, 2 * stripe_height, width, height, fill="#FF0000", outline="")
    root.mainloop()

#  Багамскиe островa
def bagami():
    root = tk.Tk()
    root.title("Russian Flag")
    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()
    width = 300
    height = 200
    stripe_height = height // 3
    # sinine
    canvas.create_rectangle(0, 0, width, stripe_height, fill="#008B8B", outline="")
    # kollane
    canvas.create_rectangle(0, stripe_height, width, 2 * stripe_height, fill="#FFFF00", outline="")
    # sinine
    canvas.create_rectangle(0, 2 * stripe_height, width, height, fill="#008B8B", outline="")
    canvas.create_polygon(0, 0, width - 140, height / 2, 0, height, fill="#000000", outline="")
    root.mainloop()

def pilt2():
    x0 = 0
    y0 = 0
    x1 = 600
    y1 = 600
    p = 0
    x_ =600
    x_ = 600
    y_ = 600
    for i in range(20):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        tahvel.create_rectangle(x0, y0, x1, y1, fill=choice(colors))
        tahvel.create_oval(x0, y0, x1, y1, fill=choice(colors))
        x_ -= 2 * p
        y_ -= 2 * p
        p = int(((x_ ** 2 + y_ ** 2) ** (1 / 2) - x_) / 2)
        p = int(((p ** 2) / 2) ** (1 / 2))



def valgusfor():
    tahvel.delete("all")
    root = tk.Tk()
    root.title("Valgusfor")
    canvas = tk.Canvas(root, width=100, height=300, bg="white")
    canvas.pack()

    red_light = canvas.create_oval(25, 25, 75, 75, fill="black")
    yellow_light = canvas.create_oval(25, 125, 75, 175, fill="black")
    green_light = canvas.create_oval(25, 225, 75, 275, fill="black")

    while True:
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="black")
        canvas.itemconfig(green_light, fill="black")
        root.update()  # Värskendame akent, et muudatused oleksid nähtavad
        time.sleep(2)  # Oota 2 sekundit
        canvas.itemconfig(red_light, fill="black")
        canvas.itemconfig(yellow_light, fill="yellow")
        root.update()  # Värskendame akent, et muudatused oleksid nähtavad
        time.sleep(1)  # Oota 1 sekund
        canvas.itemconfig(yellow_light, fill="black")
        canvas.itemconfig(green_light, fill="green")
        root.update()  # Värskendame akent, et muudatused oleksid nähtavad
        time.sleep(2)  # Oota 2 sekundit
        canvas.itemconfig(green_light, fill="black")
        root.update()  # Värskendame akent, et muudatused oleksid nähtavad

    root.mainloop()


def doska():
    tahvel.delete("all")
    size = 500
    rows = 8
    cols = 8
    square_size = size // max(rows, cols)
    colors = ["white", "black"]
    for row in range(rows):
        for col in range(cols):
            color_index = (row + col) % 2  # Alternating colors
            color = colors[color_index]
            x0 = col * square_size
            y0 = row * square_size
            x1 = x0 + square_size
            y1 = y0 + square_size
            tahvel.create_rectangle(x0, y0, x1, y1, fill=color, outline="", tags="item")

var = tk.IntVar()
ovall = tk.Radiobutton(raam, text='Oval', variable=var, value=1, font=suur_font, command=ooval)
Estonia = tk.Radiobutton(raam, text='Estonian flag', variable=var, value=2, font=suur_font, command=Estonian_flag)
ovall.grid(row=0, column=1)
Estonia.grid(row=1, column=1)
Russia = tk.Radiobutton(raam, text='Russian flag', variable=var, value=3, font=suur_font, command=Russia_flag)
Russia.grid(row=2, column=1)
Bagami = tk.Radiobutton(raam, text='Bagamskie ostrova', variable=var, value=4, font=suur_font, command=bagami)
Bagami.grid(row=3, column=1)
Pilt = tk.Radiobutton(raam, text='Pilt', variable=var, value=5, font=suur_font, command=pilt2)
Pilt.grid(row=4, column=1)
Valgusfor = tk.Radiobutton(raam, text='Valgusfor', variable=var, value=6, font=suur_font, command=valgusfor)
Valgusfor.grid(row=5, column=1)
Doska = tk.Radiobutton(raam, text='Doska', variable=var, value=7, font=suur_font, command=doska)
Doska.grid(row=6, column=1)
raam.mainloop()





