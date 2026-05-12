from nicegui import ui


# =========================================================
# GLOBAL STYLES
# =========================================================

class GlobalStyles:

    @staticmethod
    def loadStyleSheet():

        ui.add_head_html("""
    <style>
/* =====================================================
    GLOBAL RESET & VARIABLES
===================================================== */
:root {
    --primary: #4f46e5;
    --primary-hover: #4338ca;
    --primary-glow: rgba(79, 70, 229, 0.15);
    --bg-main: #f8fafc;
    --text-dark: #0f172a;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    --card-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
    
    /* Layout Constants */
    --header-height: 85px;
    --footer-height: 40px;
    --layout-gap: 20px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-family: 'Inter', "Segoe UI", Roboto, sans-serif;
    background: var(--bg-main);
    color: var(--text-dark);
    -webkit-font-smoothing: antialiased;
}

/* Quasar Specific Overrides */
.q-layout, .q-page-container, .q-page {
    width: 100%;
    height: 100%;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden;
    background: var(--bg-main);
}

/* =====================================================
    HEADER SECTION
===================================================== */
.app-header {
    width: 100%;
    height: var(--header-height);
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    border-bottom: 1px solid var(--border-color);
    position: relative;
    z-index: 1000;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 18px;
}

    .app-logo {

        width: 48px;
        height: 48px;
        object-fit: contain;
        border-radius: 12px;
        background: white;
        padding: 4px;
        box-shadow:0 2px 8px rgba(0,0,0,0.08);
    }
                         
.app-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: white;
    font-size: 24px;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.35);
    transition: transform 0.2s ease;
}

.app-title {
    color: var(--text-dark);
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -0.6px;
}

/* HEADER NAVIGATION & LARGE BUTTONS */
.header-nav {
    display: flex;
    align-items: center;
    gap: 16px;
}

.header-nav-button {
    min-width: 140px; /* Forces larger size */
    height: 50px;
    padding: 0 28px;
    border-radius: 12px;
    background: var(--primary) !important;
    color: white !important;
    font-size: 16px;
    font-weight: 600;
    text-transform: none;
    white-space: nowrap;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 12px var(--primary-glow);
}

.header-nav-button:hover {
    transform: translateY(-2px);
    background: var(--primary-hover) !important;
    box-shadow: 0 8px 20px rgba(79, 70, 229, 0.25);
}

/* =====================================================
    MAIN LAYOUT (Structure Fix)
===================================================== */
.main-layout {
    width: 100%;
    /* Subtracts Header, Footer, and the 20px gap we want at the bottom */
    height: calc(100vh - var(--header-height) - var(--footer-height) - var(--layout-gap));
    display: flex;
    flex-direction: row;
    padding: 20px 25px 0 25px; 
    gap: 25px;
    margin-bottom: var(--layout-gap); /* Space between content and footer */
    overflow: hidden;
}

/* =====================================================
    SIDEBAR (Fixed Overlap)
===================================================== */
.sidebar {
    width: 280px;
    height: 100%;
    background: white;
    border-radius: 24px;
    padding: 24px 16px;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border-color);
    box-shadow: var(--card-shadow);
    overflow-y: auto;
}

.sidebar-title {
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding-left: 12px;
    margin-bottom: 20px;
    opacity: 0.8;
}

.sidebar-button {
    width: 100%;
    height: 52px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    margin-bottom: 8px;
    border-radius: 14px;
    background: transparent !important;
    color: var(--text-muted) !important;
    font-size: 15px;
    font-weight: 500;
    transition: all 0.2s ease;
    text-decoration: none;
    border: none;
}

.sidebar-button .q-icon {
    font-size: 22px;
    margin-right: 14px;
    color: var(--primary);
}

.sidebar-button:hover {
    background: var(--primary-glow) !important;
    color: var(--primary) !important;
    transform: translateX(5px);
}

/* =====================================================
    CONTENT AREA
===================================================== */
.content-area {
    flex: 1;
    height: 100%;
    overflow-y: auto;
    padding-right: 10px;
}

.view-title {
    font-size: 32px;
    font-weight: 800;
    color: var(--text-dark);
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}

.view-description {
    font-size: 1rem;
    color: var(--text-muted); /* Muted small text */
    margin-bottom: 20px;
    font-weight: 400;
}
.view-description {
    font-size: 16px;
    color: var(--text-muted);
    margin-bottom: 28px;
}

.content-card {
    background: white;
    border-radius: 24px;
    padding: 32px;
    border: 1px solid var(--border-color);
    box-shadow: var(--card-shadow);
    margin-bottom: 20px;
}

/* =====================================================
    FOOTER
===================================================== */
.app-footer {
    width: 100%;
    height: var(--footer-height);
    background: white;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: 500;
    border-top: 1px solid var(--border-color);
    position: relative;
    z-index: 5;
}

/* Smooth Scrollbar for Content */
.content-area::-webkit-scrollbar, 
.sidebar::-webkit-scrollbar {
    width: 6px;
}
.content-area::-webkit-scrollbar-thumb, 
.sidebar::-webkit-scrollbar-thumb {
    background-color: #cbd5e1;
    border-radius: 10px;
}

</style>
 """)
