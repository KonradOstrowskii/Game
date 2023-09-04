from characters.creating_player import create_player
import tkinter as tk
from tkinter import messagebox
from characters.race import Elf, Dwarf, Orc
from characters.player import Player
from characters.equipment import Equipment, Weapon, Helmet

def create_player():
    player_name = player_name_entry.get()

    while True:
        player = Player(player_name)
        race_choice = race_choice_var.get()
        if race_choice == 1:
            player.race = Elf()
            player.apply_race_bonuses()
            weak_sword = Weapon("Narrow Sword", "A dull sword", damage_bonus=2)
            weak_helmet = Helmet("Basic Cap", "A simple cap", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_sword)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
            break
        elif race_choice == 2:
            player.race = Dwarf()
            player.apply_race_bonuses()
            weak_hammer = Weapon("Weak Hammer", "A lightweight hammer", damage_bonus=2)
            weak_helmet = Helmet("Plain Helmet", "A simple helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_hammer)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
            break
        elif race_choice == 3:
            player.race = Orc()
            player.apply_race_bonuses()
            weak_axe = Weapon("Blunt Axe", "A dull axe", damage_bonus=2)
            weak_helmet = Helmet("Old Helmet", "A worn helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_axe)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
            break
        else:
            messagebox.showerror("Invalid Choice", "Please choose  Elf, Dwarf, Orc")
            return

    player_text.set(f"Player created:\n{str(player)}")
    
    
def print_race_descriptions():
    description_text.set("Available Races:\n1. Elf\n" + Elf.__str__(Elf()) + "\n2. Dwarf\n" + Dwarf.__str__(Dwarf()) + "\n3. Orc\n" + Orc.__str__(Orc()))

# Create the main tkinter window
root = tk.Tk()
root.title("Create Player")

# Create text variables to update labels
description_text = tk.StringVar()
equipment_text = tk.StringVar()
player_text = tk.StringVar()

# Create labels to display race descriptions, equipment, and player information
race_label = tk.Label(root, textvariable=description_text)
equipment_label = tk.Label(root, textvariable=equipment_text)
player_label = tk.Label(root, textvariable=player_text)

# Create a label and entry for the player name
player_name_label = tk.Label(root, text="Enter your player name:")
player_name_entry = tk.Entry(root)

# Create radio buttons for race selection
race_choice_var = tk.IntVar()
race_choice_label = tk.Label(root, text="Choose a race:")
elf_radio = tk.Radiobutton(root, text="Elf", variable=race_choice_var, value=1)
dwarf_radio = tk.Radiobutton(root, text="Dwarf", variable=race_choice_var, value=2)
orc_radio = tk.Radiobutton(root, text="Orc", variable=race_choice_var, value=3)

# Create a button to create the player
create_button = tk.Button(root, text="Create Player", command=create_player)

# Pack the labels, entry, radio buttons, and button
race_label.pack()
elf_radio.pack()
dwarf_radio.pack()
orc_radio.pack()
player_name_label.pack()
player_name_entry.pack()
create_button.pack()
equipment_label.pack()
player_label.pack()

# Initialize race descriptions
print_race_descriptions()

# Run the tkinter main loop
root.mainloop()
