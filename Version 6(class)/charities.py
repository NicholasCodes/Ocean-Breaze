from tkinter import *
from tkinter import ttk
import tkinter as tk
from subprocess import call
import webbrowser


# class for subpage that is used to stop code from breaking
class Subpage:
    def __init__(self, page):
        self.page = page


# a callback function for the image button to open a url from a browsers
def callback(url):
    webbrowser.open_new(url)

    
# a def for opening a subpage
def open_new_page(page):
    charity.destroy()
    call(["python", page])

    
# ------------------------------------------------- GUI CODE ---------------------------------------------------------
charity = tk.Tk()
charity.title("Ocean Breaze")
charity.geometry("605x800")
charity.configure(bg='#b1f5ff')

# makes it so that you cannot resize the window
charity.resizable(width=False, height=False)

# create the main frame
main_frame = tk.Frame(charity, bg="black")
main_frame.grid(sticky='NEWS')

# create the top frame
top_frame = LabelFrame(main_frame, bg="white")
top_frame.grid(row=0, column=0, columnspan=2, pady=0, sticky="NEWS")

# Create the bottom frame
bottom_frame = LabelFrame(main_frame, bg="white")
bottom_frame.grid(row=2, column=0, columnspan=2, padx=0, sticky="NEWS")

# create frame_canvas
frame_canvas = tk.Frame(main_frame)
frame_canvas.grid(row=1, column=0, columnspan=2, sticky='NEWS')
frame_canvas.grid_columnconfigure(0, weight=1)

# Adds a canvas into the frame_canvas
canvas = tk.Canvas(frame_canvas, width=100, height=575)
canvas.grid(row=0, column=0, sticky="NEWS")

# Link of scrollbar to the canvas
scrollbar = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=2, sticky='ns')
canvas.configure(yscrollcommand=scrollbar.set)

# Creates a frame for the charities
body_frame = tk.Frame(canvas, bg="#009cff")
canvas.create_window((0, 0), window=body_frame, anchor='nw')

# Create Ocean Breeze title Image
OceanBreaze_Title_Card = PhotoImage(
    file="img/smalltitle.png")
image_label = Button(top_frame, image=OceanBreaze_Title_Card, command=lambda: [Subpage("OceanBreaze.py"),
                                                                               open_new_page("OceanBreaze.py")])
image_label.grid(row=0, column=2, columnspan=2, padx=123, pady=0)

# ------------------------------------------------- BODY FRAME CODE -------------------------------------------------
# button links from charities to the world wide web
link1_click = PhotoImage(
    file="img/Teamseas_transparent.png")
link1 = Button(body_frame, image=link1_click, borderwidth=0)
link1.grid(row=2, column=0, columnspan=1, pady=10, sticky="NSW")
link1.bind("<Button-1>", lambda e: callback("https://teamseas.org/"))

message_text1 = StringVar()
message_text1.set(
    "Team Seas, stylized as #TeamSeas, is an international collaborative fundraiser project run by YouTubers"
    " MrBeast and Mark Rober that aim to make an effort in cleaning the oceans and beaches from waste."
    " The company is run by a simple system that equates to anyone that donates 1 pound (1.99 nzd)"
    " will contribute to 1 pound (453 grams) of trash removed from the seas."
    " This is a really good charity that has already fundraised up to 31 million dollars"
    " which equates to close to 14,061 Tonnes (1 tonne = 1000kg) of trash being removed from the seas.")

link1_text = ttk.Label(body_frame, textvariable=message_text1, wraplength=300)
link1_text.grid(row=2, column=1, columnspan=1, pady=10, sticky="NSW")

link2_click = PhotoImage(
    file="img/Liveocean.png")
link2 = Button(body_frame, image=link2_click, borderwidth=0)
link2.grid(row=3, column=0, columnspan=1, pady=10, sticky="NSW")
link2.bind("<Button-1>", lambda e: callback("https://liveocean.com/foundation/"))

message_text2 = StringVar()
message_text2.set(
    "Live Ocean is a New Zealand registered ocean conservation charity founded by Olympic gold"
    " and silver medallists Peter Burling and Blair Tuke. Live Ocean was founded by Tuke and"
    " Burling out of their belief that New Zealand needs to step up to the challenge to protect"
    " and restore the oceans.")

link2_text = ttk.Label(body_frame, textvariable=message_text2, wraplength=300)
link2_text.grid(row=3, column=1, columnspan=1, pady=10, sticky="NSW")

link3_click = PhotoImage(
    file="img/Ocean_conservancy.png")
link3 = Button(body_frame, image=link3_click, borderwidth=0)
link3.grid(row=4, column=0, columnspan=1, pady=10, sticky="NSW")
link3.bind("<Button-1>", lambda e: callback("https://oceanconservancy.org/"))

message_text3 = StringVar()
message_text3.set(
    " This non-profit is working hard to see that the ocean's most extraordinary"
    " places are preserved for future generations to use and enjoy.  They use sound"
    ", science-based decisions that will lead to innovative, sustainable solutions,"
    " and strive to create a healthy ocean where life continues to nurture and sustain"
    " all of us, regardless of where we live.")

link3_text = ttk.Label(body_frame, textvariable=message_text3, wraplength=300)
link3_text.grid(row=4, column=1, columnspan=1, pady=10, sticky="NSW")

link4_click = PhotoImage(
    file="img/Oceana_logo.png")
link4 = Button(body_frame, image=link4_click, borderwidth=0)
link4.grid(row=5, column=0, columnspan=1, pady=10, sticky="NSW")
link4.bind("<Button-1>", lambda e: callback("https://oceana.org/"))

message_text4 = StringVar()
message_text4.set(
    "Oceana seeks to make our oceans more biodiverse and abundant"
    " by winning policy victories in the countries that govern much of"
    " the world's marine life.  This non-profit gets a lot done the hard way...."
    "by changing policy and regulations.  They make lasting change happen.")

link4_text = ttk.Label(body_frame, textvariable=message_text4, wraplength=300)
link4_text.grid(row=5, column=1, columnspan=1, pady=10, sticky="NSW")

link5_click = PhotoImage(
    file="img/coralreef_logo.png")
link5 = Button(body_frame, image=link5_click, borderwidth=0)
link5.grid(row=6, column=0, columnspan=1, pady=10, sticky="NSW")
link5.bind("<Button-1>", lambda e: callback("https://coral.org/en/"))

message_text5 = StringVar()
message_text5.set(
    "Working with people around the world—from fishermen to government leaders,"
    " divers to scientists, Californians to Fijians—the Coral Reef Alliance protects"
    " our most valuable and threatened ecosystem. We lead holistic conservation programs"
    " that improve coral reef health and resilience and are replicated across the globe.")

link5_text = ttk.Label(body_frame, textvariable=message_text5, wraplength=300)
link5_text.grid(row=6, column=1, columnspan=1, pady=10, sticky="NSW")

# Update buttons frames idle tasks to let tkinter calculate widget sizes
body_frame.update_idletasks()

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# --------------------------------------------- BOTTOM FRAME / FOOTER CODE ---------------------------------------------
# clickable charity image
click_charity = PhotoImage(
    file="img/charities3_red.png")
click_charity_button = Button(bottom_frame, image=click_charity,
                              command=lambda: [Subpage("charities.py"), open_new_page("charities.py")],
                              borderwidth=0)
click_charity_button.grid(row=0, column=0, columnspan=1, padx=49, pady=0)

# charities label
charities_label = Label(bottom_frame, text="Charities", wraplength=600)
charities_label.grid(row=1, rowspan=1, column=0, columnspan=1, padx=49, pady=0)

# Creates a clickable button for the pollutions page
click_pollution = PhotoImage(file="img/pollution2.png")
click_pollution_button = Button(bottom_frame, image=click_pollution,
                                command=lambda: [Subpage("Pollution.py"), open_new_page("Pollution.py")],
                                borderwidth=0)
click_pollution_button.grid(row=0, column=1, columnspan=1, padx=49, pady=0)

# Pollution Label
pollution_label = Label(bottom_frame, text="Pollution", wraplength=600)
pollution_label.grid(row=1, rowspan=1, column=1, columnspan=1, padx=49, pady=0)

# Create a clickable button for the recycling page
click_Recycling = PhotoImage(
    file="img/recycling.png")
click_Recycling_button = Button(bottom_frame, image=click_Recycling,
                                command=lambda: [Subpage("Recycling.py"), open_new_page("Recycling.py")])
click_Recycling_button.grid(row=0, column=4, columnspan=1, padx=49, pady=0)

# Recycling Label
recycling_label = Label(bottom_frame, text="Recycling", wraplength=600)
recycling_label.grid(row=1, rowspan=1, column=4, columnspan=1, padx=49, pady=0)

# Run the mainloop
charity.mainloop()
