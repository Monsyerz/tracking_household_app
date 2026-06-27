def weekly_to_monthly(weekly_income):
    """Convert weekly income into estimated monthly income."""
    return weekly_income * 52 / 12


def calculate_total_income(people):
    """Calculate total monthly income for all household members."""
    return sum(weekly_to_monthly(person.weekly_income) for person in people)


def calculate_total_expenses(expenses):
    """Calculate total monthly expenses."""
    return sum(expense.amount for expense in expenses)


def calculate_money_left(total_income, total_expenses):
    """Calculate money left after expenses."""
    return total_income - total_expenses
