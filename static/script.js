const memberList = document.querySelector("#member-list");
const addMemberButton = document.querySelector("#add-member-button");

function createMemberRow() {
    const row = document.createElement("div");
    row.className = "household-member";

    row.innerHTML = `
        <label>
            Name
            <input type="text" name="person_name" placeholder="Household member name" required>
        </label>

        <label>
            Weekly income
            <input type="number" name="weekly_income" min="0" step="0.01" placeholder="0.00" required>
        </label>

        <button class="remove-member-button" type="button">Remove</button>
    `;

    row.querySelector(".remove-member-button").addEventListener("click", function () {
        row.remove();
    });

    return row;
}

addMemberButton.addEventListener("click", function () {
    memberList.appendChild(createMemberRow());
});
