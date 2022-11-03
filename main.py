#! python3
""" Dette er et testprogram med Tkinter. 
Skrevet af frank@simens.dk
Skrevet i Python på Ubuntu 22.10 Brude virke på forskellige linux med korrekt phyton version og tkinter."""

from tkinter import *
from tkinter import messagebox

import os


# add widgets here
window=Tk()
window.title('Showinfo')
window.geometry("500x300+20+20")

def close():
    window.destroy()

def about():
        svar = messagebox.askokcancel('About', 'Contact frank@simens.dk \nProjektet kan findes på https://github.com/Hvemmse/ \nLicens GPL 3 \nhttps://www.112support.dk"')

        if svar:
            messagebox.showinfo('Tak', 'Tak Fordi du bruger programmet')
            


def kopier():
    os.system("cat ./status.txt | xsel -i -b")
    
def visinfo():
    os.system("sh ./status > status.txt")
    
    f = open("./status.txt", "r")
    data = f.read()
    txtarea.insert (END, data)

lbl=Label(window, text="Her vises nogle info om systemet.", fg='black', font=("Helvetica", 14))
lbl.place(x=20, y=40)

#definer knapper for neden i Programmet

txtarea = Text(window, width=60, height=30)
txtarea.pack(pady=60)

btnLuk = Button(window, text='luk', command=close)
btnLuk.bind('<Button-1>')
btnLuk.place(x=40, y=260)

btnOK = Button(window, text='About', command=about)
btnOK.bind('<Button-1>')
btnOK.place(x=90, y=260)

btnUdskriv = Button(window, text='Kopier', command=kopier)
btnUdskriv.bind('<Button-1>')
btnUdskriv.place(x=155, y=260)

btnVisInfo = Button(window, text='VisInfo', command=visinfo)
btnVisInfo.bind('<Button-1>')
btnVisInfo.place(x=225, y=260)

window.mainloop()
