
from nicegui import ui

class Footer:
    
    def render(self):

        with ui.footer().classes('app-footer'):
            ui.label('© 2026 Enterprise Dashboard')
