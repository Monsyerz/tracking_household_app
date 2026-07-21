class Person:
    """Represent one household member and their weekly income."""

    def __init__(self, name: str, weekly_income: float) -> None:
        self.name = name
        self.weekly_income = weekly_income


class Expense:
    """Represent one monthly expense category and its amount."""

    def __init__(self, category: str, amount: float) -> None:
        self.category = category
        self.amount = amount


class HouseholdBudget:
    """Stores household members, expenses, and monthly savings goal."""

    def __init__(self, savings_goal: float = 0.0) -> None:
        self.people: list[Person] = []
        self.expenses: list[Expense] = []
        self.savings_goal = savings_goal
