from tkinter import *


window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# Label
label = Label(text="I am a label", font=("Aerial", 24, "bold"))
# label.pack(side="top")
# label.place(x=0,y=0)
label.grid(row=0, column=0)
label.config(padx=50, pady=50)

#Button
def button_clicked():
    data = input.get()
    label.config(text=data)
    print("I got clicked")

button = Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(row=1, column=1)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
#input.pack()
input.grid(row=2, column=3)
























window.mainloop()