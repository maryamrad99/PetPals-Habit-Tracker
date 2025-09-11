
from habit import Habit
from pet import Pet
from persistence import save_data, load_data
from datetime import datetime


class HabitManager:
    def __init__(self, habits_file="habits.json", pets_file="pets.json"):
        self.habit_file = habits_file
        self.pets_file = pets_file
        self.habits = []
        self.pets = []
        self.load_all()

    # ---------- Persistence ----------
    def load_all(self):
        """Load habits and pets from files."""
        habits_data = load_data(self.habit_file).get("habits", [])
        pets_data = load_data(self.pets_file).get("pets", [])

        # Rebuild Habit Objects
        self.habits = [
            Habit(h["id"], h["habit_name"], h["periodicity"], h["created_at"], h.get("assigned_pet_id"))
            for h in habits_data
        ]


        # Restore completed dates
        for habit, hdata in zip(self.habits, habits_data):
            habit.completed_dates = hdata.get("completed_dates", [])


        # Rebuild Pet Objects
        self.pets = [Pet(p["id"], p["species"], p.get("nickname", "")) for p in pets_data]
        for pet, pdata in zip(self.pets, pets_data):
            pet.happiness_level = pdata.get("happiness_level", 50)
            pet.pet_age = pdata.get("pet_age", 0)
            pet.experience_points = pdata.get("experience_points",0)
            pet.unlocked_items = pdata.get("unlocked_items", [])

    def save_all(self):
        """Save habits and pets to files."""
        habits_data = [
            {
                "id": h.id,
                "habit_name": h.habit_name,
                "periodicity": h.periodicity,
                "created_at": h.created_at,
                "assigned_pet_id": h.assigned_pet_id,
                "completed_dates": h.completed_dates,
            }
            for h in self.habits
        ]

        pet_data = [
            {
                "id": p.id,
                "species": p.species,
                "nickname": p.nickname,
                "happiness_level": p.happiness_level,
                "pet_age": p.pet_age,
                "experience_points": p.experience_points,
                "unlocked_items": p.unlocked_items
            }
            for p in self.pets
        ]

        save_data(self.habit_file, {"habits": habits_data})
        save_data(self.pets_file, {"pets": pet_data})

    # ---------- Habit Management ----------
    def add_habit(self, name, periodicity, species, nickname=""):
        """Add a new habit to the system."""
        new_id = len(self.habits) + 1
        pet_id = len(self.pets) + 1

        habit = Habit(new_id, name, periodicity, datetime.now().isoformat(), assigned_pet_id=pet_id)
        pet = Pet(pet_id, species, nickname)

        self.habits.append(habit)
        self.pets.append(pet)
        self.save_all()
        print(f"Added habit '{name}' with pet '{species}' ({nickname}).")

    def remove_habit(self, habit_id):
        """Remove habit (and free its pet)."""
        self.habits = [h for h in self.habits if h.id != habit_id]
        self.pets = [p for p in self.pets if p.id != habit_id]
        self.save_all()
        print(f"Removed habit {habit_id} and its pet.")

    def list_habits(self):
        """Return list of all habits."""
        if not self.habits:
            print("No habits yet.")
        for h in self.habits:
            print(f"[{h.id}] {h.habit_name} ({h.periodicity}) - linked to Pet {h.assigned_pet_id}")

    def complete_habit(self, habit_id):
        """Mark a habit as complete for today."""
        habit = next((h for h in self.habits if h.id == habit_id), None)
        if not habit:
            print("habit not found.")
            return
        
        ts = datetime.now().isoformat()
        if habit.add_completion(ts) is None:  # still returning None
            
            # Update pet happiness & XP
            pet = next((p for p in self.pets if p.id == habit.assigned_pet_id), None)
            if pet:
                pet.adjust_happiness(10)
                pet.add_experience(10)
                print(f" Completed '{habit.habit_name}'. {pet.species} '{pet.nickname}' is happier!")
            self.save_all()

    def view_streak(self, habit_id):
        """Return (current_streak, longest_streak) for a habit or None if not found"""
        habit = next((h for h in self.habits if h.id == habit_id), None)
        if not habit:
            return None
        return habit.current_streak(), habit.longest_streak()

    
