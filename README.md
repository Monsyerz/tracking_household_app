# Household Budget Tracker

Household Budget Tracker is a modular command-line Python application for estimating a household's monthly budget. It collects income and expense information, performs the calculations in separate modules, and prints a clear summary. The repository also contains a basic Flask interface that reuses the calculation modules.

## Current Features

- Add multiple household members and their weekly income
- Estimate monthly income from weekly income
- Record fixed monthly expenses in common household categories
- Add custom expense categories
- Calculate total household income and total expenses
- Calculate the money remaining after expenses
- Validate numeric input in the command-line workflow

The application processes one budget during each run. It does not currently save or load financial data.

## Project Structure

```text
tracking_household_app/
|-- main.py
|-- input_handler.py
|-- models.py
|-- calculator.py
|-- report.py
|-- app.py
|-- templates/
|   |-- index.html
|   `-- result.html
|-- static/
|   |-- style.css
|   `-- script.js
|-- requirements.txt
|-- HouseholdBudgetTracker.spec
`-- README.md
```

## Running the Command-Line Application

From the project directory, run:

```bash
python main.py
```

Follow the prompts to enter household members, weekly income, fixed expenses, and any custom expense categories.

## Technologies

- Python
- Flask
- HTML, CSS, and JavaScript for the basic web interface

## Planned Improvements

The following features are planned and are not implemented yet:

- Saving and loading budget data
- Savings goals
- Stronger input validation
- Automated tests
- Monthly summaries
- CSV export
- Charts or a more complete graphical interface

## Project Status

This is an active learning and portfolio project.
