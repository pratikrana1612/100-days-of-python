from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


input = Entry(width=10)
input.grid(row=0, column=1)


miles_label = Label(text="Miles", padx=20, pady=15)
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is_equal_to", padx=20, pady=15)
is_equal_to_label.grid(row=1, column=0)

output_label = Label(text=0, padx=20, pady=15)
output_label.grid(row=1, column=1)

km_label = Label(text='Km', padx=20, pady=15)
km_label.grid(row=1, column=2)


def submited():
    output_label['text'] = round(float(input.get())*1.60934, 2)


button = Button(text="Calculate", command=submited)
button.grid(row=2, column=1)

window.mainloop()
