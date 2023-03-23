import tkinter as tk

import pandas
import pandas as pd
import random
# ---------------------------- DATA SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_data = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    print(original_data)
    to_learn_data = original_data.to_dict(orient="records")
else:
    to_learn_data = data.to_dict(orient="records")

# ---------------------------- FUNC SETUP ------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_data)
    card.itemconfig(title_id, text="French", fill="black")
    card.itemconfig(word_id, text=current_card['French'], fill="black")
    card.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    card.itemconfig(title_id, text="English", fill="white")
    english_word = current_card['English']
    card.itemconfig(word_id, text=english_word, fill="white")
    card.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn_data.remove(current_card)
    print(len(to_learn_data))
    data = pandas.DataFrame(to_learn_data)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = card.create_image(400, 263, image=card_front_img)
title_id = card.create_text(400, 150, font=("Arial", "40", "italic"))
word_id = card.create_text(400, 263, font=("Arial", "60", "bold"))
card.grid(row=0, column=0, columnspan=2)

right_img = tk.PhotoImage(file="images/right.png")
right = tk.Button(image=right_img, highlightthickness=0, command=is_known)
right.grid(column=1, row=1)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)

next_card()

window.mainloop()