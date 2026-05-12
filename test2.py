from nicegui import ui
from nicegui import app

app.add_static_files(
    '/static',
    'static'
)

@ui.page('/')

def home():

    ui.label('Hello')

if __name__ in {'__main__', '__mp_main__'}:    
    ui.run(
           native=True,
            window_size=(1200, 800),
            fullscreen=False,
            reload=True,
            title='Recon Vault'
    )