from flask import Flask, render_template, request

from calculator import calculate_total_expenses, calculate_total_income, calculate_money_left
from models import Expense, HouseholdBudget, Person

app = Flask(__name__)


@app.route("/")
def index():
    """Display the budget form."""
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    """Create a budget from form data and display calculated results."""
    budget = HouseholdBudget()

    person_names = request.form.getlist("person_name")
    weekly_incomes = request.form.getlist("weekly_income")

    for person_name, weekly_income in zip(person_names, weekly_incomes):
        if person_name.strip():
            budget.people.append(Person(person_name.strip(), float(weekly_income)))

    expense_categories = {
        "Rent / Housing": "rent",
        "Car lease": "car_lease",
        "Internet": "internet",
        "Phone": "phone",
        "Electricity": "electricity",
        "Gas": "gas",
        "Water": "water",
        "Food": "food",
    }

    for category, field_name in expense_categories.items():
        amount = float(request.form[field_name])
        budget.expenses.append(Expense(category, amount))

    total_income = calculate_total_income(budget.people)
    total_expenses = calculate_total_expenses(budget.expenses)
    money_left = calculate_money_left(total_income, total_expenses)

    return render_template(
        "result.html",
        people=budget.people,
        expenses=budget.expenses,
        total_income=total_income,
        total_expenses=total_expenses,
        money_left=money_left,
    )


if __name__ == "__main__":
    app.run(debug=True)
