# =========================================================
# RECONCILE REPORT VIEW
# =========================================================
import asyncio
from pathlib import Path
from nicegui import ui,run
import FileUtility
from src.screens.BaseView import BaseView
from src.conciliator.ConciliatorReconcileReport import ConciliatorReconcileReport

class ViewReconcileReport(BaseView):

    def __init__(self):

        super().__init__(
            "Reconcile Report",
            "Upload reconciliation files and generate reports."
        )
        self._conciliator = ConciliatorReconcileReport()
        self.progress_bar = None
        self.progress_label =None        
        self.selected_folder_label = None

    def handle_upload(self, e):
        self.selected_file_label.set_text(f"Selected File: {e.name}")

    async def choose_folder(self):
        choosedFolder =await run.io_bound( FileUtility.selectFolder)
        # choosedFolder = FileUtility.selectFolder()
        if choosedFolder:
            self._conciliator.input_folder=choosedFolder
            self.selected_folder_label.set_text(choosedFolder)
            try:
                tPath = Path(choosedFolder)
                tFileCount = len(list(tPath.glob("*.xls*")))
                self._conciliator._excel_file_count = tFileCount
                self.file_count_label.set_text(f"{tFileCount} excel files found")
                self.file_count_label.set_visibility(True)
            except Exception as e:
                print(f"Error counting files :{e}")
                ui.notify(f"System Error: {str(e)}", 
                          type='negative', position='top',
                          classes="uiNotification")


        else:
            self._conciliator.input_folder=None
            self._conciliator._excel_file_count = 0
            self.selected_folder_label.set_text("No folder selected")
            self.file_count_label.set_visibility(False)

    def choose_file(self):
        choosedFile = FileUtility.selectExcelFile()        
        if choosedFile:            
            self.selected_file_label.set_text(choosedFile)
        else:
            self.selected_file_label.set_text("No file selected")

    def handle_event(self,event_data):

        event_name = event_data.get('event')

        if event_name == 'progress_changed':
            current = event_data['current']
            total = event_data['total']
            file_name = event_data['file_name']
            status = event_data['status']
            progress = (current / total)
            progressPercent = int(progress*100)
            self.progress_bar.set_value(progress)
            self.progress_label.set_text(
                f"{progressPercent}% -> {file_name} | {status} "
                # f'[{current}/{total}] '
                # f'{file_name} - {status}'
            )

        elif event_name == 'completed':
            # output_file = event_data['output_file']
            self.progress_bar.set_value(1)
            self.progress_label.set_text(
                '100% -> Completed Successfully '
            )

        elif event_name == 'folder_creation_failed':
            self.progress_label.set_text(
                'Folder creation failed'
            )


    async def processReport(self):

        valid, message = self._conciliator.validate()
        if not valid:
            ui.notify(message,type='negative',
                      classes="uiNotification",
                      position="top"
                      )
            return
                
        # RESET
        self.progress_bar.set_value(0)
        self.progress_label.set_text(
            'Processing Started...'
        )

        # # START PROCESS
        # await self._conciliator.generate_report(

        #     self.handle_event
        
        # )

    # =============================================
        # START PROCESS
        # =============================================
        try:

            output_file = await (
                self._conciliator.generate_report(
                    self.handle_event
                )
            )

            # =========================================
            # SUCCESS NOTIFICATION
            # =========================================

            ui.notify(
                f'Report Generated Successfully\n'
                f'{output_file}',
                type='positive',
                position='top',
                classes='uiNotification'
            )

        except Exception as ex:

            ui.notify(
                f'System Error:\n{str(ex)}',
                type='negative',
                position='top',
                classes='uiNotification'
            )
    def render_content(self):
        
        with ui.column().classes('w-full gap-4'):

            ui.label('Click the button below to pick a folder having all input files.')

            with ui.row().classes('folder-selection-row'):
                ui.button('Select Folder',
                        icon="file_upload",
                        on_click=self.choose_folder
                        ).classes('browse-button')
                self.file_count_label = ui.label('').classes('excel-count-badge')
                self.file_count_label.set_visibility(False)
            
            # SELECTED FILE LABEL
            self.selected_folder_label = ui.label('No folder selected').classes('file-path-display')

            # Progress Bar
            self.progress_bar = ui.linear_progress(show_value=False,value=0).classes("progressReconcileReport")
            self.progress_label = ui.label('Progress not started')
            # GENERATE BUTTON
            ui.button(
                "Generate Report",
                icon='bolt',
                 on_click=self.processReport).classes('card-action-button')
    def render(self):
        return super().render()
        