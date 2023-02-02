import pandas
from tkinter import *
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


# print(data)

def yes_button_handler():
    word_changer(True)


def no_button_handler():
    word_changer(False)


def word_changer(flag):
    try:
        data = pandas.read_csv('data/words_to_learn.csv')
        
    except FileNotFoundError:
        data = pandas.read_csv('data/french_words.csv')
    if(flag):
        to_learn_dataFame.remove(dic)
    to_learn_dataFame = data.to_dict(orient='records')
    global filp_card
    window.after_cancel(filp_card)
    dic = choice(to_learn_dataFame)
    canvas.itemconfig(title, text=f"French", fill='black')
    canvas.itemconfig(word, text=f"{dic['French']}", fill='black')
    canvas.itemconfig(main_image, image=image_front)
    to_learn_dataFame.
    # .to_csv('word_to_learn.csv')
    # print(data[randint(1,len(data)-1)])
    filp_card = window.after(3000, card_change, dic)


def card_change(dic):
    canvas.itemconfig(main_image, image=image_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=dic['English'], fill='white')


window = Tk()
window.title("Flasy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# to change any thing on canvas we have to use main canvas
# canvas created
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

# image created
image_front = PhotoImage(file='images\card_front.png')
image_back = PhotoImage(file="images/card_back.png")

# image_seted
main_image = canvas.create_image(400, 263, image=image_front)
canvas.grid(row=0, column=0, columnspan=2)

# text created and seted on canvas
title = canvas.create_text(400, 150, text="French",
                           font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text='fadf', font=("Ariel", 60, "bold"))

yes_button_image = PhotoImage(file='images\yes.png')
yes_button = Button(image=yes_button_image,
                    highlightthickness=0, command=yes_button_handler)
yes_button.grid(row=1, column=0)

no_button_image = PhotoImage(file='images\wrong.png')
no_button = Button(image=no_button_image,
                   highlightthickness=0, command=no_button_handler)
no_button.grid(row=1, column=1)

filp_card = window.after(3000, card_change)
word_changer(False)


window.mainloop()
