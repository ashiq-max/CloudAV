import tkinter as tk
from tkinter import filedialog, messagebox
from check_hash import check_file
from pathlib import Path

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file to scan")
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def scan_file():
    file_path = entry_path.get().strip()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a file first.")
        return
    try:
        result = check_file(file_path)
        text_output.config(state="normal")
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"File: {result['path']}\n")
        text_output.insert(tk.END, f"SHA256: {result['sha256']}\n")
        if result["infected"]:
            text_output.insert(tk.END, "Status: INFECTED ⚠️\n", "infected")
        else:
            text_output.insert(tk.END, "Status: CLEAN ✅\n", "clean")
        text_output.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI ----------
root = tk.Tk()
root.title("CloudAV - Local Antivirus Scanner")
root.geometry("600x350")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

lbl_path = tk.Label(frame, text="File to Scan:")
lbl_path.pack(anchor="w")

entry_path = tk.Entry(frame, width=60)
entry_path.pack(side="left", padx=5, pady=5)

btn_browse = tk.Button(frame, text="Browse", command=browse_file)
btn_browse.pack(side="left", padx=5)

btn_scan = tk.Button(root, text="Scan Now", command=scan_file, bg="#4CAF50", fg="white", padx=10, pady=5)
btn_scan.pack(pady=10)

text_output = tk.Text(root, height=10, width=70, state="disabled", wrap="word")
text_output.pack(padx=10, pady=10)
text_output.tag_config("infected", foreground="red")
text_output.tag_config("clean", foreground="green")

root.mainloop()
