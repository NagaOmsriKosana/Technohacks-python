import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def create_button(text, row, col, col_span=1, bg="#E6E6E6"):
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5, bg=bg)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, ipadx=20, ipady=20)
    button.bind("<Button-1>", on_click)
    return button

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")

# Create and style the heading label
heading_label = tk.Label(root, text="Calculator", font=("Helvetica", 24, "bold"), bg="#333333", fg="white")
heading_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

# Create and style the entry widget
entry = tk.Entry(root, font=("Helvetica", 30), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipadx=20, ipady=20)

# Define button labels and background colors
button_labels = [
    ('7', "#CCCCCC"), ('8', "#CCCCCC"), ('9', "#CCCCCC"), ('/', "#FF9900"),
    ('4', "#CCCCCC"), ('5', "#CCCCCC"), ('6', "#CCCCCC"), ('*', "#FF9900"),
    ('1', "#CCCCCC"), ('2', "#CCCCCC"), ('3', "#CCCCCC"), ('-', "#FF9900"),
    ('0', "#CCCCCC"), ('.', "#CCCCCC"), ('=', "#FF9900"), ('+', "#FF9900")
]

# Create and style buttons in a grid
row, col = 2, 0
for label, bg_color in button_labels:
    create_button(label, row, col, bg=bg_color)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button with a red background
create_button("C", row, col, col_span=2, bg="#FF3333")

root.mainloop()
