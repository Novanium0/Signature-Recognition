from tkinter import *
from PIL import ImageGrab, Image, EpsImagePlugin
import win32gui
import os
import io

root=Tk()
root.title("Reconnaisance de signature")
root.geometry("1000x900")
root.config(bg='#000000')
root.resizable(width=False, height=False)

can=Canvas(root, width=1000, height=900, bg='#000000')

def page0():
    home1=can.create_text(500, 200, text="Projet d'informatique", fill="white", font=("Edwardian Script ITC",50))
    home2=can.create_text(500, 450, text="La reconnaissance de signature", fill="white", font=("Edwardian Script ITC",30))
    home3=can.create_window(500, 700, window=next)

def page1():
    can.delete("all")
    can.delete("home1")
    titre=can.create_text(500, 100, text="Signez dans le cadre ci-dessous :", fill='white', font=("Edwardian Script ITC",30))
    confirmation=can.create_text(500, 675, text="Etes-vous satisfait(e) de votre signature?", fill='white', font=("Edwardian Script ITC",30))
    bouton1=can.create_window(350, 800, window=OUI)
    bouton2=can.create_window(650, 800, window=NON)
    zone=can.create_rectangle(250, 200, 750, 600, fill='white')

def move(event):
    x,y=event.x,event.y
    x1,y1=x,y
    if can.old_coords:
        x1, y1 = can.old_coords
    can.old_coords = x, y
    can.create_line(x,y,x1,y1,width=3, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=1)

def trace(event):
    root.bind('<Motion>', move)

def untrace(event):
    root.unbind('<Motion>')
    can.old_coords = None

def non():
    can.delete("zone")
    zone=can.create_rectangle(250, 200, 750, 600, fill='white')

def oui():
    can.postscript(file='Signature.eps', colormode='color')
    img = Image.open('Signature.eps')
    A=img.save('C:\Python Scripts\Signature Recognition\Signature.eps')
    root.destroy()

next=Button(root, text="Continuer", height=1, fg='#000000', bg='white', font=("Edwardian Script ITC",30), relief=RAISED, command=page1)

OUI=Button(root, text="oui", height=1, fg='#000000', bg='#00FF00', font=("Edwardian Script ITC",20), relief=RAISED, command=oui)
NON=Button(root, text="non", height=1, fg='#000000', bg='#FF0000', font=("Edwardian Script ITC",20), relief=RAISED, command=non)

root.bind('<Button-1>', trace)
root.bind('<ButtonRelease-1>', untrace)
can.old_coords = None

page0()

can.pack()
root.mainloop()
