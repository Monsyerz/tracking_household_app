from flask import Flask, render_template, request
from models import Person, Expense, HouseholdBudget
from calculator import calculate_total_income, calculate_total_expenses, calculate_money_left

app = Flask(__name__)


@app.route("/")
def index():
    """Display the home page."""
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    """Calculate budget summary from form data."""
    budget = HouseholdBudget()

    person_name = request.form["person_name"]
    weekly_income = float(request.form["weekly_income"])

    budget.people.append(Person(person_name, weekly_income))

    budget.expenses.append(Expense("Rent / Housing", float(request.form["rent"])))
    budget.expenses.append(Expense("Food", float(request.form["food"])))
    budget.expenses.append(Expense("Car", float(request.form["car"])))

    total_income = calculate_total_income(budget.people)
    total_expenses = calculate_total_expenses(budget.expenses)
    money_left = calculate_money_left(total_income, total_expenses)

    return render_template(
        "result.html",
        total_income=total_income,
        total_expenses=total_expenses,
        money_left=money_left,
    )


if __name__ == "__main__":
    app.run(debug=True)