from tkinter import *


def button_clicked():
    my_label['text']=input.get()

#window 
window=Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)


#label
my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label["text"]="New Text"
my_label.config(text='new text')
# my_label.pack(side="left")
# my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)
my_label.config(padx=20,pady=20)

#button
button=Button(text="Click Me",command=button_clicked)
button2=Button(text="new Button")
# button.pack(side="left")
button.grid(column=1,row=1)
button2.grid(row=0,column=2)

#input entry
input=Entry(width=10)
# input.pack(side="right")
input.grid(row=2,column=9)

window.mainloop()
