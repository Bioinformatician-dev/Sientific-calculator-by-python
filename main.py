import tkinter as tk
from tkinter import ttk
import math

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:
            # Replace custom symbols with Python operators
            expression = current_text.replace("÷", "/").replace("×", "*").replace("√", "math.sqrt").replace("^", "**")
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": None, "math": math})

            # Check if the result is a whole number
            if result.is_integer():
                result = int(result)

            result_var.set(result)
        except SyntaxError:
            result_var.set("Syntax Error")
        except ZeroDivisionError:
            result_var.set("Division by Zero")
        except Exception:
            result_var.set("Error")
    elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text in ["sin", "cos", "tan"]:
        try:
            current_number = float(current_text)
            if clicked_button_text == "sin":
                result_var.set(math.sin(math.radians(current_number)))
            elif clicked_button_text == "cos":
                result_var.set(math.cos(math.radians(current_number)))
            elif clicked_button_text == "tan":
                result_var.set(math.tan(math.radians(current_number)))
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + clicked_button_text)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget to display the result
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font=("Helvetica", 24), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3),
    ("√", 6, 0), ("^", 6, 1), ("sin", 6, 2), ("cos", 6, 3), ("tan", 7, 2)  # Added trigonometric functions
]

# Configure style for theme
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Helvetica", 16), width=10, height=4)

# Create buttons and add them to the grid
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

# Configure row and column weights
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Set the window size
width = 500
height = 800
root.geometry(f"{width}x{height}")

# Make the window non-resizable
root.resizable(False, False)

# Keyboard control
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))

# Run the main loop
root.mainloop()






