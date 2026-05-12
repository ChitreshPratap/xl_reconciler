from pathlib import Path

from nicegui import ui
import GlobalStylesheet
from nicegui import app
from src.screens.BaseView import BaseView
from src.screens.ViewReconcileReport import ViewReconcileReport
from src.customparts.Footer import Footer
from src.customparts.Header import Header
from src.customparts.SideBar import Sidebar


# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = Path(__file__).resolve().parent
# app.add_static_files('/static', BASE_DIR/ 'static')

class MainApplication:

    def __init__(self):

        self.content_area = None

    def build(self):
        # GlobalStylesheet.GlobalStyles.loadStyleSheet()
        # ui.add_css_files("static/styles/app.css")
        # self.add_global_styles()
        # ui.add_css("/static/styles/app.css")

        ui.add_head_html("""
            <link rel="stylesheet" href="/static/styles/app.css">
        """)
        Header().render()
        with ui.row().classes('w-full').style(
            'height: calc(100vh - 110px);'):
            Sidebar(self).render()
            # with ui.column().classes(
            #     'flex-grow p-6 bg-gray-100 overflow-auto'
            # ) as self.content_area:
            #     pass
            with ui.column().classes(
                'content-area'
            ) as self.content_area:
                pass

        Footer().render()
        self.load_view(ViewReconcileReport())

    def load_view(self, view: BaseView):

        self.content_area.clear()
        with self.content_area:
            view.render()

    # def add_global_styles(self):

    #     ui.add_head_html("""

    #     <style>

    #         body {
    #             margin: 0;
    #             background-color: #f5f7fb;
    #             font-family: Arial, sans-serif;
    #         }

    #     </style>

    #     """)

