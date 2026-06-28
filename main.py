from input_handler import create_household_budget
from report import print_budget_report


def main():
    """Run the household budget tracker application."""
    budget = create_household_budget()
    print_budget_report(budget)


if __name__ == "__main__":
    main()