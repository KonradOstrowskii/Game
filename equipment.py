class Equipment:
    """
    Represents the equipment slots for a player character.
    
    Attributes:
        helmet (Helmet): The equipped helmet.
        weapon (Weapon): The equipped weapon.
        shield (Shield): The equipped shield.
        armor (Armor): The equipped armor.
    """
    def __init__(self):
        self.slots = {
            'helmet': None,
            'weapon': None,
            'shield': None,
            'armor': None
        }

    def equip(self, item):
        """
        Equip the specified item to the corresponding equipment slot.
        
        Args:
            item (Item): The item to be equipped.
        """
        slot_type = item.slot_type
        if slot_type in self.slots:
            self.slots[slot_type] = item

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage_bonus):
        super().__init__(name, description)
        self.damage_bonus = damage_bonus
        self.slot_type = 'weapon'

class Helmet(Item):
    def __init__(self, name, description, hit_points_bonus):
        super().__init__(name, description)
        self.hit_points_bonus = hit_points_bonus
        self.slot_type = 'helmet'

class Armor(Item):
    def __init__(self, name, description, hit_points_bonus):
        super().__init__(name, description)
        self.hit_points_bonus = hit_points_bonus
        self.slot_type = 'armor'

class shield(Item):
    def __init__(self, name, description, hit_points_bonus):
        super().__init__(name, description)
        self.hit_points_bonus = hit_points_bonus
        self.slot_type = 'shield'

