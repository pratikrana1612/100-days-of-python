from tkinter import *

window=Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)


my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()
my_label["text"]="New Text"
my_label.config(text='new text')


def button_clicked():
    my_label['text']=input.get()

button=Button(text="Click Me",command=button_clicked)
button.pack()


input=Entry(width=10)
input.pack()

window.mainloop()
