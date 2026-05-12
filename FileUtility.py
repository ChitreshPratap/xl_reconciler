from pathlib import Path
import sys
import tkinter as tk
from tkinter import filedialog


def get_base_path():

    # =====================================
    # PYINSTALLER
    # =====================================

    if getattr(sys, 'frozen', False):

        return Path(sys._MEIPASS)

    # =====================================
    # NORMAL PYTHON
    # =====================================

    return Path(__file__).resolve().parent

def selectFolder():

    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Bring the dialog to the front
    # Open the Windows File Selector
    folderPath = filedialog.askdirectory()    
    root.update()
    root.destroy()
    return folderPath

def selectExcelFile():

    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Bring the dialog to the front
    
    # Open the Windows File Selector
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx *.xlsb *.xlsm *.xls *.xls*")]
    )    
    root.destroy()
    if file_path:
        resultPath = file_path
    else:
        resultPath = ""
    
    return resultPath
