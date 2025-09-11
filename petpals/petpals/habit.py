
from datetime import datetime, timedelta

class Habit:
    """A simple habit tracker."""

    def __init__(self, id, habit_name, periodicity, created_at, assigned_pet_id=None):
        self.id = id
        self.habit_name = habit_name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.created_at = created_at
        self.completed_dates = []  # list of datetime strings in ISO format
        self.assigned_pet_id = assigned_pet_id

    def add_completion(self, ts: str):
        """Record a completion (ISO timestamp), only once per period."""
        date_str = ts.split("T")[0]
        if any(c.startswith(date_str) for c in self.completed_dates):
            print(f"Habit '{self.habit_name}' already completed today.")
        else:
            self.completed_dates.append(ts)

    def current_streak(self) -> int:
        """Compute current streak in consecutive periods (days for daily habits, etc)."""
        if not self.completed_dates:
            return 0
        dates = sorted([datetime.fromisoformat(ts) for ts in self.completed_dates])
        streak = 1
        for i in range(len(dates) - 1, 0, -1):
            if (dates[i].date() - dates[i-1].date()) == timedelta(days=1):
                streak += 1
            else:
                break
        return streak

    def longest_streak(self) -> int:
        """Compute longest streak."""
        if not self.completed_dates:
            return 0
        dates = sorted([datetime.fromisoformat(ts) for ts in self.completed_dates])
        longest, current = 1, 1
        for i in range(1, len(dates)):
            if (dates[i].date() - dates[i-1].date()) == timedelta(days=1):
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        return longest
