import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=30, pady=30)

lable1 = tkinter.Label(text="Enter your height (kg)")
lable1.pack()

entry1 = tkinter.Entry()
entry1.pack()

lable2 = tkinter.Label(text="Enter your weight (cm)")
lable2.pack()

entry2 = tkinter.Entry()
entry2.pack()

bmiLable = tkinter.Label()
bmiLable.pack()


def calculate():
    height = entry1.get()
    weight = entry2.get()

    if weight == "" or height == "":
        bmiLable.config(text="Enter both weight and height!")
    else:
        try:
            x = float(weight) / (float(height) / 100) ** 2
            result_string = description(x)
            bmiLable.config(text=result_string)

        except:
            bmiLable.config(text="Enter a valid number")


button1 = tkinter.Button(text="calculate", bg="black", command=calculate,foreground='white')

button1.pack()


def description(x):
    result_string = f"Your BMI is: {round(x,2)}. You are "
    if x <= 18.5:
        result_string += "underweight"
    elif 18.5 < x <= 24.9:
        result_string += "normal"
    elif 24.9 < x <= 29.9:
        result_string += "overweight "
    elif 29.9 <= x <= 34.9:
        result_string += "obese"
    else:
        result_string += "extremely obese"

    return result_string


tkinter.mainloop()
