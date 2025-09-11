
class Pet:
    """Represents a virtual pet linked to a habit."""
    
    def __init__(self, id, species, nickname=""):
        self.id = id
        self.species = species
        self.nickname = nickname
        self.happiness_level = 50  # 0-100 scale
        self.pet_age = 0         #grows with experience
        self.experience_points = 0
        self.unlocked_items = []

    def adjust_happiness(self, delta:int):
        """Increase or decrease happiness level by delta, keeping it within 0–100."""
        self.happiness_level = max(0, min(100, self.happiness_level + delta))


    def add_experience(self, points:int):
        """Add experience points and increases pet's age."""
        self.experience_points += points
        # Example: every 100 XP = +1 age level
        while self.experience_points >= 100:
            self.experience_points -= 100
            self.pet_age += 1

    def unlock(self, item:str):
        """Unlock new accessory or reward."""
        if item not in self.unlocked_items:
            self.unlocked_items.append(item)

    