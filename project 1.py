# ---------------------------------------------
# Project: Daily Calorie Tracker CLI
# Name: Punit Yadav
# Roll No: 2501010200
# Course: Programming for Problem Solving using Python (ETCCPP102)
# Date: 25 Oct 2025
# ---------------------------------------------

# Welcome message
print("=====================================")
print("   Welcome to Daily Calorie Tracker  ")
print("=====================================")
print("This program helps you track how many calories you eat in a day.\n")

# Asking user how many meals they want to enter
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)

# Calculations
total = sum(calories)
average = total / len(calories)
limit = float(input("\nEnter your daily calorie limit: "))

# Checking limit
if total > limit:
    print("\n⚠️ You have eaten more than your daily limit!")
else:
    print("\n✅ Great! You are within your daily limit.")

# Displaying summary
print("\n------------ DAILY REPORT ------------")
print("Meal Name\tCalories")
print("--------------------------------------")
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")
print("--------------------------------------")
print(f"Total Calories:\t{total}")
print(f"Average Calories:\t{average:.2f}")
print("--------------------------------------")

# Ask user to save report
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    with open("calorie_log.txt", "a") as f:
        f.write("\n====== Daily Calorie Report ======\n")
        for i in range(len(meals)):
            f.write(f"{meals[i]} - {calories[i]} calories\n")
        f.write(f"Total: {total} | Average: {average:.2f}\n")
        f.write("-----------------------------------\n")
    print("✅ Report saved in 'calorie_log.txt'.")
else:
    print("Okay, report not saved.")

print("\nThank you for using Daily Calorie Tracker! 👋")
