from nicegui import ui

from src.screens.ReportsView import ReportsView
from src.screens.SettingView import SettingsView
from src.screens.UsersView import UsersView
from src.screens.ViewReconcileReport import ViewReconcileReport

class Sidebar:

    def __init__(self, app):
        self.app = app

    def render(self):

        with ui.column().classes('sidebar'):

            ui.label("MENU").classes('sidebar-title')

            self.menu_button(
                "Reconcile Report",
                "receipt_long",
                ViewReconcileReport
            )

            self.menu_button(
                "Users",
                "people",
                UsersView
            )

            self.menu_button(
                "Reports",
                "bar_chart",
                ReportsView
            )

            self.menu_button(
                "Settings",
                "settings",
                SettingsView
            )


    def menu_button(self, text, icon, view_class):

        ui.button(
            text,
            icon=icon,
            on_click=lambda: self.app.load_view(view_class())
        ).classes('sidebar-button')

