from input_handler import (
    create_household_budget,
    get_non_empty_text,
    get_non_negative_number,
    get_positive_whole_number,
    get_yes_no,
)
from models import Expense, HouseholdBudget, Person
from report import print_budget_report
from storage import load_budget, save_budget


MENU_OPTIONS = (
    "Create a new household budget",
    "Load a saved budget",
    "View the current budget report",
    "Add a household member",
    "Edit a household member",
    "Remove a household member",
    "Add an expense",
    "Edit an expense",
    "Delete an expense",
    "Set or update the savings goal",
    "Save the current budget",
    "Exit",
)


def get_menu_choice() -> int:
    """Ask for a valid main menu selection."""
    while True:
        choice = get_positive_whole_number("Choose an option: ")
        if choice <= len(MENU_OPTIONS):
            return choice

        print(f"Please enter a number from 1 to {len(MENU_OPTIONS)}.")


def get_item_index(item_count: int, item_name: str) -> int:
    """Ask the user to select an existing item and return its list index."""
    while True:
        choice = get_positive_whole_number(f"Choose a {item_name} number: ")
        if choice <= item_count:
            return choice - 1

        print(f"Please enter a number from 1 to {item_count}.")


class BudgetApplication:
    """Manage the command-line menu and the current budget state."""

    def __init__(self) -> None:
        self.budget: HouseholdBudget | None = None
        self.has_unsaved_changes = False

    def show_menu(self) -> None:
        """Display all available command-line actions."""
        print("\nHousehold Budget Tracker")
        print("-" * 30)
        for number, option in enumerate(MENU_OPTIONS, start=1):
            print(f"{number}. {option}")

    def run(self) -> None:
        """Run the application menu until the user chooses to exit."""
        while True:
            self.show_menu()
            choice = get_menu_choice()

            if choice == 1:
                self.create_new_budget()
            elif choice == 2:
                self.load_saved_budget()
            elif choice == 3:
                self.view_report()
            elif choice == 4:
                self.add_household_member()
            elif choice == 5:
                self.edit_household_member()
            elif choice == 6:
                self.remove_household_member()
            elif choice == 7:
                self.add_expense()
            elif choice == 8:
                self.edit_expense()
            elif choice == 9:
                self.delete_expense()
            elif choice == 10:
                self.update_savings_goal()
            elif choice == 11:
                self.save_current_budget()
            elif self.confirm_exit():
                print("Goodbye.")
                break

    def confirm_replacing_unsaved_budget(self, action: str) -> bool:
        """Confirm an action that would discard unsaved budget changes."""
        if not self.has_unsaved_changes:
            return True

        return get_yes_no(
            f"You have unsaved changes. Continue and {action}? (yes/no): "
        )

    def require_budget(self) -> bool:
        """Return whether a budget exists and show guidance when it does not."""
        if self.budget is not None:
            return True

        print("No current budget. Create or load a budget first.")
        return False

    def create_new_budget(self) -> None:
        """Collect a new budget after protecting unsaved work."""
        if not self.confirm_replacing_unsaved_budget("create a new budget"):
            print("New budget creation cancelled.")
            return

        self.budget = create_household_budget()
        self.has_unsaved_changes = True
        print("New budget created. Remember to save your changes.")

    def load_saved_budget(self) -> None:
        """Load the saved budget after protecting unsaved work."""
        if not self.confirm_replacing_unsaved_budget("load another budget"):
            print("Loading cancelled.")
            return

        saved_budget = load_budget()
        if saved_budget is None:
            return

        self.budget = saved_budget
        self.has_unsaved_changes = False
        print("Saved budget loaded successfully.")

    def view_report(self) -> None:
        """Display the current budget report when a budget exists."""
        if self.require_budget():
            print_budget_report(self.budget)

    def show_household_members(self) -> None:
        """Display numbered household members."""
        if self.budget is None:
            return

        print("\nHousehold Members:")
        for number, person in enumerate(self.budget.people, start=1):
            print(f"{number}. {person.name} - ${person.weekly_income:,.2f} weekly")

    def add_household_member(self) -> None:
        """Add a household member to the current budget."""
        if not self.require_budget():
            return

        name = get_non_empty_text("Enter household member name: ")
        weekly_income = get_non_negative_number("Enter weekly income: ")
        self.budget.people.append(Person(name, weekly_income))
        self.has_unsaved_changes = True
        print("Household member added.")

    def edit_household_member(self) -> None:
        """Edit an existing household member."""
        if not self.require_budget():
            return
        if not self.budget.people:
            print("There are no household members to edit.")
            return

        self.show_household_members()
        index = get_item_index(len(self.budget.people), "household member")
        person = self.budget.people[index]
        person.name = get_non_empty_text("Enter the updated name: ")
        person.weekly_income = get_non_negative_number(
            "Enter the updated weekly income: "
        )
        self.has_unsaved_changes = True
        print("Household member updated.")

    def remove_household_member(self) -> None:
        """Remove an existing household member after confirmation."""
        if not self.require_budget():
            return
        if not self.budget.people:
            print("There are no household members to remove.")
            return

        self.show_household_members()
        index = get_item_index(len(self.budget.people), "household member")
        person = self.budget.people[index]
        if not get_yes_no(f"Remove {person.name}? (yes/no): "):
            print("Removal cancelled.")
            return

        del self.budget.people[index]
        self.has_unsaved_changes = True
        print("Household member removed.")

    def show_expenses(self) -> None:
        """Display numbered expense categories."""
        if self.budget is None:
            return

        print("\nExpenses:")
        for number, expense in enumerate(self.budget.expenses, start=1):
            print(f"{number}. {expense.category} - ${expense.amount:,.2f}")

    def add_expense(self) -> None:
        """Add an expense to the current budget."""
        if not self.require_budget():
            return

        category = get_non_empty_text("Enter expense category: ")
        amount = get_non_negative_number("Enter monthly expense amount: ")
        self.budget.expenses.append(Expense(category, amount))
        self.has_unsaved_changes = True
        print("Expense added.")

    def edit_expense(self) -> None:
        """Edit an existing expense."""
        if not self.require_budget():
            return
        if not self.budget.expenses:
            print("There are no expenses to edit.")
            return

        self.show_expenses()
        index = get_item_index(len(self.budget.expenses), "expense")
        expense = self.budget.expenses[index]
        expense.category = get_non_empty_text("Enter the updated category: ")
        expense.amount = get_non_negative_number(
            "Enter the updated monthly amount: "
        )
        self.has_unsaved_changes = True
        print("Expense updated.")

    def delete_expense(self) -> None:
        """Delete an existing expense after confirmation."""
        if not self.require_budget():
            return
        if not self.budget.expenses:
            print("There are no expenses to delete.")
            return

        self.show_expenses()
        index = get_item_index(len(self.budget.expenses), "expense")
        expense = self.budget.expenses[index]
        if not get_yes_no(f"Delete {expense.category}? (yes/no): "):
            print("Deletion cancelled.")
            return

        del self.budget.expenses[index]
        self.has_unsaved_changes = True
        print("Expense deleted.")

    def update_savings_goal(self) -> None:
        """Set the monthly savings goal for the current budget."""
        if not self.require_budget():
            return

        self.budget.savings_goal = get_non_negative_number(
            "Enter the monthly savings goal: "
        )
        self.has_unsaved_changes = True
        print("Savings goal updated.")

    def save_current_budget(self) -> bool:
        """Save the current budget and update its unsaved state."""
        if not self.require_budget():
            return False

        if not save_budget(self.budget):
            return False

        self.has_unsaved_changes = False
        print("Budget saved to data/current_budget.json.")
        return True

    def confirm_exit(self) -> bool:
        """Confirm exiting and offer to save unsaved changes first."""
        if not self.has_unsaved_changes:
            return True

        if get_yes_no("Save changes before exiting? (yes/no): "):
            if self.save_current_budget():
                return True

            return get_yes_no("Saving failed. Exit without saving? (yes/no): ")

        return get_yes_no("Exit without saving? (yes/no): ")


def run_application() -> None:
    """Create and run the command-line budget application."""
    application = BudgetApplication()
    application.run()
