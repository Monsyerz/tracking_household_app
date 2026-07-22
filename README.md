# Household Budget Tracker

Household Budget Tracker is a modular command-line Python application for estimating a household's monthly budget. It collects income and expense information, performs the calculations in separate modules, and prints a clear summary. The repository also contains a basic Flask interface that reuses the calculation modules.

## Current Features

- Add multiple household members and their weekly income
- Estimate monthly income from weekly income
- Record fixed monthly expenses in common household categories
- Add custom expense categories
- Set a non-negative monthly savings goal
- Calculate total household income and total expenses
- Calculate the money remaining after expenses and planned savings
- Validate names, household size, numeric amounts, and yes/no answers
- Save the current budget to a local JSON file
- Load an existing budget without re-entering its details
- Handle missing or invalid saved data without crashing
- Use a command-line menu to manage the current budget
- Add, edit, and remove household members
- Add, edit, and delete expenses
- Update the savings goal and save changes when ready
- Protect unsaved changes before replacing a budget or exiting

The application works with one current budget stored in `data/current_budget.json`.

## Project Structure

```text
tracking_household_app/
|-- main.py
|-- input_handler.py
|-- models.py
|-- calculator.py
|-- report.py
|-- storage.py
|-- menu.py
|-- data/
|   `-- .gitkeep
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

Use the numbered menu to create or load a budget, view its report, manage household members and expenses, update the savings goal, and save changes. Menu selections and financial values are validated before they are used.

The application warns before replacing a budget or exiting when unsaved changes exist. You can save those changes before exiting.

The generated JSON file contains user-entered financial data and is ignored by Git. Do not commit it to the repository.

## Running the Web Interface

Install the required package and start the Flask server from the project directory:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/` in a browser and keep the terminal running. The HTML templates must be served by Flask; opening `templates/index.html` directly or using a static preview server will not run the budget calculation route.

## Technologies

- Python
- Flask
- HTML, CSS, and JavaScript for the basic web interface

## Planned Improvements

The following features are planned and are not implemented yet:

- Additional validation for more input edge cases
- Automated tests
- Monthly summaries
- CSV export
- Charts or a more complete graphical interface

## Project Status

This is an active learning and portfolio project.
