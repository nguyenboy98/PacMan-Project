import tkinter
from cmath import *
import numpy as np
import cv2
import pygame
from setting import *
from tkinter import *
from tkinter import messagebox


# def creat_board():
#     board= np.zeros((8,8))
#     return board
# board= creat_board()
# print(board)

top=Tk()
C = Canvas(top, bg="blue", height=250, width=300)
filename = tk.PhotoImage(file = "D:\\Nguyen\\Python Project\\DSA Project\\map.jpg")
background_label = top.Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop