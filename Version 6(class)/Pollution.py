from tkinter import *
from tkinter import ttk
import tkinter as tk
from subprocess import call


# a def for opening a subpage
def open_new_page(page):
    pollution.destroy()
    call(["python", page])


# class for subpage that is used to stop code from breaking
class Subpage:
    def __init__(self, page):
        self.page = page


# ------------------------------------------------- GUI CODE ---------------------------------------------------------
pollution = tk.Tk()
pollution.title("Ocean Breaze")
pollution.geometry("605x800")
pollution.configure(bg='#b1f5ff')

# makes it so that you cannot resize the window
pollution.resizable(width=False, height=False)

# create the main frame
main_frame = tk.Frame(pollution, bg="black")
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

# Creates a frame for the recycling
body_frame = tk.Frame(canvas, bg="#009cff")
canvas.create_window((0, 0), window=body_frame, anchor='nw')

# Create Ocean Breeze title Image
OceanBreaze_Title_Card = PhotoImage(
    file="img/smalltitle.png")
image_label = Button(top_frame, image=OceanBreaze_Title_Card,
                     command=lambda: [Subpage("OceanBreaze.py"), open_new_page("OceanBreaze.py")])
image_label.grid(row=0, column=2, columnspan=2, padx=123, pady=0)

# ------------------------------------------------- BODY FRAME CODE -------------------------------------------------
# pictures of pollution
Photo1 = PhotoImage(
    file="img/pollution pic1.png")
Photolabel1 = Label(body_frame, image=Photo1, borderwidth=0)
Photolabel1.grid(row=1, column=1, columnspan=1, pady=10, sticky="NSW")

Photo2 = PhotoImage(
    file="img/pollution pic2.png")
Photolabel2 = Label(body_frame, image=Photo2, borderwidth=0)
Photolabel2.grid(row=3, column=0, columnspan=1, pady=10, sticky="NSW")

# message labels for the pollution body
message_text1 = StringVar()
message_text1.set(
    "An estimated 8 Million tons of plastic enters our oceans every year. There are 5.25 trillion pieces"
    " of plastic waste estimated to be in our oceans. 269,000 tons float, 4 billion microfibers per km² "
    "dwell below the surface. 70% of our debris sinks into the ocean's ecosystem, 15% floats, and 15% "
    "lands on our beaches")

pollution_statistics = ttk.Label(body_frame, textvariable=message_text1, wraplength=300)
pollution_statistics.grid(row=1, column=0, columnspan=1, pady=10, sticky="NSW")

message_text2 = StringVar()
message_text2.set(
    "Marine life, as we know it, is suffering irreparable damage from the chemical pollution of the waters"
    " and the millions of tons of mismanaged waste dumped in the oceans each year. The result is a planetary"
    " crisis with over 100 million marine animal’s lives get lost every year, and the decay of the ocean's"
    " ecosystem.Almost 1,000 species of marine animals get impacted by ocean pollution, and we now have over"
    " 500 locations recorded as dead zones where marine life cannot exist. How did this happen, what is causing"
    " the most damage, .")

affect_on_marine_life_stats = ttk.Label(body_frame, textvariable=message_text2, wraplength=600)
affect_on_marine_life_stats.grid(row=2, column=0, columnspan=2, pady=10, sticky="NWS")

message_text3 = StringVar()
message_text3.set(
    "The ocean absorbs about 30% of the carbon dioxide (CO2) that is released in the atmosphere. As levels of "
    "atmospheric CO2 increase from human activity such as burning fossil fuels (e.g., car emissions) and changing "
    "land use (e.g., deforestation), the amount of carbon dioxide absorbed by the ocean also increases.  When CO2 "
    "is absorbed by seawater, a series of chemical reactions occur resulting in the increased concentration of "
    "hydrogen ions. This process has far reaching implications for the ocean and the creatures that live there."
)

carbon_emissions_effect = ttk.Label(body_frame, textvariable=message_text3, wraplength=300)
carbon_emissions_effect.grid(row=3, column=1, columnspan=1, pady=10, sticky="NSW")

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
pollution.mainloop()
