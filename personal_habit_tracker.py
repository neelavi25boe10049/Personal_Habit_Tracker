# Personal Habit Tracker
habits = []

def add_habit():
    name = input("Enter habit name: ")
    freq = input("Enter frequency (daily/weekly): ").lower()
    habits.append({"name": name, "frequency": freq, "done": 0})
    print("Habit added!\n")

def mark_done():
    if not habits:
        print("No habits yet.\n")
        return
    print("\n--- Habits ---")
    for i, h in enumerate(habits, 1):
        print(f"{i}. {h['name']} ({h['frequency']}) - Done: {h['done']}")
    try:
        idx = int(input("Enter habit number to mark done: "))
        if 1 <= idx <= len(habits):
            habits[idx-1]['done'] += 1
            print("Marked as done!\n")
        else:
            print("Invalid number.\n")
    except:
        print("Invalid input.\n")

def view_habits():
    if not habits:
        print("No habits recorded.\n")
        return
    print("\n--- Habit List ---")
    for h in habits:
        print(f"{h['name']} | {h['frequency']} | Done count: {h['done']}")
    print()

def menu():
    while True:
        print("===== Personal Habit Tracker =====")
        print("1. Add Habit")
        print("2. Mark Habit Done")
        print("3. View Habits")
        print("4. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            add_habit()
        elif ch == '2':
            mark_done()
        elif ch == '3':
            view_habits()
        elif ch == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

if _name_ == '_main_':
    menu()
