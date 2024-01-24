class Equipment:
    """
    Represents the equipment slots for a player character.

    Attributes:
        helmet (Helmet):       The equipped helmet.
        weapon (Weapon):       The equipped weapon.
        shield (Shield):       The equipped shield.
        armor (Armor):         The equipped armor.
        shoes (Shoes):         The equipped shoes.
        ring (Ring):           The equipped ring.
        neckless (Neckless):   The equipped neckless.
    """

    def __init__(self):
        self.slots = {
            'helmet': None,
            'weapon': None,
            'shield': None,
            'armor': None,
            'shoes': None,
            'ring': None,
            'neckless': None
        }

    def equip(self, item, player):
        """
        Equip the specified item to the corresponding equipment slot.

        Args:
            item (Item): The item to be equipped.
        """
        slot_type = item.slot_type
        if slot_type in self.slots:
            if self.slots[slot_type] is None:
                self.slots[slot_type] = item
                print("You have equipped {}.".format(item.name))

                # Add the equipped item to the player's equipment slots
                player.equipment.slots[slot_type] = item
                return slot_type
            else:
                print("You already have a {} equipped.".format(slot_type))
        else:
            print("Invalid equipment slot: {}.".format(slot_type))


class Item:
    def __init__(self, name, description, damage_bonus=0, hit_points_bonus=0, attributes=None):
        self.name = name
        self.description = description
        self.damage_bonus = damage_bonus
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes or {}

    def add_attribute(self, attribute_name, attribute_value):
        self.attributes[attribute_name] = attribute_value


class Weapon(Item):
    def __init__(self, name, description, damage_bonus, attributes=None):
        super().__init__(name, description, damage_bonus, attributes)
        self.slot_type = 'weapon'

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "damage_bonus": self.damage_bonus,
            "attributes": self.attributes,
        }


class Helmet(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description,hit_points_bonus, attributes)
        self.slot_type = 'helmet'

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }


class Armor(Item):
    def __init__(self, name, description, attributes=None):
        super().__init__(name, description, attributes)
        self.slot_type = 'armor'


class Shield(Item):
    def __init__(self, name, description, attributes=None):
        super().__init__(name, description, attributes)
        self.slot_type = 'shield'


class Shoes(Item):
    def __init__(self, name, description, attributes=None):
        super().__init__(name, description, attributes)
        self.slot_type = 'shoes'


class Ring(Item):
    def __init__(self, name, description, attributes=None):
        super().__init__(name, description, attributes)
        self.slot_type = 'ring'


class Neckless(Item):
    def __init__(self, name, description, attributes=None):
        super().__init__(name, description, attributes)
        self.slot_type = 'neckless'
