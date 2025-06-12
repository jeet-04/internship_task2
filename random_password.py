import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0!")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length!")
        return

    characters = ""
    
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_numbers.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type!")
        return
    
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Change button text after first generation
    generate_button.config(text="Generate Another Password")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Make window fullscreen
root.state('zoomed')  # For Windows (use root.attributes('-fullscreen', True) for Linux/Mac)

# Centering frame
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centering the frame

# Title Label
title_label = tk.Label(main_frame, text="Password Generator", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Length Input
length_frame = tk.Frame(main_frame)
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 14))
length_label.pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5, font=("Arial", 14))
length_entry.pack(side=tk.LEFT)
length_entry.insert(0, "12")  # Default length

# Character Type Selection
var_lower = tk.BooleanVar()
var_upper = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_special = tk.BooleanVar()

options_frame = tk.Frame(main_frame)
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=var_lower, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=var_upper, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=var_numbers, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Special (@#$%^&*)", variable=var_special, font=("Arial", 12)).pack(anchor="w")

# Generate Button
generate_button = tk.Button(main_frame, text="Generate Password", command=generate_password, font=("Arial", 14), bg="#4CAF50", fg="white")
generate_button.pack(pady=20)

# Password Display
password_entry = tk.Entry(main_frame, width=30, font=("Arial", 14), justify="center")
password_entry.pack(pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white")
copy_button.pack(pady=10)

# Run the GUI
root.mainloop()