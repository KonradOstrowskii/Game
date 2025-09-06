"""
Module defining equipment and items.
"""

class Equipment:
    """
    Represents the equipment slots for a player character. This class only manages
    which item is in which slot. It does not handle player stats.
    """
    def __init__(self):
        self.slots = {
            "helmet": None,
            "weapon": None,
            "shield": None,
            "armor": None,
            "shoes": None,
            "ring": None,
            "necklace": None,
        }

    def equip(self, item):
        """
        Equip the specified item to the corresponding equipment slot.
        """
        slot_type = getattr(item, 'slot_type', None)
        if slot_type in self.slots:
            if self.slots[slot_type] is None:
                self.slots[slot_type] = item
                print(f"You have equipped {item.name}.")
                return True
            else:
                print(f"You already have a {slot_type} equipped.")
                return False
        else:
            print(f"Invalid equipment slot: {slot_type}.")
            return False

class Item:
    """
    Base class for all items in the game.
    """
    def __init__(self, name, description, slot_type, attributes=None):
        self.name = name
        self.description = description
        self.slot_type = slot_type
        self.attributes = attributes if attributes is not None else {}

    def to_dict(self):
        """Converts the item's common attributes to a dictionary."""
        # --- KLUCZOWA POPRAWKA ---
        # Dodajemy 'slot_type', aby system zapisu wiedział, jaki to przedmiot.
        return {
            "name": self.name,
            "description": self.description,
            "attributes": self.attributes,
            "slot_type": self.slot_type, # <-- TA LINIA JEST NOWA
        }

class Weapon(Item):
    def __init__(self, name, description, damage_bonus, attributes=None):
        super().__init__(name, description, "weapon", attributes)
        self.damage_bonus = damage_bonus

    def to_dict(self):
        data = super().to_dict()
        data["damage_bonus"] = self.damage_bonus
        return data


class Helmet(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description, "helmet", attributes)
        self.hit_points_bonus = hit_points_bonus

    def to_dict(self):
        data = super().to_dict()
        data["hit_points_bonus"] = self.hit_points_bonus
        return data


class Armor(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description, "armor", attributes)
        self.hit_points_bonus = hit_points_bonus

    def to_dict(self):
        data = super().to_dict()
        data["hit_points_bonus"] = self.hit_points_bonus
        return data


class Shield(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description, "shield", attributes)
        self.hit_points_bonus = hit_points_bonus

    def to_dict(self):
        data = super().to_dict()
        data["hit_points_bonus"] = self.hit_points_bonus
        return data


class Shoes(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description, "shoes", attributes)
        self.hit_points_bonus = hit_points_bonus

    def to_dict(self):
        data = super().to_dict()
        data["hit_points_bonus"] = self.hit_points_bonus
        return data


class Ring(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description, "ring", attributes)
        self.hit_points_bonus = hit_points_bonus

    def to_dict(self):
        data = super().to_dict()
        data["hit_points_bonus"] = self.hit_points_bonus
        return data


class Necklace(Item):
    def __init__(self, name, description, hit_points_bonus, attributes=None):
        super().__init__(name, description, "necklace", attributes)
        self.hit_points_bonus = hit_points_bonus

    def to_dict(self):
        data = super().to_dict()
        data["hit_points_bonus"] = self.hit_points_bonus
        return data