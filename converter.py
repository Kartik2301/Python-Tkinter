from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=150)
window.config(padx=60, pady=30)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)
miles_input.grid(padx=10)
miles_input.insert(END, "0")

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def compute():
    value = miles_input.get()
    value = float(value)
    km_value = value * 1.60934
    km_result_label.config(text=f'{km_value}')

calculate_button = Button(text="Calculate", command=compute)
calculate_button.grid(row=2, column=1)















window.mainloop()