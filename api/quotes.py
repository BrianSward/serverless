from http.server import BaseHTTPRequestHandler
from tkinter import *
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        tom = requests.get(url="https://api.whatdoestrumpthink.com/api/v1/quotes/random")
        tom.raise_for_status()
        print(tom)

        data = tom.json()
        print(data["message"])
        canny.itemconfig(quote_text, text=data["message"])


window = Tk()
window.title("Fat Orange Monkey Says")
window.config(padx=50, pady=50)

canny = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canny.create_image(150, 207, image=background_img)
quote_text = canny.create_text(150, 190, text="Smash Face for Genius Talk", width=250, font=("Arial", 19, "bold"), fill="white")
canny.grid(row=0, column=0)

butt_face = PhotoImage(file="trump.png" )
butt_button = Button(image=butt_face, highlightthickness=0, command=handler.do_GET)
butt_button.grid(row=1, column=0)

window.mainloop()


