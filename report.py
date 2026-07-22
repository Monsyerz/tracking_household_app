from calculator import (
    calculate_money_left,
    calculate_total_expenses,
    calculate_total_income,
)
from models import HouseholdBudget


def format_money(amount: float) -> str:
    """Format a number as a dollar amount."""
    return f"${amount:,.2f}"


def print_budget_report(budget: HouseholdBudget) -> None:
    """Print a monthly household budget summary."""
    total_income = calculate_total_income(budget.people)
    total_expenses = calculate_total_expenses(budget.expenses)
    money_left = calculate_money_left(
        total_income,
        total_expenses,
        budget.savings_goal,
    )

    print("\nHousehold Monthly Summary")
    print("-" * 30)

    print("\nHousehold Members:")
    for person in budget.people:
        print(f"- {person.name}: {format_money(person.weekly_income)} weekly")

    print("\nMonthly Expenses:")
    for expense in budget.expenses:
        print(f"- {expense.category}: {format_money(expense.amount)}")

    print("\nSummary:")
    print(f"Total estimated monthly income: {format_money(total_income)}")
    print(f"Total monthly expenses: {format_money(total_expenses)}")
    print(f"Monthly savings goal: {format_money(budget.savings_goal)}")
    print(f"Money left after expenses and savings: {format_money(money_left)}")
