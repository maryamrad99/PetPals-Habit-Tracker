
from datetime import datetime, timedelta
from petpals.habit import Habit
from petpals.pet import Pet
from petpals.analytics import list_all_habits, filter_by_periodicity, longest_streak_overall, happiest_pet
from petpals.persistence import save_data, load_data
import os


# ---------------- HABIT TESTS ----------------
def test_habit_completion_and_streaks():
    habit = habit.Habit(1, "Drink Water", "daily", datetime.now().isoformat())

    # Add completion today
    today = datetime.now().isoformat()
    assert habit.add_completion(today) is None  # method prints now

    # Add completion again today -> should not duplicate
    habit.add_completion(today)
    assert len(habit.completed_dates) == 1

    # Add completion yesterday
    yesterday = (datetime.now() - timedelta(days=1)).isoformat()
    habit.add_completion(yesterday)

    # Check streaks
    assert habit.current_streak() >= 2
    assert habit.longest_streak() >= 2

# ---------------- PET TESTS ----------------
def test_pet_happiness_and_leveling():
    pet = pet(1, "dog", "Buddy")

    # Test happiness
    pet.adjust_happiness(30)
    assert pet.happiness_level == 80
    pet.adjust_happiness(-100)
    assert pet.happiness_level == 0

    # Test XP leveling
    pet.add_experience(250)  # should level up twice (200 XP) and keep 50 XP
    assert pet.pet_age == 2
    assert pet.experience_points == 50

    # Test unlocks
    pet.unlock("Golden Bone")
    assert "Golden Bone" in pet.unlocked_items

# ---------------- ANALYTICS TESTS ----------------
def test_analytics_functions():
    habit1 = Habit(1, "Exercise", "daily", datetime.now().isoformat())
    habit2 = Habit(2, "Meditate", "weekly", datetime.now().isoformat())

    # Add streak to h1
    today = datetime.now().isoformat()
    yesterday = (datetime.now() - timedelta(days=1)).isoformat()
    habit1.add_completion(yesterday)
    habit1.add_completion(today)

    habits = [habit1, habit2]

    # Test list_all_habits
    assert "Exercise" in list_all_habits(habits)
    assert "Meditate" in list_all_habits(habits)

    # Test filter_by_periodicity
    daily_habits = filter_by_periodicity(habits, "daily")
    assert len(daily_habits) == 1
    assert daily_habits[0].habit_name == "Exercise"

    # longest_streak_overall
    assert longest_streak_overall(habits) >= 2
 
    # happiest_pet
    pet1 = Pet(1, "dog", "Buddy")
    pet2 = Pet(2, "cat", "Mimi")
    pet1.happiness_level = 40
    pet2.happiness_level = 80
    pets = [pet1, pet2]
    assert happiest_pet(pets) == pet2

# ---------------- SAVING DATA PERSISTENCE ----------------
def test_save_and_load_json(tmp_path):
    # Create temp file
    file = tmp_path / "test.json"

    # Data to save
    data = {"pets": [{"id":1, "species": "panda", "nickname": "furry"}]}

    # Save and reload data
    save_data(file, data)
    loaded = load_data(file)

    assert loaded == data
    # Clean up (pytest tmp_path auto-cleans, so no manual delete needed)

