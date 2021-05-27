##  Import:

from tkinter import *

##  On définit et on calibre notre fenêtre:
fen=Tk()
fen.title("Reconnaisance de signature")
fen.geometry("1000x900")
fen.config(bg='#808080')
fen.resizable(width=False, height=False)

##  On définit une zone pour la signature:

zone=Frame(width=500, height=500, bg='#FFFFFF')
zone.place(x=250, y=200)

##  On place un titre:

titre=Label(fen, text="Signez dans le cadre ci-dessous", height=2, fg='#FFFFFF', bg='#808080', font=("Parchment",50))
titre.place(x=200, y=0)

##  On demande si la personne souhaite conserver cette signature:

confirmation=Label(fen, text="Etes-vous satifait(e) de votre signature?", height=1, fg='#FFFFFF', bg='#808080', font=("Parchment",50))
confirmation.place(x=117, y=677)

##  On définit les boutons pour répondre:

OUI=Button(fen, text="oui", height=1, fg='#000000', bg='#00FF00', font=("Parchment",25), relief=RAISED)
OUI.place(x=365, y=777)

NON=Button(fen, text="non", height=1, fg='#000000', bg='#FF0000', font=("Parchment",25), relief=RAISED, command=non)
NON.place(x=735, y=777)

def non():
    zone.pack_forget()

fen.mainloop()