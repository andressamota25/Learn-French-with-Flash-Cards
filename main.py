from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_tada = pd.read_csv("data/french_words.csv")
    to_learn = original_tada.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def random_choice():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word_card, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_Front)
    flip_timer = window.after(3000, func=show_new_card)

def show_new_card():
    global current_card
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word_card, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_know():
   to_learn.remove(current_card)
   print(len(to_learn))
   data = pd.DataFrame(to_learn)
   data.to_csv("data/words_to_learn.csv", index=False)
   random_choice()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_new_card)

canvas = Canvas(width=800, height=526)
card_Front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_Front)
language = canvas.create_text(400, 300, text="", font=("Arial", 40, "italic"), fill="black")
word_card = canvas.create_text(400, 200, text="", font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="images/right.png")
button = Button(image=right, highlightthickness=0, command=is_know)
button.grid(row=3, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=random_choice)
wrong_button.grid(row=3, column=0)

random_choice()
window.mainloop()
