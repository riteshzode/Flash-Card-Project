import random
from tkinter import *
from words import dict_data

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

# end game func

def end_game():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="", fill="black")
    canvas.itemconfig(card_word, text="", fill="black")
    canvas.create_text(400, 250, text="Game Over", font=("Arial", 40, "italic"))
    green_button.config(state="disabled")
    red_button.config(state="disabled")

# next card func

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(dict_data)
    canvas.itemconfig(card_title, text="Term", fill="black")
    canvas.itemconfig(card_word, text=current_card["Tools"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)

    flip_timer = window.after(3000, func=flip_card)

# flip card func

def flip_card():
    canvas.itemconfig(card_title, text="Definition", fill="white")
    canvas.itemconfig(card_word, text=current_card["Word"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)



window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 110, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 280, text="", width=500, font=("Arial", 20, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

green_button_img = PhotoImage(file="right.png")
green_button = Button(image=green_button_img, command=next_card, highlightthickness=0)
green_button.grid(row=1, column=1)

red_button_img = PhotoImage(file="wrong.png")
red_button = Button(image=red_button_img, command=end_game, highlightthickness=0)
red_button.grid(row=1, column=0)


next_card()


window.mainloop()
