from math import isfinite


def _read_non_empty_text(value: object, field_name: str) -> str:
    """Validate and return a non-empty string from stored data."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value.strip()


def _read_non_negative_number(value: object, field_name: str) -> float:
    """Validate and return a finite, non-negative number from stored data."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a number.")

    number = float(value)
    if not isfinite(number) or number < 0:
        raise ValueError(f"{field_name} must be a finite, non-negative number.")
    return number


class Person:
    """Represent one household member and their weekly income."""

    def __init__(self, name: str, weekly_income: float) -> None:
        self.name = name
        self.weekly_income = weekly_income

    def to_dict(self) -> dict[str, object]:
        """Convert the household member to JSON-compatible data."""
        return {
            "name": self.name,
            "weekly_income": self.weekly_income,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Person":
        """Create a household member from validated stored data."""
        if not isinstance(data, dict):
            raise ValueError("Each household member must be an object.")

        name = _read_non_empty_text(data.get("name"), "Member name")
        weekly_income = _read_non_negative_number(
            data.get("weekly_income"),
            "Weekly income",
        )
        return cls(name, weekly_income)


class Expense:
    """Represent one monthly expense category and its amount."""

    def __init__(self, category: str, amount: float) -> None:
        self.category = category
        self.amount = amount

    def to_dict(self) -> dict[str, object]:
        """Convert the expense to JSON-compatible data."""
        return {
            "category": self.category,
            "amount": self.amount,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Expense":
        """Create an expense from validated stored data."""
        if not isinstance(data, dict):
            raise ValueError("Each expense must be an object.")

        category = _read_non_empty_text(data.get("category"), "Expense category")
        amount = _read_non_negative_number(data.get("amount"), "Expense amount")
        return cls(category, amount)


class HouseholdBudget:
    """Stores household members, expenses, and monthly savings goal."""

    def __init__(self, savings_goal: float = 0.0) -> None:
        self.people: list[Person] = []
        self.expenses: list[Expense] = []
        self.savings_goal = savings_goal

    def to_dict(self) -> dict[str, object]:
        """Convert the complete budget to JSON-compatible data."""
        return {
            "people": [person.to_dict() for person in self.people],
            "expenses": [expense.to_dict() for expense in self.expenses],
            "savings_goal": self.savings_goal,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "HouseholdBudget":
        """Create a complete budget from validated stored data."""
        if not isinstance(data, dict):
            raise ValueError("The saved budget must be an object.")

        people_data = data.get("people")
        expenses_data = data.get("expenses")
        if not isinstance(people_data, list):
            raise ValueError("Saved household members must be a list.")
        if not isinstance(expenses_data, list):
            raise ValueError("Saved expenses must be a list.")

        savings_goal = _read_non_negative_number(
            data.get("savings_goal", 0.0),
            "Savings goal",
        )
        budget = cls(savings_goal)
        budget.people = [Person.from_dict(person) for person in people_data]
        budget.expenses = [Expense.from_dict(expense) for expense in expenses_data]
        return budget
