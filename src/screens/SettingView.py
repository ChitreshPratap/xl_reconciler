from nicegui import ui

from src.screens.BaseView import BaseView

class SettingsView(BaseView):

    def __init__(self):
        super().__init__(
            "Settings",
            "Configure application settings."
        )

    def render_content(self):

        ui.switch("Enable Notifications")
        ui.switch("Dark Mode")
        ui.switch("Auto Backup")

