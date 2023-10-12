from tkinter import *
from tkinter import messagebox
from tkinter import ttk
result = 0
# ================  Screen   =======================
main_screen = Tk()
main_screen.title("Nicho's calculator")
main_screen.config(padx=50, pady=50)

# ================ Functions =======================
def dropdown_select():
    selected_option = selected_operation.get()
    return selected_option

def calculate():
    selected = dropdown_select()
    global result
    num1_text = num1_box.get()
    num2_text = num2_box.get()

    if not num1_text or not num2_text:
        result_box.config(state="normal")  # Make the result Entry writable
        result_box.delete(0, END)  # Clear any previous result
        result_box.insert(0, "Please enter valid numbers")
        return

    num1 = float(num1_text)
    num2 = float(num2_text)
    if selected == "sum":
        result = num1 + num2
    elif selected == "sub":
        result = num1 - num2
    elif selected == "mul":
        result = num1 * num2
    elif selected == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "No divisions by zero"
    elif selected == "power":
        result = num1 ** num2
    result_box.config(state="normal")  # Make the result Entry writable
    result_box.delete(0, END)  # Clear any previous result
    result_box.insert(0, result)
    result_box.config(state="readonly")

# ================   Stuff   =======================
operations = ["sum", "sub", "mul", "div", "power"]
selected_operation = StringVar()
dropdown = ttk.Combobox(main_screen, textvariable=selected_operation,
                        values=operations, state="readonly")
dropdown.set("sum")
dropdown.bind("<<ComboboxSelected>>", dropdown_select)
dropdown.grid(column=2, row=3)

# ===============  Rest      =======================
canvas = Canvas(width=500, height=300, highlightthickness=0)
crazy = PhotoImage(file="../calculator_nicho/crazy.png")
canvas.create_image(110, 112, image=crazy)
canvas.grid(column=0, row=0)

# LABELS #
num1_label = Label(text="Number 1", width=20)
num1_label.grid(column=0, row=1)

num2_label = Label(text="Number 2", width=20)
num2_label.grid(column=0, row=2)

select_label = Label(text="Select operator", width=20)
select_label.grid(column=2, row=2)

result_label = Label(text="Result", width=20)
result_label.grid(column=2, row=2)
# ENTRIES #
num1_box = Entry(width=35)
num1_box.grid(column=1, row=1)
num1_box.focus()

num2_box = Entry(width=35)
num2_box.grid(column=1, row=2)

result_box = Entry(width=35)
result_box.config(state="readonly")
result_box.grid(column=2, row=4)
# BUTTON #
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=5)

main_screen.mainloop()
