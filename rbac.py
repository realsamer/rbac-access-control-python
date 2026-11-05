
roles = {
    "Admin": ["Create", "View", "Update", "Delete"],
    "Manager": ["View", "Update"],
    "Customer": ["View"]
}

users = {}

print("RBAC Roles and Permissions")
print("--------------------------")

for role, permissions in roles.items():
    print(role + ": " + ", ".join(permissions))

print("\nAssign Roles to Users")
print("---------------------")

while True:
    username = input("\nEnter username (or 'done' to finish): ").strip()

    if username.lower() == "done":
        break

    if username == "":
        print("Username cannot be empty.")
        continue

    role = input("Enter role (Admin, Manager, Customer): ").strip().capitalize()

    if role in roles:
        users[username] = role
        print("Role assigned successfully.")
    else:
        print("Invalid role.")

print("\nUsers and Their Roles")
print("---------------------")

for username, role in users.items():
    print(username + ": " + role)
