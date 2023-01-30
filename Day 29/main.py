# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
from tkinter import messagebox
from tkinter import *
from random import randint,choice,shuffle

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)

    password_list = []

    password_list=[choice(letters) for _ in range(randint(8, 10))]
    # for char in range(nr_letters):
    #     password_list.append(choice(letters))
    password_list+=[choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #     password_list += choice(symbols)
    password_list+=[choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #     password_list += choice(numbers)

    shuffle(password_list)

    password="".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    input_password.insert(0,password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input_website.get()
    email = input_email_user_name.get()
    password = input_password.get()

    if (website == '' and password == ''):
        messagebox.showwarning(
            title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail:{email}\n Password:{password}\n Is It ok to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(
                    f' {website} | {email} | {password}')
                file.write('\n')
            input_website.delete(first=0, last=END)
            input_password.delete(first=0, last=END)
            input_website.focus()

    # messagebox.showinfo(title="Title",message="message")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)
# window.minsize(500,500)

canvas = Canvas(width=200, height=200, bg='green')
image_password = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image_password)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", padx=10, pady=10)
website_label.grid(row=1, column=0)

input_website = Entry(width=40)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)

email_user_name = Label(text="Email/UserName:", padx=10, pady=10)
email_user_name.grid(row=2, column=0)


input_email_user_name = Entry(width=40)
input_email_user_name.insert(0, 'ranapratik1612@gmail.com')
input_email_user_name.grid(row=2, column=1, columnspan=2)


password_label = Label(text='Password:', padx=10, pady=10)
password_label.grid(row=3, column=0)

input_password = Entry(width=21)
input_password.grid(row=3, column=1)


gen_pas_btn = Button(text="Generate Password",command=generate_password)
gen_pas_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)
window.mainloop()
