
class StructReconcileRecord:

    def __init__(
        self,
        file_name='',
        m13='',
        g14='',
        status='SUCCESS',
        error_message=''
    ):

        self.file_name = file_name
        self.m13 = m13
        self.g14 = g14

        self.status = status
        self.error_message = error_message
        