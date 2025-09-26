from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passwort-Manager")
window.config(padx=50,pady=50, bg="White")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness= 0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo, anchor="center")
canvas.grid(row=0, column=0, columnspan=4)

website_label = Label(text="Website:")
website_label.grid(column=0,row=2)

website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=3,row=2)
website_entry.focus()


email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=3)

email_entry = Entry(width=35)
email_entry.grid(row=3, columnspan=3, column=1)

password_label = Label(text="Password:")
password_label.grid(column=0,row=4)

password_entry = Entry(width=21)
password_entry.grid(row = 4, column= 1, columnspan=1)

password_button = Button(width=17, text="Generate Password")
password_button.grid(row=4, column= 2)

add_button = Button(text="Add", width=36)
add_button.grid(row=5,column=1, columnspan=2)


window.mainloop()