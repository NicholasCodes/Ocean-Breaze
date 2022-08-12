from tkinter import *
from subprocess import call
import tkinter as tk


# a def for opening a subpage
def open_new_page(page):
    ocean_breaze.destroy()
    call(["python", page])


# class for subpage that is used to stop code from breaking
class Subpage:
    def __init__(self, page):
        self.page = page


class Calculator:
    """The Calculator class helps to calculate the total plastic footprint for users"""
    def __init__(self, name, total_waste, multiplier):
        self.name = name
        self.total_waste = total_waste
        self.multiplier = multiplier
        # appends the class instances into this list, making future proofing easier
        my_entries.append(self)

    # method that adds amount into the total waste for the entry
    def add(self, added_amount):
        # Resets the calculations after each entry and adds the amount into the total_waste
        self.total_waste = 0
        if added_amount >= 0:
            self.total_waste += (added_amount * self.multiplier)
            return True
        else:
            return False


# Create a function to get entry names list
def create_name_list():
    name_list = []
    for entries in my_entries:
        name_list.append(entries.name)
    return name_list


# creates a function that updates the total plastic footprint
def update_total_footprint():
    plastic_footprint = 0
    update_string = ""

    # grabs each entry in the list and adds them all together (keep)
    for entries in my_entries:
        plastic_footprint += entries.total_waste

    if plastic_footprint > 0:
        update_string += "\nTotal Plastic Footprint: {:.2f}kg in a year".format(plastic_footprint)
    else:
        update_string += "\nTotal Plastic Footprint: {:.2f}kg in a year".format(plastic_footprint)
    plastic_waste_details.set(update_string)


# Create the add_amount function
def add_amount(entries, set_amount):
    if entries.add(set_amount):
        action_feedback.set("Input Successful".format(set_amount, entries.name))
    else:
        action_feedback.set("Only positive numbers are accepted")


# creates a function to manage each entry box to correlate the right amount to the right resource
def manage_action():
    try:
        for x in range(len(my_entries)):
            for entries in my_entries:
                # this makes it so that the correct amount goes into its corresponding entry
                if entries == my_entries[x]:
                    add_amount(entries, amount_list[x].get())
            # Update the GUI
            update_total_footprint()
            # Resets the entry box
            amount_list[x].set("0")

    # excepts values that arent accepted
    except ValueError:
        action_feedback.set("Input Unsuccessful, please enter a valid number and avoid leaving entries blank")
        # resets the entry boxes so that blank entries are reset to 0
        for x in range(len(my_entries)):
            amount_list[x].set("0")

    # makes it so that the user cannot input a word or leave entries blank
    except TclError:
        action_feedback.set("Input Unsuccessful, please enter a valid number and avoid leaving entries blank")
        # resets the entry boxes so that blank entries are reset to 0
        for x in range(len(my_entries)):
            amount_list[x].set("0")


# ------------------------------------------------- GUI CODE ---------------------------------------------------------
ocean_breaze = tk.Tk()
ocean_breaze.title("Ocean Breaze")
ocean_breaze.geometry("605x800")
ocean_breaze.configure(bg='#b1f5ff')

# makes it so that you cannot resize the window
ocean_breaze.resizable(width=False, height=False)

# create the main frame
main_frame = tk.Frame(ocean_breaze, bg="black")
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

# Creates a frame for the calculator
calculator_frame = tk.Frame(canvas, bg="#009cff")
canvas.create_window((0, 0), window=calculator_frame, anchor='nw')

# Creates an Ocean Breeze title Image inside the top frame
OceanBreaze_Title_Card = PhotoImage(
    file="img/smalltitle.png")
image_label = Button(top_frame, image=OceanBreaze_Title_Card,
                     command=lambda: [Subpage("OceanBreaze.py"), open_new_page("OceanBreaze.py")])
image_label.grid(row=0, column=2, columnspan=2, padx=123, pady=0)
# ------------------------------------------------ CALCULATOR FRAME CODE -----------------------------------------------
# my lists:
my_entries = []
entry_names = create_name_list()
amount_list = []
multiplier_list = []

# Creates instances of the class
pet_bottles = Calculator("PET_Bottles", 0, 1.9)
plastic_bags = Calculator("Plastic_bags", 0, 0.4)
food_wrappers = Calculator("Food_wrappers", 0, 0.8)
yogurt_containers = Calculator("Yogurt Containers", 0, 0.8)
cotton_swabs = Calculator("Cotton Swabs", 0, 0.1)
Detergent_cleaning_products = Calculator("Detergent, cleaning products bottles", 0, 6.3)
shampoo = Calculator("Shampoo / shower gel / cosmetics bottles", 0, 4.2)
refill_packets = Calculator("Refill packets", 0, 0.9)
toothbrushes = Calculator("Toothbrushes", 0, 1)
toothpastes = Calculator("Toothpastes", 0, 0.8)
take_away_plastic_box = Calculator("Take-away plastic box", 0, 1.7)
take_away_plastic_cup = Calculator("Take-away plastic cup", 0, 1)
straws = Calculator("Straws", 0, 0.02)
disposable_cutlery = Calculator("Disposable cutlery", 0, 0.2)
plastic_plates = Calculator("Plastic plates", 0, 1.3)
toys_furniture = Calculator("Toys, furniture etc.", 0, 1)

# Create the top frame
top_frame = tk.LabelFrame(calculator_frame)
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! With the ocean breaze calculator below you can easily see how much rubbish you produce as"
                 "well as ways to stop or decrease it!, You can also press the CHARITY button to access multitudes of"
                 "charities to donate to, as well as press either the POLLUTION button to receive info on pollution"
                 "or press the RECYCLING button to learn more about how to recycle properly!")

# Create and pack the introductory label
introductory_label = tk.Label(top_frame, font=('arial', 17, 'bold'), textvariable=message_text, wraplength=500)
introductory_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the food and kitchen frame
food_and_kitchen = tk.LabelFrame(calculator_frame, text="Food & Kitchen Needs")
food_and_kitchen.grid(row=1, rowspan=1, column=0, padx=10, pady=10, sticky="NEWS")

# Creates the bathroom and laundry frame
bathroom_and_laundry = tk.LabelFrame(calculator_frame, text="Bathroom and Laundry")
bathroom_and_laundry.grid(row=2, rowspan=1, column=0, padx=10, pady=10, sticky="NEWS")

# Creates the disposable containers and packaging frame
containers_and_packaging = tk.LabelFrame(calculator_frame, text="Disposable Containers and Packaging")
containers_and_packaging.grid(row=3, rowspan=1, column=0, padx=10, pady=10, sticky="NEWS")

# Creates the other frame
other = tk.LabelFrame(calculator_frame, text="Other")
other.grid(row=4, rowspan=1, column=0, padx=10, pady=10, sticky="NEWS")

# Creates variables to store the amounts in each entry box
amount1 = DoubleVar()
amount1.set("0")
amount2 = DoubleVar()
amount2.set("0")
amount3 = DoubleVar()
amount3.set("0")
amount4 = DoubleVar()
amount4.set("0")
amount5 = DoubleVar()
amount5.set("0")
amount6 = DoubleVar()
amount6.set("0")
amount7 = DoubleVar()
amount7.set("0")
amount8 = DoubleVar()
amount8.set("0")
amount9 = DoubleVar()
amount9.set("0")
amount10 = DoubleVar()
amount10.set("0")
amount11 = DoubleVar()
amount11.set("0")
amount12 = DoubleVar()
amount12.set("0")
amount13 = DoubleVar()
amount13.set("0")
amount14 = DoubleVar()
amount14.set("0")
amount15 = DoubleVar()
amount15.set("0")
amount16 = DoubleVar()
amount16.set("0")
# ------------------------------------------ Food and Kitchen Frame --------------------------------------------------
# Creates and packs a label
tk.Label(food_and_kitchen, font=('arial', 16, 'bold'), text="Enter your weekly consumption for these products") \
    .grid(row=0, column=0, columnspan=2, padx=10, pady=3, sticky="W")

# Create a label and entry for PET bottles and packs it into the food_and_kitchen frame in the GUI
tk.Label(food_and_kitchen, font=('arial', 16, 'bold'), text="PET Bottles:") \
    .grid(row=1, column=0, padx=124, pady=3)
tk.Entry(food_and_kitchen, font=('arial', 16, 'bold'), textvariable=amount1, bd=10,
         insertwidth=4).grid(row=1, column=1, pady=10)

# Create a label and entry for plastic bags and packs it into the food_and_kitchen frame in the GUI
tk.Label(food_and_kitchen, font=('arial', 16, 'bold'), text="Plastic bags:").grid(row=2, column=0, padx=10, pady=3)
tk.Entry(food_and_kitchen, font=('arial', 16, 'bold'), textvariable=amount2, bd=10,
         insertwidth=4).grid(row=2, column=1, pady=10)

# Create a label and entry for food wrappers and packs it into the food_and_kitchen frame in the GUI
tk.Label(food_and_kitchen, font=('arial', 16, 'bold'), text="Food Wrappers:").grid(row=3, column=0, padx=10, pady=3)
tk.Entry(food_and_kitchen, font=('arial', 16, 'bold'), textvariable=amount3, bd=10,
         insertwidth=4).grid(row=3, column=1, pady=10)

# Create a label and entry for yogurt containers and packs it into the food_and_kitchen frame in the GUI
tk.Label(food_and_kitchen, font=('arial', 16, 'bold'), text="Yogurt Containers:").grid(row=4, column=0, padx=10, pady=3)
tk.Entry(food_and_kitchen, font=('arial', 16, 'bold'), textvariable=amount4, bd=10,
         insertwidth=4).grid(row=4, column=1, pady=10)

# ----------------------------------------- Bathroom and Laundry Frame -------------------------------------------------
# Create a label and entry for Cotton Swabs and packs it into the GUI
tk.Label(bathroom_and_laundry, font=('arial', 16, 'bold'), text="Cotton Swabs:") \
    .grid(row=0, column=0, padx=10, pady=3)
tk.Entry(bathroom_and_laundry, font=('arial', 16, 'bold'), textvariable=amount5, bd=10,
         insertwidth=4).grid(row=0, column=1, pady=10)

# Create a label and entry for Detergent, cleaning products bottles and packs it into the GUI
tk.Label(bathroom_and_laundry, font=('arial', 16, 'bold'), text="Detergent, cleaning products bottles:") \
    .grid(row=1, column=0, padx=10, pady=3)
tk.Entry(bathroom_and_laundry, font=('arial', 16, 'bold'), textvariable=amount6, bd=10,
         insertwidth=4).grid(row=1, column=1, pady=10)

# Create a label and entry for Shampoo / shower gel / cosmetics bottles and packs it into the GUI
tk.Label(bathroom_and_laundry, font=('arial', 16, 'bold'), text="Shampoo / shower gel / cosmetics bottles:") \
    .grid(row=2, column=0, padx=10, pady=3)
tk.Entry(bathroom_and_laundry, font=('arial', 16, 'bold'), textvariable=amount7, bd=10,
         insertwidth=4).grid(row=2, column=1, pady=10)

# Create a label and entry for Refill packets and packs it into the GUI
tk.Label(bathroom_and_laundry, font=('arial', 16, 'bold'), text="Refill packets:") \
    .grid(row=3, column=0, padx=10, pady=3)
tk.Entry(bathroom_and_laundry, font=('arial', 16, 'bold'), textvariable=amount8, bd=10,
         insertwidth=4).grid(row=3, column=1, pady=10)

# Create a label and entry for Toothbrushes and packs it into the GUI
tk.Label(bathroom_and_laundry, font=('arial', 16, 'bold'), text="Toothbrushes:").grid(row=4, column=0, padx=10, pady=3)
tk.Entry(bathroom_and_laundry, font=('arial', 16, 'bold'), textvariable=amount9, bd=10,
         insertwidth=4).grid(row=4, column=1, pady=10)

# Create a label and entry for Toothpastes and packs it into the GUI
tk.Label(bathroom_and_laundry, font=('arial', 16, 'bold'), text="Toothpastes:").grid(row=5, column=0, padx=10, pady=3)
tk.Entry(bathroom_and_laundry, font=('arial', 16, 'bold'), textvariable=amount10, bd=10,
         insertwidth=4).grid(row=5, column=1, pady=10)

# --------------------------------- Disposable Containers and Packaging Frame -----------------------------------------
# Create a label and entry for Take-away plastic boxes and packs it into the GUI
tk.Label(containers_and_packaging, font=('arial', 16, 'bold'), text="Take-away plastic boxes:") \
    .grid(row=0, column=0, padx=75, pady=3)
tk.Entry(containers_and_packaging, font=('arial', 16, 'bold'), textvariable=amount11, bd=10,
         insertwidth=4).grid(row=0, column=1, pady=10)

# Create a label and entry for Take-away plastic cups and packs it into the GUI
tk.Label(containers_and_packaging, font=('arial', 16, 'bold'), text="Take-away plastic cups:") \
    .grid(row=1, column=0, padx=10, pady=3)
tk.Entry(containers_and_packaging, font=('arial', 16, 'bold'), textvariable=amount12, bd=10,
         insertwidth=4).grid(row=1, column=1, pady=10)

# Create a label and entry for Straws and packs it into the GUI
tk.Label(containers_and_packaging, font=('arial', 16, 'bold'), text="Straws:").grid(row=2, column=0, padx=10, pady=3)
tk.Entry(containers_and_packaging, font=('arial', 16, 'bold'), textvariable=amount13, bd=10,
         insertwidth=4).grid(row=2, column=1, pady=10)

# Create a label and entry for Disposable cutlery and packs it into the GUI
tk.Label(containers_and_packaging, font=('arial', 16, 'bold'), text="Disposable cutlery:") \
    .grid(row=3, column=0, padx=10, pady=3)
tk.Entry(containers_and_packaging, font=('arial', 16, 'bold'), textvariable=amount14, bd=10,
         insertwidth=4).grid(row=3, column=1, pady=10)

# Create a label and entry for Plastic plates and packs it into the GUI
tk.Label(containers_and_packaging, font=('arial', 16, 'bold'), text="Plastic plates:") \
    .grid(row=4, column=0, padx=10, pady=3)
tk.Entry(containers_and_packaging, font=('arial', 16, 'bold'), textvariable=amount15, bd=10,
         insertwidth=4).grid(row=4, column=1, pady=10)

# ---------------------------------------------- Other Frame Code-------------------------------------------------------
# Create a label and entry for Toys, furniture etc and packs it into the GUI
tk.Label(other, font=('arial', 16, 'bold'), text="Toys, furniture etc.:") \
    .grid(row=0, column=0, padx=96, pady=3)
tk.Entry(other, font=('arial', 16, 'bold'), textvariable=amount16, bd=10,
         insertwidth=4).grid(row=0, column=1, pady=10)

# extends the amounts into the amount list
amount_list.extend([amount1, amount2, amount3, amount4, amount5, amount6, amount7, amount8,
                    amount9, amount10, amount11, amount12, amount13, amount14, amount15, amount16])

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = tk.Label(other, textvariable=action_feedback)
action_feedback_label.grid(row=2, column=0, columnspan=2)

# Creates the Calculate button, which when pressed, runs the manage_action function
my_button = Button(other, font=('arial', 16, 'bold'), text="Calculate", command=manage_action)
my_button.grid(row=3, columnspan=2, column=0, pady=20)

# Create and set the plastic waste details variable
plastic_waste_details = StringVar()

# Create the details label and pack it into the GUI
details_label = tk.Label(other, font=('arial', 16, 'bold'), textvariable=plastic_waste_details)
details_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Update buttons frames idle tasks to let tkinter calculate widget sizes
calculator_frame.update_idletasks()

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

# Updates the footprint
update_total_footprint()
# Run the mainloop
ocean_breaze.mainloop()
