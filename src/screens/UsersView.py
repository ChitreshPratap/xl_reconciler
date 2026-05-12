from nicegui import ui

from src.screens.BaseView import BaseView


class UsersView(BaseView):

    def __init__(self):
        super().__init__(
            "Users",
            "Manage users and permissions."
        )

    def render_content(self):

        rows = [
            {'name': 'John', 'role': 'Admin'},
            {'name': 'David', 'role': 'Manager'},
            {'name': 'Emma', 'role': 'User'},
        ]

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name'},
            {'name': 'role', 'label': 'Role', 'field': 'role'},
        ]

        ui.table(
            columns=columns,
            rows=rows
        )
