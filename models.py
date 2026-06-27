class Person:
    def __init__(self, name, weekly_income):
        self.name = name
        self.weekly_income = weekly_income
"Represents one household member and their weekly income."


class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
"Represents one monthly expense category and its amount."


class HouseholdBudget:
    "Stores household members, expenses, and monthly savings goal."
    def __init__(self):
        self.people = []
        self.expenses = []
        self.savings = 0