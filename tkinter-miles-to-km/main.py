from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.minsize()
window.config(padx=15, pady=15)

def calculate():
  miles = float(miles_input.get())
  km = miles * 1.60934
  km_output_label["text"] = f"{km}"


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

km_output_label = Label(text='0', width=10)
km_output_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

calc_button = Button(text='Calculate', command=calculate)
calc_button.grid(column=1, row=2)






window.mainloop()

