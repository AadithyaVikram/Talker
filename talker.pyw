from tkinter import *
import pyttsx3
import keyboard
text_box=Tk()
text_box.title("TALKER")

editor=Text()
editor.pack()
def spe():
    a = editor.get("1.0", END)
    pyttsx3.speak(a)
    editor.delete("1.0", END)
def clr():
    editor.delete("1.0",END)
keyboard.add_hotkey("ctrl+a+s", spe)

menu_bar=Menu(text_box)
menu_bar.add_command(label="Speak (ctrl+a+s)",command=spe)
menu_bar.add_command(label="Clear",command=clr)
menu_bar.add_command(label="Quit",command=quit)
text_box.config(menu=menu_bar)

my_label=Label(text_box,text="text in the above box to speak \n speak button shortcut is 'ctrl+a+s'")
my_label.pack()

text_box.mainloop()
