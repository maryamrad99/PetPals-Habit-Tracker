
from manager import HabitManager

def main():
    manager = HabitManager()

    while True:
        print("Welcome to PetPals Habit Tracker!")
        print("1. Add Habit")
        print("2. Remove Habit")
        print("3. List Habits")
        print("4. View Streaks")
        print("5. Complete Habit")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Habit name:  ")
            periodicity = input("Periodicity (daily/weekly):   ")
            species = input("Pet species:  ")
            nickname = input("Pet nickname:  ")
            manager.add_habit(name, periodicity, species, nickname)

        elif choice == "2":
            try: 
                habit_id = int(input("Habit ID to remove:  ").strip())
                manager.remove_habit(habit_id)
            except ValueError:
                print("Invalid ID")
        
        elif choice == "3":
            manager.list_habits()

        elif choice == "4":
            try:
                habit_id = int(input("Habit ID to view streak:  ").strip())
            except ValueError:
                print("Invalid ID.")
                continue
            result = manager.view_streak(habit_id)
            if result is None:
                print("Habit not found")
            else:
                current, longest = result
                print(f"Habit [{habit_id}]- Current streak: {current}, Longest streak: {longest}")

        elif choice == "5":
            try:
                habit_id = int(input("Habit ID to complete:  ").strip())
                manager.complete_habit(habit_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == "6":
            print("Goodbye!")
            break
      
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()