import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # Store the current expression
        self.expression = ""

        # Create a StringVar to update the display
        self.text_input = tk.StringVar()

        # Entry widget for displaying the expression/result
        self.entry = tk.Entry(master, textvariable=self.text_input, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Define calculator buttons and their layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, padx=20, pady=20, font=("Arial", 18),
                               command=lambda bt=button_text: self.on_button_click(bt))
            button.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.text_input.set("")
        elif char == "=":
            try:
                # Evaluate the expression and update display
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result  # allow further operations on the result
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.text_input.set("")
        else:
            # Append the pressed button's text to the expression
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
