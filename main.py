from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = random.choices(letters, k=nr_letters)
    password_list.extend(random.choices(symbols, k=nr_symbols))
    password_list.extend(random.choices(numbers, k=nr_numbers))

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if website == "":
        messagebox.showerror("No Website Entered", "Please enter a website")
    elif password == "":
        messagebox.showerror("No Password Entered", "Please enter a password")
    elif email == "":
        messagebox.showerror("No Email/Username Entered", "Please enter an email/password")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it "
                                               f"okay to save?")
        if is_ok:
            try:
                with open('data.json', mode='r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json', mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data.json', mode='w') as data_file:
                    json.dump(data, data_file, indent=4)

            # clear the contents
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text='Website:')
label_website.grid(column=0, row=1)
label_website = Label(text='Email/Username:')
label_website.grid(column=0, row=2)
label_password = Label(text='Password:')
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, 'johnivanpuayap@gmail.com')
entry_password = Entry(width=20)
entry_password.grid(column=1, row=3)

# Buttons
button_generate = Button(text='Generate Password', command=generate_password)
button_generate.grid(column=2, row=3)
button_add = Button(text='Add', width=35, command=add_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
