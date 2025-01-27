import tkinter as tk
from tkinter import messagebox

def add_entry():
  date = date_entry.get()
  provider = provider_entry.get()

  if not date or not provider:
    messagebox.showerror("Error", "Please enter both date and provider.")
    return

  with open("direct_debits.txt", "a") as f:
    f.write(f"{date} - {provider}\n")
  messagebox.showinfo("Success", "Entry added successfully!")
  date_entry.delete(0, tk.END)
  provider_entry.delete(0, tk.END)

def view_entries():
  try:
    with open("direct_debits.txt", "r") as f:
      entries_text.delete('1.0', tk.END)  # Clear previous entries
      entries_text.insert(tk.END, "Your direct debit entries:\n")
      for line in f:
        entries_text.insert(tk.END, line)
  except FileNotFoundError:
    entries_text.delete('1.0', tk.END)  # Clear previous entries
    entries_text.insert(tk.END, "No entries found.")

# Create the main window
window = tk.Tk()
window.title("Direct Debit Tracker")

# Create widgets
date_label = tk.Label(window, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0)
date_entry = tk.Entry(window)
date_entry.grid(row=0, column=1)

provider_label = tk.Label(window, text="Provider:")
provider_label.grid(row=1, column=0)
provider_entry = tk.Entry(window)
provider_entry.grid(row=1, column=1)

add_button = tk.Button(window, text="Add Entry", command=add_entry)
add_button.grid(row=2, columnspan=2)

view_button = tk.Button(window, text="View Entries", command=view_entries)
view_button.grid(row=3, columnspan=2)

entries_text = tk.Text(window, height=10, width=40)
entries_text.grid(row=4, columnspan=2)

window.mainloop()