import tkinter as tk
from tkinter import filedialog
from nicegui import ui

# --- 1. INCORPORATE YOUR CSS ---
ui.add_head_html('''
<style>
    :root {
        --primary: #4f46e5;
        --bg-main: #f8fafc;
        --text-dark: #0f172a;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
    }
    .header-nav-button {
        min-width: 160px;
        height: 50px;
        background-color: var(--primary) !important;
        color: white !important;
        border-radius: 12px;
        font-weight: 600;
        cursor: pointer;
        border: none;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
        transition: transform 0.2s;
    }
    .header-nav-button:hover { transform: translateY(-2px); }
    .content-card {
        background: white;
        border-radius: 24px;
        padding: 40px;
        border: 1px solid var(--border-color);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
    }
</style>
''')

# --- 2. LOGIC TO GET TRUE PATH ---
def select_excel_path(label_control):
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Bring the dialog to the front
    
    # Open the Windows File Selector
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    
    root.destroy()
    
    # Update the NiceGUI label with the REAL path
    if file_path:
        label_control.set_text(file_path)
    else:
        label_control.set_text("Selection cancelled.")

# --- 3. THE UI LAYOUT ---
with ui.column().classes('w-full items-center p-8 bg-slate-50 min-h-screen'):
    
    with ui.column().classes('w-full max-w-3xl gap-6'):
        ui.label('File Management').classes('text-4xl font-extrabold text-slate-900')
        
        with ui.card().classes('content-card w-full'):
            ui.label('Local Excel Selector').classes('text-xl font-bold text-slate-800 mb-2')
            ui.label('Click the button below to pick a file from your computer and retrieve its full system path.').classes('text-slate-500 mb-6')
            
            # This is where the full path will be displayed
            path_display = ui.label('No file path selected').classes('p-4 bg-slate-100 rounded-lg text-indigo-700 font-mono break-all border border-slate-200')
            
            # The styled button
            ui.button('SELECT EXCEL FILE', on_click=lambda: select_excel_path(path_display)).classes('header-nav-button mt-6')

# Run the app
ui.run(title="Excel Path Picker", native=True)