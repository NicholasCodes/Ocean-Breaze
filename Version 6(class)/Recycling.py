from tkinter import *
from tkinter import ttk
import tkinter as tk
from subprocess import call
import webbrowser


# creates a def for inputting subtexts with a adjustable row
def set_subtext(text, row):
    texts = ttk.Label(body_frame, text=text, wraplength=594, font=("Arial", 16))
    texts.grid(row=row, column=0, columnspan=2, pady=10, sticky="NSW")


# creates a def for inputting heading texts with a adjustable row
def set_heading_text(text, row):
    heading_text = ttk.Label(body_frame, text=text, wraplength=594, font=("PHOSPHATE", 30))
    heading_text.grid(row=row, column=0, columnspan=2, pady=10, sticky="NSW")


# a def for opening a subpage
def open_new_page(page):
    recycling.destroy()
    call(["python", page])


# class for subpage that is used to stop code from breaking
class Subpage:
    def __init__(self, page):
        self.page = page


# a callback function for the image button to open a url from a browsers
def callback(url):
    webbrowser.open_new(url)


# ------------------------------------------------- GUI CODE ----------------------------------------------------------
recycling = tk.Tk()
recycling.title("Ocean Breaze")
recycling.geometry("605x800")
recycling.configure(bg='#b1f5ff')

# makes it so that you cannot resize the window
recycling.resizable(width=False, height=False)

# creates the main frame
main_frame = tk.Frame(recycling, bg="black")
main_frame.grid(sticky='NEWS')

# creates the top frame
top_frame = LabelFrame(main_frame, bg="white")
top_frame.grid(row=0, column=0, columnspan=2, pady=0, sticky="NEWS")

# Creates the bottom frame
bottom_frame = LabelFrame(main_frame, bg="white")
bottom_frame.grid(row=2, column=0, columnspan=2, padx=0, sticky="NEWS")

# creates frame_canvas
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

# Creates a body frame for the recycling info
body_frame = tk.Frame(canvas, bg="#009cff")
canvas.create_window((0, 0), window=body_frame, anchor='nw')

# Grabs the Ocean Breeze title Image and packs it into the top frame
OceanBreaze_Title_Card = PhotoImage(
    file="img/smalltitle.png")
image_label = Button(top_frame, image=OceanBreaze_Title_Card, borderwidth=0,
                     command=lambda: [Subpage("OceanBreaze.py"), open_new_page("OceanBreaze.py")])
image_label.grid(row=0, column=2, columnspan=2, padx=123, pady=0)

# ------------------------------------------------- TEXT FRAME CODE -------------------------------------------------
# STEP 1
set_heading_text("Step 1: Recycle plastic bags separately", 0)

set_subtext("You might think plastic bags are convenient for gathering all your recyclable material "
            "together. However, plastic bags can be an unpredictable and time-consuming nightmare for those"
            " sorting at the recycling plant.\n\nIf you have a habit of putting all your aluminium "
            "cans into a plastic bag and tying it up before you hand it in, stop now. You could be wasting "
            "your time because plastic bags are routinely thrown away, even if they are filled.\n\nPlastic bags "
            "slow down the automated recycling process. This is because human sorters have to individually open them"
            " up and then dispose of the bags, thus making the process more difficult.\n\nPlastic bags are a bane to"
            " our environment: they litter the landscape and threaten wildlife. There’s a good reason why supermarkets"
            " charge for each plastic bag used in the UK.\n\nRather than throwing out a plastic bag or ruining"
            " your recycling batch, the ideal option is to recycle them separately. There are plenty of plastic bag "
            "recycling programmes held by the government and many supermarkets feature a plastic bag bin specifically "
            "for recycling this difficult material. ", 1)

# STEP 2
set_heading_text("Step 2: Try not to shred paper", 2)

set_subtext(
    "Back in the infant years of recycling, shredded paper was difficult to recycle and often ended up in landfill."
    " Since then, recycling plants have improved and now shredded paper is usually properly recycled. However this "
    "does not mean you should shred your sheets at every opportunity.\n\nShredding is sometimes unavoidable, especially"
    " when dealing with private documents. But you should not be doing it solely to fit more into a recycling bin.\n\n"
    "If the pieces of paper are too small, some recycling centres will not accept them and even those that do have to "
    "lower the quality of what it can be recycled into. The length of the paper fibre determines if it can be recycled "
    "into high-grade material such as useful printer paper or low-grade material.\n\nLeaving paper outside, or exposing"
    " it to the elements could also alter how much of it gets recycled. Paper left out in the rain can have its organic"
    " material broken down, which is why many recycling bins feature lids that are sealed until manual intervention", 3)

# STEP 3
set_heading_text("Step 3: Compress bottles and put the lid back on", 4)

set_subtext(
    "Should you keep bottle lids on or remove them? It’s a simple question that has generated a lot of confusion."
    "\n\nThe previously recommended method was removing them. This is because bottle tops are normally made of "
    "polypropylene. This polymer tends to melt at a higher temperature  compared to the rest of most plastic "
    "bottles.\n\nAnother reason was because uncompressed bottles with lids on were dangerous in the early stages "
    "of recycling. The compression of an air-packed bottle often resulted in bottle caps being propelled at high"
    " speed, which was seen as a clear health risk.\n\nThe recycling process has improved since then and it is now"
    " okay to keep lids on bottles. In fact, it is now advisable to leave them on because bottle caps handed in "
    "separately could be placed into general waste if missed during screening.\n\nOne of the most helpful ways to "
    "recycle bottles is to squash the air out, and then place the lid back on. This way there is neither water nor "
    "air inside.", 5)

# STEP 4
set_heading_text("Step 4: Keep cardboard and your other recyclables clean", 6)

set_subtext(
    "While cardboard is recyclable, grease can damage the cardboard and render it impossible to recycle.\n\nThis"
    " means you also need to avoid placing foods, liquids and animal wastes in your recycling bin as it can "
    "contaminate the rest of the recyclable materials.\n\nNewspapers used to hold your order of chips and most "
    "cardboard take-away boxes are better placed into a normal bin or a compost bin.", 7)

# STEP 5
set_heading_text("Step 5: Read your local recycling guide", 8)

set_subtext("While this advice applies to most areas, each will have its own recycling guide and some may accept "
            "materials others do not. To be sure you are not wasting your time recycling something that cannot be, "
            "or contaminating good material – it’s well worth reading your area’s recycling guide. Below is a link"
            "to a further website that can provide you with even more ways to make the oceans a better place", 9)

# clickable image that links to the oceanic society page on google
oceanic_society_img = PhotoImage(
    file="img/Oceanic_Society.png")
oceanic_society_button = Button(body_frame, image=oceanic_society_img, borderwidth=0)
oceanic_society_button.grid(row=10, column=0, columnspan=1, pady=10, padx=20, sticky="NSW")
oceanic_society_button.bind("<Button-1>", lambda e: callback("https://www.oceanicsociety.org/resources/7-"
                                                             "ways-to-reduce-ocean-plastic-pollution-today/"))

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
recycling.mainloop()
