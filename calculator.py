from tkinter import *

def calculate():
    try:
        result = eval(entry.get())  # Evaluates the expression
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("Python Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button in buttons:
    def action(x=button):
        if x == "=":
            calculate()
        elif x == "C":
            entry.delete(0, END)
        else:
            entry.insert(END, x)
    Button(root, text=button, padx=20, pady=10, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()