# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
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
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=20)
entry_password.grid(column=1, row=3)

# Buttons
button_generate = Button(text='Generate Password')
button_generate.grid(column=2, row=3)
button_add = Button(text='Add', width=35)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()