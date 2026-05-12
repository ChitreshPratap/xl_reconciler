from nicegui import ui

class MainPage:

    @staticmethod
    @ui.page('/')
    def show():
        ui.label(
            '🚀 Recon Vault').classes('text-3xl font-bold')
        ui.button('Start',
                  on_click=lambda:ui.notify(message="Application Started",
                                            position="top",close_button=True,type="info",color="yellow"
                                            )
        )


