from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Game To Play")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file='images\card_front.png')
canvas.create_image(400, 263, image=image)
canvas.grid(row=0, column=0, columnspan=2)
# canvas.pack()
# canvas.grid()
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text='fadf', font=("Ariel", 60, "bold"))

yes_button_image = PhotoImage(file='images\yes.png')
yes_button = Button(image=yes_button_image, highlightthickness=0)
yes_button.grid(row=1, column=0)

no_button_image = PhotoImage(file='images\wrong.png')
no_button = Button(image=no_button_image, highlightthickness=0)
no_button.grid(row=1, column=1)
window.mainloop()
