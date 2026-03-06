import tkinter as tk
from datetime import date
import json
import os

FILE = "progress.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def mark_today():
    today = str(date.today())
    if today not in data:
        data.append(today)
        save_data(data)
        update_ui()

def update_ui():
    today = date.today()
    year_end = date(today.year, 12, 31)
    total_days = 365
    done = len(data)
    remaining = (year_end - today).days

    status_label.config(
        text=f"Days Completed: {done}\nDays Remaining: {remaining}"
    )

# UI
root = tk.Tk()
root.title("365 Day Exam Tracker")
root.geometry("350x220")

data = load_data()

tk.Label(root, text="📅 365 Day Consistency Tracker",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="✔ Mark Today Done",
          font=("Arial", 12),
          bg="green", fg="white",
          command=mark_today).pack(pady=10)

status_label = tk.Label(root, font=("Arial", 11))
status_label.pack(pady=10)

update_ui()
root.mainloop()
