import tkinter as tk

def on_button_click(event):
    # Update the entry widget when a button is clicked
    entry.insert(tk.END, event.widget.cget("text"))

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for row_idx, row in enumerate(button_texts):
    for col_idx, text in enumerate(row):
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 20))
        button.grid(row=row_idx + 1, column=col_idx)
        button.bind("<Button-1>", on_button_click)

# Clear and evaluate buttons
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Helvetica", 20), command=clear_entry)
clear_button.grid(row=5, column=0)

eval_button = tk.Button(root, text="=", padx=20, pady=20, font=("Helvetica", 20), command=evaluate_expression)
eval_button.grid(row=5, column=1, columnspan=3)

root.mainloop()
