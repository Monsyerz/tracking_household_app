from math import isfinite

from models import Person, Expense, HouseholdBudget


def get_non_empty_text(prompt: str) -> str:
    """Ask for text until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value

        print("This value cannot be empty.")


def get_non_negative_number(prompt: str) -> float:
    """Ask for a finite number that is greater than or equal to zero."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not isfinite(value):
            print("Please enter a finite number.")
        elif value < 0:
            print("Please enter zero or a positive number.")
        else:
            return value


def get_positive_whole_number(prompt: str) -> int:
    """Ask for a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a positive whole number.")
            continue

        if value > 0:
            return value

        print("Please enter a positive whole number.")


def get_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return True for yes or False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "yes":
            return True
        if answer == "no":
            return False

        print("Please enter yes or no.")


def get_household_members() -> list[Person]:
    """Collect household member names and weekly incomes from the user."""
    people: list[Person] = []

    number_of_people = get_positive_whole_number(
        "How many people are in your household? "
    )

    for person_number in range(1, number_of_people + 1):
        name = get_non_empty_text(f"Enter name for person {person_number}: ")
        weekly_income = get_non_negative_number(f"Enter weekly income for {name}: ")

        people.append(Person(name, weekly_income))

    return people


def get_expenses() -> list[Expense]:
    """Collect default and custom monthly expenses from the user."""
    expenses: list[Expense] = []

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
        amount = get_non_negative_number(f"Enter monthly amount for {category}: ")
        expenses.append(Expense(category, amount))

    while get_yes_no("Do you want to add a custom expense category? (yes/no): "):
        category = get_non_empty_text("Enter custom expense category name: ")
        amount = get_non_negative_number(f"Enter monthly amount for {category}: ")
        expenses.append(Expense(category, amount))

    return expenses


def create_household_budget() -> HouseholdBudget:
    """Create and return a HouseholdBudget object using user input."""
    budget = HouseholdBudget()

    budget.people = get_household_members()
    budget.expenses = get_expenses()
    budget.savings_goal = get_non_negative_number(
        "Enter your monthly savings goal: "
    )

    return budget
