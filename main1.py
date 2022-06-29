from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry("750x400")
root.configure(bg='ghost white')
root.title("Group 1- TEXT TO SPEECH")

# Main Functions
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save(f'{Message}.mp3')
    playsound(f'{Message}.mp3')
    os.remove(f'{Message}.mp3')


def Reset():
    Msg.set("")

def Exit():
    root.destroy()

panel = Frame(root)
panel.place(x=50,y=50)

img=PhotoImage(file='tts.png')
imgLbl = Label(panel,image=img)
imgLbl.grid(rowspan=4,column=0)

Label(root, text = "Dumb Module", font = "Arial 20 bold", bg='white smoke').pack()
Label(text ="Group 1", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 20 bold', bg ='white smoke').place(x=400,y=100)

entry_field = Entry(root, textvariable = Msg ,width ='500')
entry_field.place(x=330,y=150)

Button(root, text = "PLAY", font = 'arial 15 bold' , width = '5',bg='light blue',command=Text_to_speech).place(x=330,y=240)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '5' , bg = 'Orange',command=Exit).place(x=420 , y = 240)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' ,command=Reset).place(x=510 , y = 240)


root.mainloop()
