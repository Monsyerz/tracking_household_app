from input_handler import create_household_budget, get_yes_no
from models import HouseholdBudget
from report import print_budget_report
from storage import load_budget, save_budget


def load_or_create_budget() -> HouseholdBudget:
    """Load a saved budget when requested, or collect a new budget."""
    if get_yes_no("Do you want to load the saved budget? (yes/no): "):
        saved_budget = load_budget()
        if saved_budget is not None:
            print("Saved budget loaded successfully.")
            return saved_budget

        print("A new budget will be created instead.")

    budget = create_household_budget()
    if save_budget(budget):
        print("\nBudget saved to data/current_budget.json.")
    return budget


def main():
    """Run the household budget tracker application."""
    budget = load_or_create_budget()
    print_budget_report(budget)


if __name__ == "__main__":
    main()
