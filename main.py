from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_search():
    website = website_input.get()

    try:
        with open("passwords.json", "r") as info_file:
            data = json.load(info_file)
            fetched_email = data[website_input.get()]["email"]
            fetched_password = data[website_input.get()]["password"]

        messagebox.showinfo(title="Your Details: ", message=f"There are the details you entered: "
                                                            f"\nWebsite: {website} "
                                                            f"\nEmail: {fetched_email}"
                                                            f"\nPassword: {fetched_password}")
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="Password File Not Found!")
    except JSONDecodeError:
        messagebox.showerror(title="Oops", message="No details for the Website exists!")
    except KeyError:
        messagebox.showerror(title="Oops", message="No details for the Website exists!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    alpha_list = []
    num_list = []
    symbol_list = []

    alphas = random.sample(range(1, 52), nr_letters)
    nums = random.sample(range(1, 10), nr_numbers)
    specials = random.sample(range(1, 9), nr_symbols)

    for alpha in alphas:
        alpha_list.append(letters[alpha])

    for num in nums:
        num_list.append(numbers[num])

    for special in specials:
        symbol_list.append(symbols[special])

    p_alpha = "".join(alpha_list)
    p_num = "".join(num_list)
    p_symbol = "".join(symbol_list)

    easy_password = p_alpha + p_num + p_symbol

    hard_password = ''.join(random.sample(easy_password, len(easy_password)))

    password_input.insert(END, hard_password)
    pyperclip.copy(hard_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": password_input.get(),
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty.")
    else:
        try:
            with open("passwords.json", "r") as info_file:
                data = json.load(info_file)
        except FileNotFoundError:
            with open("passwords.json", "w") as info_file:
                json.dump(new_data, info_file, indent=4)
        except JSONDecodeError:
            with open("passwords.json", "w") as info_file:
                json.dump(new_data, info_file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as info_file:
                json.dump(data, info_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=("helvetica", 10, "normal"), fg="black", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email / Username: ", font=("helvetica", 10, "normal"), fg="black", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=("helvetica", 10, "normal"), fg="black", bg="white")
password_label.grid(row=3, column=0)

generate_button = Button(text="Generate Password", font=("helvetica", 10, "normal"),)
generate_button.config(command=password_generator)
generate_button.grid(row=4, column=2, columnspan=1, pady=5)

search_button = Button(text="Search", font=("helvetica", 10, "normal"), width=15,)
search_button.config(command=password_search)
search_button.grid(row=4, column=1, columnspan=1, pady=5)

add_button = Button(text="Add", font=("helvetica", 10, "normal"), width=40,)
add_button.config(command=save_password)
add_button.grid(row=5, column=1, columnspan=2, pady=5)

website_input = Entry(width=42, borderwidth=2)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, pady=5)

email_input = Entry(width=42, borderwidth=2)
email_input.insert(END, "sanjaypm09@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, pady=5)

password_input = Entry(width=42, borderwidth=2)
password_input.grid(row=3, column=1, columnspan=2, pady=5)

window.mainloop()
