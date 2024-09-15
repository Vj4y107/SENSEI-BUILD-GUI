import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

def load_asset(path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)

def load_image(path):
    img = Image.open(path).convert("RGBA")  # Ensure image is in RGBA mode for transparency
    return ImageTk.PhotoImage(img)

window = tk.Tk()
window.geometry("1440x1024")
window.configure(bg="#090808")
window.title("Untitled")

canvas = tk.Canvas(
    window,
    bg="#090808",
    width=1440,
    height=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_rectangle(0, 0, 1440, 163, fill='#000000', outline="")

canvas.create_text(
    600,
    42,
    anchor="nw",
    text="Fit Sensei",
    fill="#28e3da",
    font=("Michroma", 48 * -1)
)

image_1 = load_image(load_asset("image_1.png"))
canvas.create_image(525, 100, image=image_1)

button_1_image = load_image(load_asset("2.png"))
button_2_image = load_image(load_asset("3.png"))
button_3_image = load_image(load_asset("4.png"))
button_4_image = load_image(load_asset("5.png"))
button_5_image = load_image(load_asset("6.png"))

# Create a function to handle button clicks
def on_button_click(button_name):
    print(f"{button_name} has been pressed!")

# Define buttons using Label instead of Button to ensure image-only appearance
button_1 = tk.Label(
    window,
    image=button_1_image,
    bg="#090808",  # Match canvas background color
    borderwidth=0,
    highlightthickness=0
)
button_1.place(x=448, y=221, width=543, height=104)
button_1.bind("<Button-1>", lambda e: on_button_click("button_1"))

button_2 = tk.Label(
    window,
    image=button_2_image,
    bg="#090808",  # Match canvas background color
    borderwidth=0,
    highlightthickness=0
)
button_2.place(x=448, y=374, width=535, height=104)
button_2.bind("<Button-1>", lambda e: on_button_click("button_2"))

button_3 = tk.Label(
    window,
    image=button_3_image,
    bg="#090808",  # Match canvas background color
    borderwidth=0,
    highlightthickness=0
)
button_3.place(x=448, y=526, width=543, height=104)
button_3.bind("<Button-1>", lambda e: on_button_click("button_3"))

button_4 = tk.Label(
    window,
    image=button_4_image,
    bg="#090808",  # Match canvas background color
    borderwidth=0,
    highlightthickness=0
)
button_4.place(x=448, y=676, width=543, height=104)
button_4.bind("<Button-1>", lambda e: on_button_click("button_4"))

button_5 = tk.Label(
    window,
    image=button_5_image,
    bg="#090808",  # Match canvas background color
    borderwidth=0,
    highlightthickness=0
)
button_5.place(x=450, y=826, width=544, height=102)
button_5.bind("<Button-1>", lambda e: on_button_click("button_5"))

window.resizable(False, False)
window.mainloop()
