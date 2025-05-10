import tkinter as tk
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error or digit_error or uppercase_error or lowercase_error or symbol_error:
        if len(password) < 6:
            return "Weak"
        else:
            return "Medium"
    else:
        return "Strong"

def display_strength():
    password = entry.get()
    strength = check_password_strength(password)

    # Update the strength label in the GUI
    strength_label.config(text=f"Strength: {strength}")

    # Change the label color based on strength
    if strength == "Weak":
        strength_label.config(fg="red")
    elif strength == "Medium":
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=display_strength)
check_button.pack(pady=20)

# Label to display strength
strength_label = tk.Label(root, text="", font=("Arial", 14))
strength_label.pack(pady=10)

root.mainloop()
