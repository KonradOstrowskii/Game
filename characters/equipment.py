"""
Module defining equipment.
"""


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
            "helmet": None,
            "weapon": None,
            "shield": None,
            "armor": None,
            "shoes": None,
            "ring": None,
            "neckless": None,
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


class Weapon:
    def __init__(self, name, description, damage_bonus, attributes=None):
        self.name = name
        self.description = description
        self.damage_bonus = damage_bonus
        self.attributes = attributes

        self.slot_type = "weapon"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "damage_bonus": self.damage_bonus,
            "attributes": self.attributes,
        }


class Helmet:
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        self.name = name
        self.description = description
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes
        self.slot_type = "helmet"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }


class Armor:
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        self.name = name
        self.description = description
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes
        self.slot_type = "armor"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }


class Shield:
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        self.name = name
        self.description = description
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes
        self.slot_type = "shield"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }


class Shoes:
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        self.name = name
        self.description = description
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes
        self.slot_type = "shoes"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }


class Ring:
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        self.name = name
        self.description = description
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes
        self.slot_type = "ring"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }


class Neckless:
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        self.name = name
        self.description = description
        self.hit_points_bonus = hit_points_bonus
        self.attributes = attributes
        self.slot_type = "neckless"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hit_points_bonus": self.hit_points_bonus,
            "attributes": self.attributes,
        }
