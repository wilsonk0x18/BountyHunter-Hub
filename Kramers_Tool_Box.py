import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import webbrowser

def run_script(script_path):
    try:
        subprocess.Popen(["cmd", "/c", "python", script_path], shell=True)
        messagebox.showinfo("Success", "Script has been launched successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the script: {e}")

def switch_tab(tab_index):
    for frame in frames.values():
        frame.pack_forget()
    frames[tab_index].pack(fill="both", expand=True)

def search_query(query):
    website_url = website_entry.get()
    if website_url:
        search_url = f"https://www.google.com/search?q={query.format(website_url)}"
        webbrowser.open_new(search_url)
    else:
        messagebox.showwarning("Warning", "Please enter a website URL.")

# Helper function to create buttons for different search types
def create_search_button(frame, text, query):
    return tk.Button(frame, text=text, command=lambda: search_query(query), bg='#009688', fg='white', padx=10, pady=5)

# UI Setup
root = tk.Tk()
root.title("Script Runner")
root.geometry('600x400')  # Set a default size

# Styling
style = {
    'font': ('Helvetica', 12),
    'bg': '#424242',
    'fg': '#FFFFFF'
}

# Create tabs
tabs = ["Web Security", "OSINT", "File Creators", "Google Dorking Auto Run"]
frames = {}
for tab_name in tabs:
    frame = tk.Frame(root, bg=style['bg'])
    frames[tab_name] = frame

# Menu bar for tabs
menu = tk.Menu(root, bg=style['bg'], fg=style['fg'], font=style['font'])
root.config(menu=menu)
for tab_name in tabs:
    menu.add_command(label=tab_name, command=lambda tab_name=tab_name: switch_tab(tab_name))

# Define script paths
script_paths = [
    r"C:\Kramers_Toolbox\KramersEnumerator.py",
    r"C:\Kramers_Toolbox\KramersIDORBrute.py",
    r"C:\Kramers_Toolbox\KramersKrawler.py",
    r"C:\Kramers_Toolbox\KramersPasswordKollaboration.py",
]

# Adding buttons to Web Security tab
tk.Button(frames["Web Security"], text="Run Web Enumerator", command=lambda: run_script(script_paths[0]), **style).pack(pady=5)
tk.Button(frames["Web Security"], text="Run IDORBrute", command=lambda: run_script(script_paths[1]), **style).pack(pady=5)
tk.Button(frames["OSINT"], text="Find Social Medias", command=lambda: run_script(script_paths[2]), **style).pack(pady=5)
tk.Button(frames["File Creators"], text="Create Password List", command=lambda: run_script(script_paths[3]), **style).pack(pady=5)

# Entry field for custom website URL
website_label = tk.Label(frames["Google Dorking Auto Run"], text="Enter Website URL:", **style)
website_label.pack(pady=10)

website_entry = tk.Entry(frames["Google Dorking Auto Run"], width=50)
website_entry.pack(pady=10)

# Adding search buttons to Google Dorking Auto Run tab
searches = {
    "PDF Scan": "site:{} filetype:pdf",
    "Admin Pages": "site:{} inurl:/admin OR inurl:/dashboard",
    "Log Files": "filetype:log site:{}",
    "SQL Database": "filetype:sql site:{}",
    "Third Party Software": "\"Powered by {}\"",
    "Directory Listings": "intitle:\"index of\" site:{}",
    "Password Pages": "site:{} \"Password\"",
    "Sensitive Pages": "site:{} intitle:\"confidential\" OR intitle:\"secret\" OR intitle:\"private\"",
    "Error Pages": "site:{} intext:\"error message\"",
    "Config Pages": "site:{} intitle:\"index of\" config",
    "Login Pages": "site:{} intitle:\"login\" OR intitle:\"signin\" OR intitle:\"sign in\"",
    "PHP Files": "site:{} intext:\"<?php\" OR intitle:\"index of\" php",
    "Connection Files": "site:{} intitle:\"index of\" dbconnect",
}

for text, query in searches.items():
    create_search_button(frames["Google Dorking Auto Run"], text, query).pack(pady=5, fill=tk.X)

# Set the initial tab
switch_tab("Web Security")
root.mainloop()
