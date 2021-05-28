from tkinter import *

fen=Tk()
fen.title("Reconnaisance de signature")
fen.geometry("1000x900")
fen.config(bg='#000000')
fen.resizable(width=False, height=False)

can=Canvas(fen, width=1000, height=900, bg='#000000')
next=Button(fen, text="Continuer", height=1, fg='#000000', bg='white', font=("Parchment",50), relief=RAISED, command=page1)

def page0():
    home1=can.create_text(500, 200, text="Projet d'informatique", fill="white", font=("Parchment",80))
    home2=can.create_text(500, 450, text="La reconnaissance de signature", fill="white", font=("Parchment",80))
    home3=can.create_window(500, 700, window=next)

OUI=Button(fen, text="oui", height=1, fg='#000000', bg='#00FF00', font=("Parchment",25), relief=RAISED)
NON=Button(fen, text="non", height=1, fg='#000000', bg='#FF0000', font=("Parchment",25), relief=RAISED)

def page1():
    can.delete("all")
    titre=can.create_text(500, 100, text="Signez dans le cadre ci-dessous", fill='white', font=("Parchment",50))
    confirmation=can.create_text(500, 700, text="Etes-vous satifait(e) de votre signature?", fill='white', font=("Parchment",50))
    bouton1=can.create_window(350, 800, window=OUI)
    bouton2=can.create_window(650, 800, window=NON)
    zone=can.create_rectangle(300,200,700,600, fill='white')

page0()
can.pack()
fen.mainloop()
