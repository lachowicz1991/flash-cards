import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- DATA SETUP ------------------------------- #
def random_word():
    data = pd.read_csv("data/french_words.csv")
    data = data.to_dict()
    french = data['French']
    english = data['English']
    print(french)
    print(english)
    word = random.choice(list(zip(french.items(), english.items())))
    french_word = word[0][1]
    title_fr = 'French'
    card_front.itemconfig(title_id, text=title_fr)
    card_front.itemconfig(word_id, text=french_word)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

img = tk.PhotoImage(file="images/card_front.png")
card_front.create_image(400, 263, image=img)
title_id = card_front.create_text(400, 150, font=("Arial", "40", "italic"))
word_id = card_front.create_text(400, 263, font=("Arial", "60", "bold"))
card_front.grid(row=0, column=0, columnspan=2)

right_img = tk.PhotoImage(file="images/right.png")
right = tk.Button(image=right_img, highlightthickness=0, command=random_word)
right.grid(column=1, row=1)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong = tk.Button(image=wrong_img, highlightthickness=0, command=random_word)
wrong.grid(column=0, row=1)

random_word()

window.mainloop()