
roles = {
    "Admin": ["Create", "View", "Update", "Delete"],
    "Manager": ["View", "Update"],
    "Customer": ["View"]
}

print("RBAC Roles and Permissions")
print("--------------------------")

for role, permissions in roles.items():
    print(role + ": " + ", ".join(permissions))
