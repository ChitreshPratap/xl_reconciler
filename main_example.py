from nicegui import ui
from MainPage import MainPage
from MainApplication import MainApplication


class Application:

    def __init__(self):
        MainPage()

    def run(self):

        ui.run(
            native=True,
            window_size=(1200, 800),
            fullscreen=False,
            reload=True,
            title='Enterprise Desktop App',
        )


if __name__ in {'__main__', '__mp_main__'}:
    app = MainApplication()
    app.build()
    ui.run(
        title="Enterprise Dashboard",
        reload=False
    )