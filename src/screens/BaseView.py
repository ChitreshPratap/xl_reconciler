from nicegui import ui

class BaseView:

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def render_header(self):
        
        ui.label(self.title).classes('view-title')
        ui.label(self.description).classes('view-description')

    def render_content(self):
        """Override in child classes"""
        pass

    def render(self):

        with ui.column().classes('view-container'):
            self.render_header()
            with ui.card().classes('content-card'):
                self.render_content()

