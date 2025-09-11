
from typing import List
from petpals.habit import Habit
from petpals.pet import Pet

def list_all_habits(habits: List[Habit]) -> List[str]:
    """Return list of all habits in a clean format."""
    return [h.habit_name for h in habits]

def filter_by_periodicity(habits: List[Habit], periodicity: str) -> List[Habit]:
    """Return habits filtered by daily/weekly."""
    return [h for h in habits if h.periodicity == periodicity]

def longest_streak_overall(habits: List[Habit]) -> int:
    """Return habit with the longest streak."""
    if not habits:
        return 0
    return max(h.longest_streak() for h in habits)

def happiest_pet(pets: List[Pet]) -> Pet | None:
    """Return pet with highest happiness level."""
    if not pets:
        return None
    return max(pets, key=lambda p: p.happiness_level)