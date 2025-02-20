import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog

class DirectDebit:
    def __init__(self, day, provider, is_recurring, end_date=None):
        self.day = day
        self.provider = provider
        self.is_recurring = is_recurring
        self.end_date = end_date if end_date else None

    def __str__(self):
        if self.is_recurring:
            if self.end_date:
                return f"{self.day}th - {self.provider} (Recurring until {self.end_date})"
            else:
                return f"{self.day}th - {self.provider} (Recurring)"
        else:
            return f"{self.day}th - {self.provider}"

def add_entry():
    try:
        day = int(day_entry.get())
        if not 1 <= day <= 31:
            raise ValueError("Invalid day. Please enter a day between 1 and 31.")
    except ValueError:
        messagebox.showerror("Error", "Invalid day. Please enter a valid day of the month.")
        return

    provider = provider_entry.get()
    if not provider:
        messagebox.showerror("Error", "Please enter the provider name.")
        return

    is_recurring = recurring_var.get()
    end_date = None
    if is_recurring:
        end_date = end_date_entry.get()
        try:
            if end_date:
                datetime.datetime.strptime(end_date, "%Y-%m-%d")  # Validate end date format
        except ValueError:
            messagebox.showerror("Error", "Invalid end date format. Please use YYYY-MM-DD.")
            return

    try:
        with open("direct_debits.txt", "a") as f:
            f.write(str(DirectDebit(day, provider, is_recurring, end_date)) + "\n")
        messagebox.showinfo("Success", "Entry added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while adding: {e}")

    clear_fields()

def view_entries():
    try:
        with open("direct_debits.txt", "r") as f:
            entries_text.delete('1.0', tk.END)
            entries_text.insert(tk.END, "Your direct debit entries:\n")
            for line in f:
                entries_text.insert(tk.END, line)
    except FileNotFoundError:
        entries_text.delete('1.0', tk.END)
        entries_text.insert(tk.END, "No entries found.")

def delete_entry():
    selected_line = entries_text.get("sel.first", "sel.last")
    if not selected_line:
        messagebox.showwarning("Warning", "Please select an entry to delete.")
        return

    try:
        with open("direct_debits.txt", "r") as f:
            lines = f.readlines()

        with open("direct_debits.txt", "w") as f:
            for line in lines:
                if line.strip() != selected_line.strip():  # Compare without newline character
                    f.write(line)

        view_entries()  # Update the display
        messagebox.showinfo("Success", "Entry deleted successfully.")

    except FileNotFoundError:
        messagebox.showwarning("Warning", "No entries found to delete.")

def edit_entry():
    selected_line = entries_text.get("sel.first", "sel.last")
    if not selected_line:
        messagebox.showwarning("Warning", "Please select an entry to edit.")
        return

    try:
        # Extract existing data
        parts = selected_line.strip().split(" - ")
        existing_day = int(parts[0].split("th")[0])
        existing_provider = parts[1]
        existing_recurring = "Recurring" in parts[1]
        existing_end_date = None
        if "Recurring until" in parts[1]:
            existing_end_date = parts[1].split("Recurring until ")[1]

        # Get updated values
        new_day = simpledialog.askinteger("Edit Day", "Enter new day:", initialvalue=existing_day)
        if new_day is None:
            return  # User canceled the dialog

        new_provider = simpledialog.askstring("Edit Provider", "Enter new provider:", initialvalue=existing_provider)
        if new_provider is None:
            return

        new_recurring = messagebox.askyesno("Edit Recurring", "Is it recurring?")

        new_end_date = None
        if new_recurring:
            new_end_date = simpledialog.askstring("Edit End Date", "Enter end date (YYYY-MM-DD):")

        # Update the file
        with open("direct_debits.txt", "r") as f:
            lines = f.readlines()

        with open("direct_debits.txt", "w") as f:
            for line in lines:
                if line.strip() == selected_line.strip():  # Compare without newline character
                    f.write(str(DirectDebit(new_day, new_provider, new_recurring, new_end_date)) + "\n")
                else:
                    f.write(line)

        view_entries()  # Update the display
        messagebox.showinfo("Success", "Entry edited successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while editing: {e}")

def clear_fields():
    day_entry.delete(0, tk.END)
    provider_entry.delete(0, tk.END)
    recurring_var.set(0)
    end_date_entry.delete(0, tk.END)
    end_date_entry.config(state=tk.DISABLED)

def toggle_end_date():
    if recurring_var.get():
        end_date_entry.config(state=tk.NORMAL)
    else:
        end_date_entry.config(state=tk.DISABLED)
        end_date_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Direct Debit Tracker")

# Create widgets
day_label = tk.Label(window, text="Day of the Month:")
day_label.grid(row=0, column=0)
day_entry = tk.Entry(window)
day_entry.grid(row=0, column=1)

provider_label = tk.Label(window, text="Provider:")
provider_label.grid(row=1, column=0)
provider_entry = tk.Entry(window)
provider_entry.grid(row=1, column=1)

recurring_var = tk.IntVar()
recurring_checkbox = ttk.Checkbutton(window, text="Recurring", variable=recurring_var, command=toggle_end_date)
recurring_checkbox.grid(row=2, columnspan=2)

end_date_label = tk.Label(window, text="End Date (YYYY-MM-DD):")
end_date_label.grid(row=3, column=0)
end_date_entry = tk.Entry(window, state=tk.DISABLED)
end_date_entry.grid(row=3, column=1)

add_button = tk.Button(window, text="Add Entry", command=add_entry)
add_button.grid(row=4, column=0)

view_button = tk.Button(window, text="View Entries", command=view_entries)
view_button.grid(row=4, column=1)

delete_button = tk.Button(window, text="Delete Entry", command=delete_entry)
delete_button.grid(row=5, column=0)

edit_button = tk.Button(window, text="Edit Entry", command=edit_entry)
edit_button.grid(row=5, column=1)

entries_text = tk.Text(window, height=10, width=40)
entries_text.grid(row=6, columnspan=2)

window.mainloop()