from tkinter import *

root = Tk()
root.title("Temperature Converter")

var1 = DoubleVar()
var2 = DoubleVar()

label = Label(root, text="Temperature Converter", font=("Arial", 20))
label.pack(side=TOP, pady=10)

# Celsius to Fahrenheit
label1 = Label(root, text="Celsius =", font=("Arial", 15))
label1.place(x=30, y=60)

entry1 = Entry(root, font=("Arial", 15), textvariable=var1)
entry1.place(x=180, y=60)

label2 = Label(root, text="Fahrenheit =", font=("Arial", 15))
label2.place(x=30, y=120)

label3 = Label(root, font=("Arial", 15))
label3.place(x=180, y=120)

def convert_c_to_f():
    fahrenheit = var1.get() * 1.8 + 32
    label3.config(text=f"{fahrenheit:.2f} °F")

button1 = Button(root, text="Convert", font=("Arial", 15), command=convert_c_to_f)
button1.place(x=350, y=60)

# Fahrenheit to Celsius
label4 = Label(root, text="Fahrenheit =", font=("Arial", 15))
label4.place(x=30, y=180)

entry2 = Entry(root, font=("Arial", 15), textvariable=var2)
entry2.place(x=180, y=180)

label5 = Label(root, text="Celsius =", font=("Arial", 15))
label5.place(x=30, y=240)

label6 = Label(root, font=("Arial", 15))
label6.place(x=180, y=240)

def convert_f_to_c():
    celsius = (var2.get() - 32) / 1.8
    label6.config(text=f"{celsius:.2f} °C")

button2 = Button(root, text="Convert", font=("Arial", 15), command=convert_f_to_c)
button2.place(x=350, y=180)

root.geometry("500x350")
root.mainloop()