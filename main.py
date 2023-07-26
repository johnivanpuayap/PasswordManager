from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website is "":
        messagebox.showerror("No Website Entered", "Please enter a website")
    elif password is "":
        messagebox.showerror("No Password Entered", "Please enter a password")
    elif email is "":
        messagebox.showerror("No Email/Username Entered", "Please enter an email/password")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it "
                                               f"okay to save?")
        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(f"{website}  |  {email}  |  {password}\n")

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
button_generate = Button(text='Generate Password')
button_generate.grid(column=2, row=3)
button_add = Button(text='Add', width=35, command=add_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
