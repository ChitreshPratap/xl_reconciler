
from nicegui import ui

from src.screens.BaseView import BaseView

class ReportsView(BaseView):

    def __init__(self):
        super().__init__(
            "Reports",
            "Generate and export reports."
        )

    def render_content(self):

        ui.label("Available Reports")

        with ui.column().classes('gap-2'):

            ui.button("Sales Report", icon='download')
            ui.button("User Report", icon='download')
            ui.button("Audit Report", icon='download')


