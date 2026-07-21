import json
from pathlib import Path

from models import HouseholdBudget


DATA_DIRECTORY = Path(__file__).parent / "data"
DEFAULT_BUDGET_FILE = DATA_DIRECTORY / "current_budget.json"


def save_budget(
    budget: HouseholdBudget,
    file_path: Path = DEFAULT_BUDGET_FILE,
) -> bool:
    """Save a household budget as JSON and return whether it succeeded."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(budget.to_dict(), file, indent=4)
    except OSError as error:
        print(f"The budget could not be saved: {error}")
        return False

    return True


def load_budget(
    file_path: Path = DEFAULT_BUDGET_FILE,
) -> HouseholdBudget | None:
    """Load and validate a saved budget, or return None if loading fails."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No saved budget was found.")
        return None
    except json.JSONDecodeError:
        print("The saved budget contains invalid JSON and could not be loaded.")
        return None
    except OSError as error:
        print(f"The saved budget could not be read: {error}")
        return None

    try:
        return HouseholdBudget.from_dict(data)
    except (TypeError, ValueError):
        print("The saved budget contains invalid data and could not be loaded.")
        return None
