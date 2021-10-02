BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

# READ THE data

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")


list_french_terms = data["French"].to_list()
print(len(list_french_terms))

# HANDLE EVENTS

word = random.choice(list_french_terms)

def refresh():
    canvas.itemconfig(bg_image, image=card_front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text="French", fill="black")
    generate_random_word()
    flip_cards()

def generate_random_word():
    global word
    word = random.choice(list_french_terms)
    canvas.itemconfig(word_text, text=word)

def update_cards():
    global word, data
    canvas.itemconfig(bg_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    translation = data[data["French"] == word]["English"]
    canvas.itemconfig(word_text, text=translation.item(), fill="white")

def flip_cards():
    window.after(1000, update_cards)

def wrong_ans():
    refresh()

def correct_ans():
    global word, list_french_terms
    list_french_terms.remove(word)
    refresh()

# UP SETUP
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
bg_image = canvas.create_image(400,263,image=card_front_image)
canvas.grid(row=0,column=0,columnspan=2)

title_text = canvas.create_text(400,150,text="French", font=("Aerial", 40, "italic"))
word_text = canvas.create_text(400,263,text=word, font=("Aerial", 60, "italic"))

flip_cards()

image1 = PhotoImage(file="./images/right.png")
cancel = Button(image=image1, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct_ans)
cancel.grid(row=1, column=0)

image2 = PhotoImage(file="./images/wrong.png")
accept = Button(image=image2, highlightthickness=0, command=wrong_ans)
accept.grid(row=1,column=1)

window.mainloop()

new_data_dict = {
    "French" : [],
    "English" : []
}
for french_word in list_french_terms:
    new_data_dict["French"].append(french_word)
    new_data_dict["English"].append(data[data["French"] == french_word]["English"].item())

df = pandas.DataFrame(new_data_dict)
df.to_csv("words_to_learn.csv")