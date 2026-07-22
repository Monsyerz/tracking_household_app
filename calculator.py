from models import Expense, Person


def weekly_to_monthly(weekly_income: float) -> float:
    """Convert weekly income into estimated monthly income."""
    return weekly_income * 52 / 12


def calculate_total_income(people: list[Person]) -> float:
    """Calculate total monthly income for all household members."""
    return sum(weekly_to_monthly(person.weekly_income) for person in people)


def calculate_total_expenses(expenses: list[Expense]) -> float:
    """Calculate total monthly expenses."""
    return sum(expense.amount for expense in expenses)


def calculate_money_left(
    total_income: float,
    total_expenses: float,
    savings_goal: float = 0.0,
) -> float:
    """Calculate money left after expenses and the monthly savings goal."""
    return total_income - total_expenses - savings_goal
