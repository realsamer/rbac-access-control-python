roles = {
    "Admin": ["Create", "View", "Update", "Delete"],
    "Manager": ["View", "Update"],
    "Customer": ["View"]
}

users = {}


def assign_role():
    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    role = input("Enter role (Admin, Manager, Customer): ").strip().capitalize()

    if role not in roles:
        print("Invalid role.")
        return

    users[username] = role
    print("Role assigned successfully.")


def check_access():
    username = input("Enter username: ").strip()

    if username not in users:
        print("User not found.")
        return

    action = input("Enter action (Create, View, Update, Delete): ").strip().capitalize()

    if action not in ["Create", "View", "Update", "Delete"]:
        print("Invalid action.")
        return

    role = users[username]

    if action in roles[role]:
        print("Access allowed: " + username + " can " + action.lower() + " accounts.")
    else:
        print("Access denied: " + username + " cannot " + action.lower() + " accounts.")


def show_permissions():
    print("\nRoles and Permissions")

    for role, permissions in roles.items():
        print(role + ": " + ", ".join(permissions))


def show_users():
    print("\nUsers and Their Roles")

    if not users:
        print("No users assigned.")
        return

    for username, role in users.items():
        print(username + ": " + role)


while True:
    print("\nRBAC Access Control System")
    print("--------------------------")
    print("1. Assign role to user")
    print("2. Check account access")
    print("3. Show role permissions")
    print("4. Show users")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        assign_role()
    elif choice == "2":
        check_access()
    elif choice == "3":
        show_permissions()
    elif choice == "4":
        show_users()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
