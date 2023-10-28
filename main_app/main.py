import sys
from PyQt5 import QtWidgets

from Game.characters.player import Player
from Game.characters.equipment import Equipment, Weapon, Helmet
from Game.characters.race import Elf, Dwarf, Orc


class Menu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create Player")

        self.player_name = QtWidgets.QLineEdit()
        self.player_race = QtWidgets.QComboBox()
        self.player_race.addItems(["Elf", "Dwarf", "Orc"])
        self.create_player_button = QtWidgets.QPushButton("Create Player")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.player_name)
        layout.addWidget(self.player_race)
        layout.addWidget(self.create_player_button)
        self.setLayout(layout)

        self.create_player_button.clicked.connect(self.create_player)

    def create_player(self):
        player_name = self.player_name.text()

        player = Player(player_name)

        race_choice = self.player_race.currentText()
        if race_choice == "Elf":
            player.race = Elf()
            player.apply_race_bonuses()
            weak_sword = Weapon("Narrow Sword", "A dull sword", damage_bonus=2)
            weak_helmet = Helmet("Basic Cap", "A simple cap", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_sword)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
        elif race_choice == "Dwarf":
            player.race = Dwarf()
            player.apply_race_bonuses()
            weak_hammer = Weapon("Weak Hammer", "A lightweight hammer", damage_bonus=2)
            weak_helmet = Helmet("Plain Helmet", "A simple helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_hammer)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
        elif race_choice == "Orc":
            player.race = Orc()
            player.apply_race_bonuses()
            weak_axe = Weapon("Blunt Axe", "A dull axe", damage_bonus=2)
            weak_helmet = Helmet("Old Helmet", "A worn helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_axe)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)

        print("Player created:")
        print(player)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    menu = Menu()
    menu.show()

    sys.exit(app.exec_())
