from nicegui import ui

class Header:

    def render(self):
                
        with ui.header().classes('app-header'):

            with ui.row().classes('header-left'):
                ui.image('./static/icons/appLogo512.png').classes('app-logo')
                # ui.icon('apps').classes("app-icon")
                ui.label('Recon Vault').classes('app-title')

            with ui.row().classes('header-nav'):
                ui.button('Home').classes("header-nav-button")
                ui.button('About').classes("header-nav-button")
                ui.button('Contact').classes("header-nav-button")

