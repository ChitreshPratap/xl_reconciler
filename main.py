from pathlib import Path
from nicegui import ui
from nicegui import native
from nicegui import app
import FileUtility
from MainApplication import MainApplication

BASE_DIR = FileUtility.get_base_path()

# BASE_DIR = Path(__file__).resolve().parent
# ui.add_static_files(
#     '/static',
#     BASE_DIR / 'static'
# )

app.add_static_files(
    '/static',
    BASE_DIR / 'static'
)

@ui.page('/')
def home():
    app = MainApplication()
    app.build()
    
if __name__ in {'__main__', '__mp_main__'}:    
    # app.native.window_args['resizable'] = False 
    # app = MainApplication()
    # app.build()
    ui.run(
        #    native=True,
            window_size=(1200, 800),
            # fullscreen=False,
            on_air=True,
            reload=False,
            title='Recon Vault',
            # port=native.find_free_port() if 'native' in locals() else 8080
            favicon="static/icons/appLogo256.ico"
    )
    # app.native.window.setWindowIcon(QIcon(str(ICON_PATH)))
    # app.native.window.


# 46

# This is a Python 3.10 issue. To fix it: You have to go to the folder "Python310\Lib" and edit the file 'dis.py'. In the 'dis.py' file you have to find this "def _unpack_opargs" and inside the else statement write a new line with this: "extended_arg = 0", then save the file.

# I did something like that:

# else:
#     arg = None
#     extended_arg = 0 
# yield (i, op, arg)
# and everything is working fine now.