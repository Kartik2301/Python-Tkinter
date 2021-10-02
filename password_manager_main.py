from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']; numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    num_lets = random.randint(8,10)
    num_nums = random.randint(2, 4)
    num_symbols = random.randint(2, 4)

    password_list += [random.choice(letters) for _ in range(num_lets)]
    password_list += [random.choice(numbers) for _ in range(num_nums)]
    password_list += [random.choice(symbols) for _ in range(num_symbols)]

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    content = f'{website} | {email} | {password}\n'
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        with open("data.json", mode="w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        messagebox.showerror(title="Error", message="No Data file found")
    else:
        try:
            value = data[website]
        except KeyError as e:
            messagebox.showerror(title="Error", message="No Details for the website exists")
        else:
            messagebox.showinfo(title="Details Found", message=f"Website's Name {website}\nPassword : {value['password']}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="password_manager_logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21, highlightthickness=0, bg="white")
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

search_button = Button(text="Search", width=14, bg="white", highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35, highlightthickness=0, bg="white")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "email@email.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21,highlightthickness=0, bg="white")
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", bg="white", highlightthickness=0, width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30,bg="white", highlightthickness=0, height=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()