import tkinter as tk
# from tkinter import font
from random import randint
import time

m=tk.Tk()
w = tk.Canvas(m, width=1000, height=1000) 
w.pack() 
canvas_height=150
canvas_width=2000
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
w.create_text (canvas_width /4,
              canvas_height / 5,
              text="Welcome to Tambola's number caller \n                                 Based on Python \n                                           -By Kavish")
shape = w.create_rectangle(400, 995, 995, 100, fill='white')
myCanvas = tk.Canvas(m, height=300, width=300)
myCanvas_width= 600
myCanvas_height= 575
w.create_text(myCanvas_width /4,
              myCanvas_height / 5,
              text="Number is : ")
w.create_rectangle(300, 350, 20, 100,)
w.create_rectangle(300, 350, 20, 135, fill="white")

noCanvas = tk.Canvas(m, height=300, width=300)
noCanvas_width= 600
noCanvas_height= 1100

drawn_numbers = list()
bingo_draw=randint(1,90)
if not bingo_draw in drawn_numbers:
    w.create_text(noCanvas_width /4,
        noCanvas_height / 5,
        text = bingo_draw)
drawn_numbers.append(bingo_draw)
time.sleep(10)



m.mainloop()

