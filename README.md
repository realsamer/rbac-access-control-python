# RBAC Access Control - Python

A simple Python program that implements Role-Based Access Control (RBAC) for an Account object.

This project was created for the Software Security course, Chapter 4: Access Control.

## Roles and Permissions

The program has three roles:

- Admin: Create, View, Update, Delete
- Manager: View, Update
- Customer: View

## Features

- Assign roles to users.
- Check if a user can perform an action.
- Display all roles and their permissions.
- Display users and their assigned roles.
- Allow or deny access based on permissions.

## How to Run

Make sure Python 3 is installed.

Run the program:

```bash
python rbac.py
```

The program will display a menu. Choose an option to assign roles, check permissions, or view users.

## Notes

User roles are stored in memory and will be cleared when the program closes.
