from models import Person, Expense, HouseholdBudget


def get_number(prompt):
    """Ask the user for a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_household_members():
    """Collect household member names and weekly incomes from the user."""
    people = []

    number_of_people = int(get_number("How many people are in your household? "))

    for person_number in range(1, number_of_people + 1):
        name = input(f"Enter name for person {person_number}: ")
        weekly_income = get_number(f"Enter weekly income for {name}: ")

        people.append(Person(name, weekly_income))

    return people


def get_expenses():
    """Collect default and custom monthly expenses from the user."""
    expenses = []

    default_categories = [
        "Rent / Housing",
        "Car lease",
        "Internet",
        "Phone",
        "Electricity",
        "Gas",
        "Water",
        "Food",
    ]

    for category in default_categories:
        amount = get_number(f"Enter monthly amount for {category}: ")
        expenses.append(Expense(category, amount))

    while True:
        add_custom = input("Do you want to add a custom expense category? (yes/no): ").lower()

        if add_custom == "no":
            break

        if add_custom == "yes":
            category = input("Enter custom expense category name: ")
            amount = get_number(f"Enter monthly amount for {category}: ")
            expenses.append(Expense(category, amount))
        else:
            print("Please enter yes or no.")

    return expenses


def create_household_budget():
    """Create and return a HouseholdBudget object using user input."""
    budget = HouseholdBudget()

    budget.people = get_household_members()
    budget.expenses = get_expenses()

    return budget
