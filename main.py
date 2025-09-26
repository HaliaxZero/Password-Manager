from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website= website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Empty Fields!", message="Please make sure to fill out all Fields")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"Therese are your Details: \n Email: {email} "
                                                              f"\n Password:{password} \n Is it okay to save?")


        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


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


password_button = Button(width=17, text="Generate Password", command=generate_password)
password_button.grid(row=4, column= 2)

add_button = Button(text="Add", width=36, command= save)
add_button.grid(row=5,column=1, columnspan=2)


window.mainloop()