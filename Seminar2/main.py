import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox


def clear_fields(entries1, entries2):
    # Clear all entries in entries1
    for entry in entries1.values():
        entry.delete(0, 'end')
    # Clear all entries in entries2
    for entry in entries2.values():
        entry.delete(0, 'end')


def confirm_action(root):
    print("Data confirmed.")
    root.destroy()
    gui_page2()

def on_enter_key_show_data(root):
    confirm_action(root)
def show_data(entries1, entries2, root):
    # Collect data from entries
    data1 = {label: entry.get() for label, entry in entries1.items()}
    data2 = {label: entry.get() for label, entry in entries2.items()}

    # Create a new top-level window
    top_level = ctk.CTkToplevel(root)
    top_level.title("Podatki o potnikih potrditev")
    top_level.geometry("300x650")  # Adjust the size as needed

    # Frame for the first set of data
    frame1 = ctk.CTkFrame(master=top_level)
    frame1.pack(side="top", fill="x", padx=20, pady=1)

    # Add a label to the top of the window
    label = ctk.CTkLabel(master=frame1, text="Potnik 1", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)
    # Display the data in labels within frame1
    for label, value in data1.items():
        # Create a frame for each label-value pair
        pair_frame = ctk.CTkFrame(master=frame1, corner_radius=10)
        pair_frame.pack(side="top", fill="x", padx=10, pady=2)

        # Create and pack the label (bold)
        label_widget = ctk.CTkLabel(master=pair_frame, text=f"{label}:", font=("Arial", 10, "bold"))
        label_widget.pack(side="left", padx=10, pady=2)

        # Create and pack the value
        value_widget = ctk.CTkLabel(master=pair_frame, text=f"{value}", font=("Arial", 10))
        value_widget.pack(side="left",padx=(2, 0))

    # Frame for the second set of data
    frame2 = ctk.CTkFrame(master=top_level)
    frame2.pack(side="top", fill="x", padx=20, pady=10)

    label = ctk.CTkLabel(master=frame2, text="Potnik 2", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)
    # Display the data in labels within frame2
    for label, value in data2.items():
        # Create a frame for each label-value pair
        pair_frame = ctk.CTkFrame(master=frame2, corner_radius=10)
        pair_frame.pack(side="top", fill="x", padx=10, pady=2)

        # Create and pack the label (bold)
        label_widget = ctk.CTkLabel(master=pair_frame, text=f"{label}:", font=("Arial", 10, "bold"))
        label_widget.pack(side="left", padx=10, pady=2)

        # Create and pack the value
        value_widget = ctk.CTkLabel(master=pair_frame, text=f"{value}", font=("Arial", 10))
        value_widget.pack(side="left", padx=(2, 0))

    root.bind("<Return>", lambda event: on_enter_key_show_data(root))

    # Confirm button at the bottom of the new window
    confirm_button = ctk.CTkButton(master=top_level, text="Potrdi", command=lambda: confirm_action(root))
    confirm_button.pack(side="bottom", fill="x", padx=20, pady=20)

    # This function could be modified to handle the confirmation action
def gui_page1():
    # Main application window
    root = ctk.CTk()
    root.title("Podatki o potnikih")
    root.geometry("600x800")

    # Define a top banner with a nicer color
    top_banner_color = "#293241"  # A dark desaturated blue
    top_banner = ctk.CTkFrame(master=root, height=50, corner_radius=0, bg_color=top_banner_color)
    top_banner.pack(side="top", fill="x")

    # Banner label with a larger font and better alignment
    banner_label = ctk.CTkLabel(master=top_banner, text="Podatki o potnikih", bg_color=top_banner_color, text_color="white", font=("Arial", 14, "bold"), anchor="center")
    banner_label.pack(side="top", fill="x")

    # Function to change the mode
    def change_mode():
        # Get the current state of the switch and set the appearance mode accordingly
        new_mode = "dark" if mode_switch.get() else "light"
        ctk.set_appearance_mode(new_mode)

    def on_enter_key(event, entries1, entries2, root):
        validatio(entries1, entries2, root)

    def validatio(entries1, entries2, root):
        if not entries1["Ime"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Ime'.")
            return
        if not entries1["Priimek"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Priimek'.")
            return
        if not entries1["Številka potnega lista"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Številka potnega lista'.")
            return
        if not entries1["Naslov"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Naslov'.")
            return
        if not entries1["Mesto"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Mesto'.")
            return
        if not entries1["Država"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Država'.")
            return
        if not entries2["Ime"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Ime'.")
            return
        if not entries2["Priimek"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Priimek'.")
            return
        if not entries2["Številka potnega lista"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Številka potnega lista'.")
            return
        if not entries2["Naslov"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Naslov'.")
            return
        if not entries2["Mesto"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Mesto'.")
            return
        if not entries2["Država"].get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Država'.")
            return

        show_data(entries1, entries2, root)

    # Content frame with a nicer background color
    content_frame1 = ctk.CTkFrame(master=root)
    content_frame1.pack(side="top", fill="x", padx=20, pady=10)

    # Add a label to the top of the window
    label = ctk.CTkLabel(master=content_frame1, text="Potnik 1", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)

    # Entry widgets with improved spacing and color
    labels = ['Ime', 'Priimek', 'Številka potnega lista', 'Naslov', 'Mesto', 'Država']
    entries1 = {}
    create_entries(content_frame1, labels, entries1)

    content_frame2 = ctk.CTkFrame(master=root)
    content_frame2.pack(side="top", fill="x", padx=20, pady=10)

    label = ctk.CTkLabel(master=content_frame2, text="Potnik 2", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)

    entries2 = {}
    create_entries(content_frame2, labels, entries2)

    root.bind("<Return>", lambda event: on_enter_key(event, entries1, entries2, root))

    # Bottom buttons with more subtle colors
    buttons_frame = ctk.CTkFrame(master=root)
    buttons_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    # Frame for the mode switch
    switch_frame = ctk.CTkFrame(master=root)
    switch_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    # Place the mode switch in the bottom right corner
    mode_switch = ctk.CTkSwitch(master=switch_frame, text="Dark Mode", command=change_mode)
    mode_switch.pack(side="right", padx=20, pady=10)

    # Clear button
    button_clear = ctk.CTkButton(master=buttons_frame, text="Počisti", command=lambda: clear_fields(entries1, entries2), fg_color="#EE6C4D", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_clear.pack(side="left", padx=10, pady=10)

    # Save button
    button_save = ctk.CTkButton(master=buttons_frame, text="Shrani podatke",
                                command=lambda: validatio(entries1, entries2, root),
                                fg_color="#BCF5A6", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_save.pack(side="right", padx=10, pady=10)


    change_mode()
    root.pack_propagate(False)

    root.mainloop()

def confirm_action2(root):
    print("Data confirmed.")
    root.destroy()
    gui_page3()
def show_data_gui2(kraj_odhoda, kraj_prihoda, start_date, end_date, flight_class, children, adults, root):
    # Create a new top-level window
    top_level = ctk.CTkToplevel(root)
    top_level.title("Podatki o izletu potrditev")
    top_level.geometry("300x400")  # Adjust the size as needed

    # Frame for the first set of data
    frame1 = ctk.CTkFrame(master=top_level, corner_radius=10)
    frame1.pack(side="top", fill="x", padx=20, pady=10)

    # Add a label to the top of the window
    label = ctk.CTkLabel(master=frame1, text="Potrditev podatkov o izletu", font=("Arial", 14, "bold"))
    label.pack(pady=(0, 20))  # Add some vertical space below the label

    # Function to create a section for each passenger
    def create_passenger_section(frame, data):
        passenger_frame = ctk.CTkFrame(master=frame, corner_radius=10)
        passenger_frame.pack(side="top", fill="x", padx=10, pady=5)

        for key, value in data.items():
            data_frame = ctk.CTkFrame(master=passenger_frame, corner_radius=10)
            data_frame.pack(side="top", fill="x", padx=10, pady=2)
            data_label = ctk.CTkLabel(master=data_frame, text=f"{key}: ", font=("Arial", 10, "bold"))
            data_label.pack(side="left", padx=10)

            value_label = ctk.CTkLabel(master=data_frame, text=value, font=("Arial", 10))
            value_label.pack(side="left")

    # Passenger 1 data section
    create_passenger_section(
        frame1,
        {
            "Kraj odhoda": kraj_odhoda,
            "Kraj prihoda": kraj_prihoda,
            "Datum odhoda": start_date,
            "Datum prihoda": end_date,
            "Razred leta": flight_class,
            "Otroci": children
        }
    )


    # Confirm button at the bottom of the new window
    confirm_button = ctk.CTkButton(master=top_level, text="Potrdi", command=lambda: confirm_action2(root))
    confirm_button.pack(side="bottom", fill="x", padx=20, pady=20)
def clear_fields_2(entries):
    # Clear all entries in entries
    entries["kraj_odhoda_entry"].delete(0, 'end')
    entries["kraj_prihoda_entry"].delete(0, 'end')
    entries["start_calendar"].set_date("")  # Assuming the Calendar widget has a method to reset the date
    entries["end_calendar"].set_date("")
    entries["flight_class_menu"].set("")  # Assuming the OptionMenu widget has a method to reset the selection
    entries["children_menu"].set("")
    entries["adults_menu"].set("")

def on_enter_key_2(event, entries1, entries2, root):
    show_data(entries1, entries2, root)
def gui_page2():
    # Main application window
    root = ctk.CTk()
    root.title("Podatki o izletu")
    root.geometry("600x700")

    # Entry for "kraj odhoda"
    kraj_odhoda_entry = ctk.CTkEntry(master=root)

    # Entry for "kraj prihoda"
    kraj_prihoda_entry = ctk.CTkEntry(master=root)

    # Calendars
    start_calendar = Calendar(root, selectmode='day', cursor="hand2", date_pattern='y-mm-dd')
    end_calendar = Calendar(root, selectmode='day', cursor="hand2", date_pattern='y-mm-dd')

    # Option Menus
    flight_class_var = ctk.StringVar(value="Economy")
    flight_class_menu = ctk.CTkOptionMenu(master=root, values=["Economy", "Business", "First"],
                                          variable=flight_class_var)

    second_choice_var = ctk.StringVar(value="0")
    second_choice_menu = ctk.CTkOptionMenu(master=root, values=["0", "1", "2", "3", "4", "5", "6", "8"],
                                           variable=second_choice_var)

    third_choice_var = ctk.StringVar(value="0")
    third_choice_menu = ctk.CTkOptionMenu(master=root, values=["0", "1", "2", "3", "4", "5", "6", "8"],
                                          variable=third_choice_var)

    # Define a top banner with a nicer color
    top_banner_color = "#293241"  # A dark desaturated blue
    top_banner = ctk.CTkFrame(master=root, height=50, corner_radius=0, bg_color=top_banner_color)
    top_banner.pack(side="top", fill="x")

    # Banner label with a larger font and better alignment
    banner_label = ctk.CTkLabel(master=top_banner, text="Podatki o izletu", bg_color=top_banner_color, text_color="white", font=("Arial", 14, "bold"), anchor="center")
    banner_label.pack(side="top", fill="x")

    # Bottom buttons with more subtle colors
    buttons_frame = ctk.CTkFrame(master=root)
    buttons_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    entries = {
        "kraj_odhoda_entry": kraj_odhoda_entry,
        "kraj_prihoda_entry": kraj_prihoda_entry,
        "start_calendar": start_calendar,
        "end_calendar": end_calendar,
        "flight_class_menu": flight_class_menu,
        "children_menu": second_choice_menu,
        "adults_menu": third_choice_menu
    }

    def save_data():
        kraj_odhoda = kraj_odhoda_entry.get()
        kraj_prihoda = kraj_prihoda_entry.get()
        start_date = start_calendar.get_date()  # Ensure this retrieves the date correctly
        end_date = end_calendar.get_date()  # Ensure this retrieves the date correctly
        flight_class = flight_class_var.get()
        children = second_choice_var.get()
        adults = third_choice_var.get()

        if not kraj_odhoda_entry.get().strip():  # strip() to ensure the field is not filled with only whitespace
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Kraj odhoda'.")
            return
        if not kraj_prihoda_entry.get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Kraj prihoda'.")
            return

        print(
            f"Kraj Odhoda: {kraj_odhoda}, Kraj Prihoda: {kraj_prihoda}, Start Date: {start_date}, End Date: {end_date}, Flight Class: {flight_class}, Children: {children}, Adults: {adults}")

        # Call show_data_gui2 with the collected data
        show_data_gui2(kraj_odhoda, kraj_prihoda, start_date, end_date, flight_class, children, adults, root)

    content_frame1 = ctk.CTkFrame(master=root)
    content_frame1.pack(side="top", fill="x", padx=20, pady=10)

    # Label for "Destinacije"
    destinacije_label = ctk.CTkLabel(master=content_frame1, text="Destinacije", font=("Arial", 12, "bold"))
    destinacije_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Label for "kraj odhoda"
    kraj_odhoda_label = ctk.CTkLabel(master=content_frame1, text="Kraj odhoda", font=("Arial", 10))
    kraj_odhoda_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")

    # Entry for "kraj odhoda"
    kraj_odhoda_entry = ctk.CTkEntry(master=content_frame1)
    kraj_odhoda_entry.grid(row=2, column=0, padx=5, pady=2, sticky="ew")

    # Label for "kraj prihoda"
    kraj_prihoda_label = ctk.CTkLabel(master=content_frame1, text="Kraj prihoda", font=("Arial", 10))
    kraj_prihoda_label.grid(row=1, column=1, padx=5, pady=2, sticky="w")

    # Entry for "kraj prihoda"
    kraj_prihoda_entry = ctk.CTkEntry(master=content_frame1)
    kraj_prihoda_entry.grid(row=2, column=1, padx=5, pady=2, sticky="ew")

    print(kraj_odhoda_entry, kraj_prihoda_entry)

    # Configure the grid layout within content_frame1
    content_frame1.columnconfigure(0, weight=1)
    content_frame1.columnconfigure(1, weight=1)

    content_frame2 = ctk.CTkFrame(master=root)
    content_frame2.pack(side="top", fill="x", padx=20, pady=10)

    # Start date label
    start_date_label = ctk.CTkLabel(master=content_frame2, text="Datum odhoda", font=("Arial", 12, "bold"))
    start_date_label.grid(row=0, column=0, padx=10, pady=5)

    # Start date calendar
    start_calendar = Calendar(content_frame2, selectmode='day', cursor="hand2", date_pattern='y-mm-dd')
    start_calendar.grid(row=1, column=0, padx=10, pady=5)

    # End date label
    end_date_label = ctk.CTkLabel(master=content_frame2, text="Datum prihoda", font=("Arial", 12, "bold"))
    end_date_label.grid(row=0, column=1, padx=10, pady=5)

    # End date calendar
    end_calendar = Calendar(content_frame2, selectmode='day', cursor="hand2", date_pattern='y-mm-dd')
    end_calendar.grid(row=1, column=1, padx=10, pady=5)

    # Configure the grid layout within content_frame2
    content_frame2.columnconfigure(0, weight=1)
    content_frame2.columnconfigure(1, weight=1)

    content_frame3 = ctk.CTkFrame(master=root)
    content_frame3.pack(side="top", fill="x", padx=20, pady=10)

    label = ctk.CTkLabel(master=content_frame3, text="Rezervacija", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)

    # Frame to hold option menus and their labels
    options_frame = ctk.CTkFrame(master=content_frame3)
    options_frame.pack(pady=5)

    # Label and option menu for flight classes
    flight_class_label = ctk.CTkLabel(master=options_frame, text="Flight Class", font=("Arial", 10))
    flight_class_label.grid(row=0, column=0, padx=10, pady=2)

    flight_classes = ["Economy", "Business", "First"]
    flight_class_var = ctk.StringVar(value="Economy")
    flight_class_menu = ctk.CTkOptionMenu(master=options_frame, values=flight_classes, variable=flight_class_var,
                                          corner_radius=10)
    flight_class_menu.grid(row=1, column=0, padx=10, pady=2)

    # Label and option menu for your second choice
    second_choice_label = ctk.CTkLabel(master=options_frame, text="Otroci", font=("Arial", 10))
    second_choice_label.grid(row=0, column=1, padx=10, pady=2)

    second_choices = ["0","1", "2", "3","4","5","6","8",]  # Replace with your options
    second_choice_var = ctk.StringVar(value=second_choices[0])
    second_choice_menu = ctk.CTkOptionMenu(master=options_frame, values=second_choices, variable=second_choice_var,
                                           corner_radius=10)
    second_choice_menu.grid(row=1, column=1, padx=10, pady=2)

    third_choice_label = ctk.CTkLabel(master=options_frame, text="Odrasli", font=("Arial", 10))
    third_choice_label.grid(row=0, column=2, padx=10, pady=2)

    third_choices = ["0","1", "2", "3","4","5","6","8",]
    third_choice_var = ctk.StringVar(value=third_choices[0])
    third_choice_menu = ctk.CTkOptionMenu(master=options_frame, values=third_choices, variable=third_choice_var,corner_radius=10)
    third_choice_menu.grid(row=1, column=2, padx=10, pady=2)

    # Configure the grid layout within options_frame
    options_frame.columnconfigure(0, weight=1)
    options_frame.columnconfigure(1, weight=1)


    def change_mode():
        # Get the current state of the switch and set the appearance mode accordingly
        new_mode = "dark" if mode_switch.get() else "light"
        ctk.set_appearance_mode(new_mode)

    # Frame for the mode switch
    switch_frame = ctk.CTkFrame(master=root)
    switch_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    # Place the mode switch in the bottom right corner
    mode_switch = ctk.CTkSwitch(master=switch_frame, text="Dark Mode", command=change_mode)
    mode_switch.pack(side="right", padx=20, pady=10)


    # Clear button
    button_clear = ctk.CTkButton(master=buttons_frame, text="Počisti", command=lambda: clear_fields_2(entries),
                                 fg_color="#EE6C4D", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_clear.pack(side="left", padx=10, pady=10)

    # Save button
    button_save = ctk.CTkButton(master=buttons_frame, text="Shrani podatke",
                                command=lambda: save_data(),
                                fg_color="#BCF5A6", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_save.pack(side="right", padx=10, pady=10)

    root.bind("<Return>", lambda event: save_data())

    root.mainloop()

def confirm_action3(root):
    print("Data confirmed.")
    root.destroy()
    gui_page4()

def show_data_gui3(entries, root):
    # Create a new top-level window
    top_level = ctk.CTkToplevel(root)
    top_level.title("Podatki o dodatkih")
    top_level.geometry("400x400")  # Adjust the size as needed

    # Loop through each passenger's data
    for person, data in entries.items():
        # Frame for each passenger's data
        person_frame = ctk.CTkFrame(master=top_level)
        person_frame.pack(side="top", fill="x", padx=20, pady=10, expand=True)

        # Label for the passenger
        label_person = ctk.CTkLabel(master=person_frame, text=person, font=("Arial", 12, "bold"))
        label_person.pack(side="top", fill="x", padx=10, pady=5)

        # Display the data in labels within the frame
        for label_text, value in data.items():
            # Create a frame for each label-value pair
            pair_frame = ctk.CTkFrame(master=person_frame, corner_radius=10)
            pair_frame.pack(side="top", fill="x", padx=10, pady=2)

            # Create and pack the label (bold)
            label_widget = ctk.CTkLabel(master=pair_frame, text=f"{label_text}: ", font=("Arial", 10, "bold"))
            label_widget.pack(side="left", padx=10)

            # Create and pack the value
            value_widget = ctk.CTkLabel(master=pair_frame, text=value, font=("Arial", 10))
            value_widget.pack(side="left")

    # Confirm button at the bottom of the new window
    confirm_button = ctk.CTkButton(master=top_level, text="Potrdi", command=lambda: confirm_action3(root))
    confirm_button.pack(side="bottom", fill="x", padx=20, pady=20)



def clear_fields_3(oseba1_var,oseba2_var,checkboxVar_oseba1,checkboxVar_oseba2,oseba1_food,oseba2_food):
    # Clear all entries in entries1
    oseba1_var.set(oseba1_food[0])
    oseba2_var.set(oseba2_food[0])
    checkboxVar_oseba1.set("Ne")
    checkboxVar_oseba2.set("Ne")
def gui_page3():
    # Main application window
    root = ctk.CTk()
    root.title("Dodatki")
    root.geometry("600x500")

    # Define a top banner with a nicer color
    top_banner_color = "#293241"  # A dark desaturated blue
    top_banner = ctk.CTkFrame(master=root, height=50, corner_radius=0, bg_color=top_banner_color)
    top_banner.pack(side="top", fill="x")

    # Banner label with a larger font and better alignment
    banner_label = ctk.CTkLabel(master=top_banner, text="Dodatki", bg_color=top_banner_color,
                                text_color="white", font=("Arial", 14, "bold"), anchor="center")
    banner_label.pack(side="top", fill="x")

    def save_data():
        entries = {
            "Oseba 1": {
                "Vrsta obroka": oseba1_var.get(),
                "Dodatna prtljaga": checkboxVar_oseba1.get()
            },
            "Oseba 2": {
                "Vrsta obroka": oseba2_var.get(),
                "Dodatna prtljaga": checkboxVar_oseba2.get()
            }
        }
        # Call the function to show data
        show_data_gui3(entries, root)

    def change_mode():
        # Get the current state of the switch and set the appearance mode accordingly
        new_mode = "dark" if mode_switch.get() else "light"
        ctk.set_appearance_mode(new_mode)

    content_frame1 = ctk.CTkFrame(master=root)
    content_frame1.pack(side="top", fill="x", padx=20, pady=10)

    # Main label centered by setting it to span across multiple columns
    label = ctk.CTkLabel(master=content_frame1, text="Vrsta oborka", font=("Arial", 12, "bold"))
    label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky='ew')  # Centered across columns

    # Sub-label for "Oseba 1" centered in column 1
    label_oseba1 = ctk.CTkLabel(master=content_frame1, text="Oseba 1", font=("Arial", 12, "bold"))
    label_oseba1.grid(row=1, column=0, padx=10, pady=5)  # Centered in column 1

    oseba1_food = ["Brez obroka", "Standardni obrok", "Vegetarijanski obrok", "Veganski obrok", "Halal obrok",]
    oseba1_var = ctk.StringVar(value=oseba1_food[0])
    oseba1_menu = ctk.CTkOptionMenu(master=content_frame1, values=oseba1_food, variable=oseba1_var, corner_radius=10)
    oseba1_menu.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    # Sub-label for "Oseba 2" centered in column 2
    label_oseba2 = ctk.CTkLabel(master=content_frame1, text="Oseba 2", font=("Arial", 12, "bold"))
    label_oseba2.grid(row=1, column=2, padx=10, pady=5)  # Centered in column 2

    oseba2_food = ["Brez obroka", "Standardni obrok", "Vegetarijanski obrok", "Veganski obrok", "Halal obrok",]
    oseba2_var = ctk.StringVar(value=oseba2_food[0])
    oseba2_menu = ctk.CTkOptionMenu(master=content_frame1, values=oseba2_food, variable=oseba2_var, corner_radius=10)
    oseba2_menu.grid(row=2, column=2, padx=10, pady=5, sticky="ew")

    # Configure the columns within the frame to properly use the space
    content_frame1.columnconfigure(0, weight=1)
    content_frame1.columnconfigure(1, weight=1)
    content_frame1.columnconfigure(2, weight=1)

    # Frame 2
    content_frame2 = ctk.CTkFrame(master=root)
    content_frame2.pack(side="top", fill="x", padx=20, pady=10)

    # Label for "Oseba 1" with centered alignment
    prtljaga1 = ctk.CTkLabel(master=content_frame2, text="Dodatna prtljaga za osebo 1", font=("Arial", 12, "bold"))
    prtljaga1.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='ew')

    # Variable to store the choice for "Oseba 1"
    checkboxVar_oseba1 = tk.StringVar(value="Ne")

    # Radio button for "Ne" aligned in the center below the label
    choice1_oseba1 = ctk.CTkRadioButton(master=content_frame2, text="Ne", variable=checkboxVar_oseba1, value="Ne")
    choice1_oseba1.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    # Radio button for "Da" aligned in the center below the label
    choice2_oseba1 = ctk.CTkRadioButton(master=content_frame2, text="Da", variable=checkboxVar_oseba1, value="Da")
    choice2_oseba1.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    # Label for "Oseba 2" with centered alignment
    prtljaga2 = ctk.CTkLabel(master=content_frame2, text="Dodatna prtljaga za osebo 2", font=("Arial", 12, "bold"))
    prtljaga2.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky='ew')

    # Variable to store the choice for "Oseba 2"
    checkboxVar_oseba2 = tk.StringVar(value="Ne")

    # Radio button for "Ne" aligned in the center below the label
    choice1_oseba2 = ctk.CTkRadioButton(master=content_frame2, text="Ne", variable=checkboxVar_oseba2, value="Ne")
    choice1_oseba2.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

    # Radio button for "Da" aligned in the center below the label
    choice2_oseba2 = ctk.CTkRadioButton(master=content_frame2, text="Da", variable=checkboxVar_oseba2, value="Da")
    choice2_oseba2.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

    content_frame2.columnconfigure(0, weight=1)
    content_frame2.columnconfigure(1, weight=1)
    content_frame2.columnconfigure(2, weight=1)

    # Bottom buttons with more subtle colors
    buttons_frame = ctk.CTkFrame(master=root)
    buttons_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    # Frame for the mode switch
    switch_frame = ctk.CTkFrame(master=root)
    switch_frame.pack(side="bottom", fill="x", padx=20, pady=10)



    # Place the mode switch in the bottom right corner
    mode_switch = ctk.CTkSwitch(master=switch_frame, text="Dark Mode", command=change_mode)
    mode_switch.pack(side="right", padx=20, pady=10)

    content_frame2.columnconfigure(0, weight=1)
    content_frame2.columnconfigure(1, weight=1)
    content_frame2.columnconfigure(2, weight=1)

    # Clear button
    button_clear = ctk.CTkButton(master=buttons_frame, text="Počisti", command=lambda: clear_fields_3(oseba1_var,oseba2_var,checkboxVar_oseba1,checkboxVar_oseba2,oseba1_food,oseba2_food),
                                 fg_color="#EE6C4D", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_clear.pack(side="left", padx=10, pady=10)

    # Save button
    button_save = ctk.CTkButton(master=buttons_frame, text="Shrani podatke",
                                command=lambda: save_data(),
                                fg_color="#BCF5A6", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_save.pack(side="right", padx=10, pady=10)


    change_mode()
    root.pack_propagate(False)

    root.mainloop()

def clear_fields_4(email_entry, cardholder_entry,cc_number_entry, cvv_entry, expiry_entry):
    # Clear all entries in entries
    cardholder_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    cc_number_entry.delete(0, 'end')
    cvv_entry.delete(0, 'end')
    expiry_entry.delete(0, 'end')

def confirm_action_4(root, email):
    print("Data confirmed.")
    root.destroy()
    gui_page5(email)

def show_data_gui4(entries, root):
    # Create a new top-level window
    top_level = ctk.CTkToplevel(root)
    top_level.title("Podatki o plačilu potrditev")
    top_level.geometry("300x300")  # Adjust the size as needed

    # Frame for the data
    frame = ctk.CTkFrame(master=top_level)
    frame.pack(side="top", fill="x", padx=20, pady=10)

    # Add a label to the top of the window
    label = ctk.CTkLabel(master=frame, text="Potrditev plačila", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)

    # Display the data in labels within the frame
    for label, value in entries.items():

        if label == "Številka kartice":
            value = f"xxxx-xxxx-xxxx-{value[-4:]}"
        # Create a frame for each label-value pair
        pair_frame = ctk.CTkFrame(master=frame, corner_radius=10)
        pair_frame.pack(side="top", fill="x", padx=10, pady=2)

        # Create and pack the label (bold)
        label_widget = ctk.CTkLabel(master=pair_frame, text=f"{label}:", font=("Arial", 10, "bold"))
        label_widget.pack(side="left", padx=10, pady=2)

        # Create and pack the value
        value_widget = ctk.CTkLabel(master=pair_frame, text=f"{value}", font=("Arial", 10))
        value_widget.pack(side="left", padx=(2, 0))

    # Confirm button at the bottom of the new window

    confirm_button = ctk.CTkButton(master=top_level, text="Potrdi", command=lambda: confirm_action_4(root,entries["Email"]))
    confirm_button.pack(side="bottom", fill="x", padx=20, pady=20)


def gui_page4():
    # Main application window
    root = ctk.CTk()
    root.title("Plačilo")
    root.geometry("600x400")

    # Define a top banner with a nicer color
    top_banner_color = "#293241"  # A dark desaturated blue
    top_banner = ctk.CTkFrame(master=root, height=50, corner_radius=0, bg_color=top_banner_color)
    top_banner.pack(side="top", fill="x")

    # Banner label with a larger font and better alignment
    banner_label = ctk.CTkLabel(master=top_banner, text="Plačilo", bg_color=top_banner_color, text_color="white", font=("Arial", 14, "bold"), anchor="center")
    banner_label.pack(side="top", fill="x")

    # Function to change the mode
    def change_mode():
        # Get the current state of the switch and set the appearance mode accordingly
        new_mode = "dark" if mode_switch.get() else "light"
        ctk.set_appearance_mode(new_mode)

    content_frame1 = ctk.CTkFrame(master=root)
    content_frame1.pack(side="top", fill="x", padx=20, pady=10)

    # Configure the grid layout with three columns
    content_frame1.columnconfigure(0, weight=1)
    content_frame1.columnconfigure(1, weight=0)  # This column will not expand
    content_frame1.columnconfigure(2, weight=1)

    # Label for "Email"
    email_label = ctk.CTkLabel(master=content_frame1, text="Email ", font=("Arial", 12, "bold"))
    email_label.grid(row=1, column=1, padx=5, pady=5)  # Centered in the second column

    # Entry for "Email"
    email_entry = ctk.CTkEntry(master=content_frame1, width=300)
    email_entry.grid(row=2, column=1, padx=5, pady=2)  # Centered in the second column

    content_frame2 = ctk.CTkFrame(master=root)
    content_frame2.pack(side="top", fill="x", padx=20, pady=10)

    # Add a label to the top of the window
    label = ctk.CTkLabel(master=content_frame2, text="Kreditna kartica", font=("Arial", 12, "bold"))
    label.pack(padx=5, pady=5)

    # First row for credit card number and security code
    frame_row1 = ctk.CTkFrame(master=content_frame2)
    frame_row1.pack(fill='x', padx=10, pady=5)

    # Credit Card Number Entry
    cc_number_label = ctk.CTkLabel(master=frame_row1, text="Številka kartice: ", font=("Arial", 12, "bold"))
    cc_number_label.grid(row=0, column=0, padx=5, pady=2, sticky='w')

    cc_number_entry = ctk.CTkEntry(master=frame_row1, width=200)  # Width can be adjusted
    cc_number_entry.grid(row=0, column=1, padx=5, pady=2, sticky='ew')


    cvv_label = ctk.CTkLabel(master=frame_row1, text="Varnostna koda:", font=("Arial", 12, "bold"))
    cvv_label.grid(row=0, column=2, padx=5, pady=2, sticky='w')

    cvv_entry = ctk.CTkEntry(master=frame_row1, width=80)  # Width set for typical CVV length
    cvv_entry.grid(row=0, column=3, padx=5, pady=2, sticky='ew')

    frame_row2 = ctk.CTkFrame(master=content_frame2)
    frame_row2.pack(fill='x', padx=10, pady=5)


    cardholder_label = ctk.CTkLabel(master=frame_row2, text="Ime imetnika:", font=("Arial", 12, "bold"))
    cardholder_label.grid(row=1, column=0, padx=5, pady=2, sticky='w')

    cardholder_entry = ctk.CTkEntry(master=frame_row2, width=200)  # Adjust width as necessary
    cardholder_entry.grid(row=1, column=1, padx=5, pady=2, sticky='ew')

    expiration_label = ctk.CTkLabel(master=frame_row2, text="Datum veljavnosti:", font=("Arial", 12, "bold"))
    expiration_label.grid(row=1, column=2, padx=5, pady=2, sticky='w')

    expiration_entry = ctk.CTkEntry(master=frame_row2, width=80)  # Width set for typical date length
    expiration_entry.grid(row=1, column=3, padx=5, pady=2, sticky='ew')

    frame_row1.columnconfigure(1, weight=3)  # Gives more weight to the credit card number entry
    frame_row1.columnconfigure(3, weight=1)  # Gives less weight to the CVV entry, so it's smaller

    frame_row2.columnconfigure(1, weight=3)  # Gives more weight to the cardholder name entry
    frame_row2.columnconfigure(3, weight=1)  # Gives less weight to the expiration date entry, so it's smaller


    def save_data():
        print("Data saved.")
        # Collect data from the entries
        entries = {
            "Email": email_entry.get(),
            "Številka kartice": cc_number_entry.get(),
            "Varnostna koda": cvv_entry.get(),
            "Ime imetnika": cardholder_entry.get(),
            "Datum veljavnosti": expiration_entry.get()
        }

        if not email_entry.get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Email'.")
            return
        if not cc_number_entry.get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Številka kartice'.")
            return
        if not cvv_entry.get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Varnostna koda'.")
            return
        if not cardholder_entry.get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Ime imetnika'.")
            return
        if not expiration_entry.get().strip():
            messagebox.showwarning("Napaka", "Prosimo, izpolnite polje 'Datum veljavnosti'.")
            return

        if not cc_number_entry.get().strip().isdigit():
            messagebox.showwarning("Napaka", "Prosimo, vnesite številko kartice.")
            return
        if not cvv_entry.get().strip().isdigit():
            messagebox.showwarning("Napaka", "Prosimo, vnesite varnostno kodo.")
            return
        if not expiration_entry.get().strip().isdigit():
            messagebox.showwarning("Napaka", "Prosimo, vnesite datum veljavnosti.")
            return

        if len(cc_number_entry.get().strip()) != 16:
            messagebox.showwarning("Napaka", "Prosimo, vnesite pravilno številko kartice.")
            return
        if len(cvv_entry.get().strip()) != 3:
            messagebox.showwarning("Napaka", "Prosimo, vnesite pravilno varnostno kodo.")
            return
        if not expiration_entry.get().strip().isdigit():
            messagebox.showwarning("Napaka", "Prosimo, vnesite pravilen datum veljavnosti.")
            return


        # Call the function to show data
        show_data_gui4(entries, root)

    root.bind("<Return>", lambda event: save_data())

    # Bottom buttons with more subtle colors
    buttons_frame = ctk.CTkFrame(master=root)
    buttons_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    # Frame for the mode switch
    switch_frame = ctk.CTkFrame(master=root)
    switch_frame.pack(side="bottom", fill="x", padx=20, pady=10)

    # Place the mode switch in the bottom right corner
    mode_switch = ctk.CTkSwitch(master=switch_frame, text="Dark Mode", command=change_mode)
    mode_switch.pack(side="right", padx=20, pady=10)

    # Clear button
    button_clear = ctk.CTkButton(master=buttons_frame, text="Počisti", command=lambda: clear_fields_4(email_entry,cardholder_entry, cc_number_entry, cvv_entry, expiration_entry), fg_color="#EE6C4D", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_clear.pack(side="left", padx=10, pady=10)

    # Save button
    button_save = ctk.CTkButton(master=buttons_frame, text="Shrani podatke",
                                command=lambda: save_data(),
                                fg_color="#BCF5A6", corner_radius=10, font=("Arial", 14, "bold"), text_color="black")
    button_save.pack(side="right", padx=10, pady=10)


    change_mode()
    root.pack_propagate(False)

    root.mainloop()

def gui_page5(email):
    # Function to show a system message box and close the program
    if email == "":
        messagebox.showinfo("Zaključek rezervacije", f'Hvala za rezervacijo.')


    def show_message_and_exit():
        messagebox.showinfo("Zaključek rezervacije", f'Rezervacija uspešno zaključena, podatki o rezervaciji so bili poslani na email: {email}.')
        root.destroy()  # This will close the Tkinter window after the messagebox

    # Main application window
    root = ctk.CTk()
    root.withdraw()  # Hide the main window as we're only showing the message box

    # Show the message box and then exit
    show_message_and_exit()

def create_entries(master_frame, labels, entries_dict):
    for i, label in enumerate(labels):
        frame = ctk.CTkFrame(master=master_frame, corner_radius=10)
        frame.pack(padx=5, pady=5, fill='x')
        label_widget = ctk.CTkLabel(master=frame, text=label, width=140, anchor="w", font=("Arial", 10, "bold"))
        label_widget.pack(side="left", padx=2, pady=2)
        entry = ctk.CTkEntry(master=frame, corner_radius=10)
        entry.pack(side="right", fill="x", expand=True)
        entries_dict[label] = entry

if __name__ == '__main__':
    gui_page1()

