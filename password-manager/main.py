import os, sys
import json
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice, randint, shuffle
from pyperclip import copy
# ---------------------------- CONSTANTS ------------------------------- #
LABEL_FONT=('Ubuntu Condensed', 14)
BUTTON_FONT=('Ubuntu Condensed', 10)

# ---------------------------- COMPILE HELPERS ------------------------------- #
if getattr(sys, 'frozen', False):
  import pyi_splash
  pyi_splash.close()

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  
  except Exception:
    base_path = os.path.dirname(os.path.abspath(__file__))

  return os.path.join(base_path, relative_path)

# ---------------------------- WEBSITE SEARCH ------------------------------- #
def website_search():
  query = website_input.get()

  if len(query) == 0:
    messagebox.showerror(title='Invalid input', message='Please enter a website name.')
  else:    
    try:
      with open('data.json', "r") as data_file:
        data = json.load(data_file)

    except FileNotFoundError:
      messagebox.showerror(title='No Data', message='No saved passwords found.\nIf you have previously saved\npasswords make sure the\ndata.json file is in the same\ndirectory as this program.')

    else:
      try:
        result = data[query]
        print(result)
      except KeyError:
        messagebox.showerror(title='No Results', message=f'No passwords for {query}.')
      
      else:
        copy_password = messagebox.askyesno(title="Success", message=f"{query}\nLogin: {result['email_user']}\nPassword: {result['password']}\nWould you like to copy the password?")

        if copy_password:
          copy(result['password'])





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  generate_password_button['text'] = 'Copied ✔️'
  password_input.delete(0, END)
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)

  password_input.insert(0, password)
  copy(password)

  generate_password_button.after(5000, reset_button)

def reset_button():
  generate_password_button['text'] = 'Generate Password'


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  email_user = email_user_input.get()
  password = password_input.get()

  if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
    messagebox.showerror(title='Invalid', message='Fill out all fields!')
    return

  new_data = {
    website: {
      "email_user": email_user,
      "password": password
    }
  }
  try:
    with open("data.json", "r") as data_file:
      data = json.load(data_file)

  except FileNotFoundError:
    with open("data.json", "w") as data_file:
      json.dump(new_data, data_file, indent=2)
  else:
    data.update(new_data)

    with open("data.json", "w") as data_file:
      json.dump(data, data_file, indent=2)
  finally:
    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# ------------------ WINDOW --------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='white')

# ------------------ CANVAS --------------------- #
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = Image.open(resource_path('logo.png'))
logo_img = ImageTk.PhotoImage(logo_img)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# ------------------ LABELS --------------------- #
website_label = Label(text='Website:', width=20, font=LABEL_FONT, bg='white', justify='right', anchor='e')
website_label.grid(column=0, row=1)

email_user_label = Label(text='Email/Username:', width=20, font=LABEL_FONT, bg='white', justify='right', anchor='e')
email_user_label.grid(column=0, row=2)

password_label = Label(text='Password:', width=20, font=LABEL_FONT, bg='white', justify='right', anchor='e')
password_label.grid(column=0, row=3)

# ------------------ INPUTS --------------------- #
website_input = Entry(width=36)
website_input.grid(column=1, row=1, sticky="EW", ipady=4)
website_input.focus()

email_user_input = Entry(width=36)
email_user_input.grid(column=1, row=2, columnspan=2, sticky="EW", ipady=4)
email_user_input.insert(0, 'cjfritz9@gmail.com')

password_input = Entry(width=16)
password_input.grid(column=1, row=3, sticky="EW", ipady=4)

# ------------------ BUTTONS --------------------- #
search_website_button = Button(text='Search', width=15, font=BUTTON_FONT, command=website_search)
search_website_button.grid(column=2, row=1, sticky="EW")

generate_password_button = Button(text='Generate Password', width=15, font=BUTTON_FONT, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text='Add', width=34, font=BUTTON_FONT, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# ---------------------------- LOOP ------------------------------- #
window.mainloop()
