from nicegui import run

from src.facilities.ExcelReconcileFacility import ExcelReconcileService

class ConciliatorReconcileReport:

    def __init__(self):
        self.input_folder = None
        self._excel_file_count = None
        self.output_folder = None
        self.service = ExcelReconcileService()

    def validate(self):

        if not self.input_folder:
            return False, (
                'Please select input folder'
            )
        if not self._excel_file_count:
            return False, (
                'No excel file found to process.'
            )
        # if not self.output_folder:
        #     return False, (
        #         'Please select output folder'
        #     )

        return True, ''

    async def generate_report(self,ehandler):

        result = await run.io_bound(
            self.service.process_files,
            self.input_folder,
            self.output_folder,
            ehandler
        )
        
        # loop = asyncio.get_running_loop()

        # result = await loop.run_in_executor(
        #     None,
        #     lambda: self.service.process_files(
        #         self.input_folder,
        #         self.output_folder,
        #         ehandler
        #     )
        # )
        return result