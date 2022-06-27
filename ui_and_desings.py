from tkinter import *

flag = 0
current_number = 0

window = Tk()
window.title("Calculator")
window.geometry("375x500")
window.configure(bg="black")

# Adding input field
entry = Entry(window, width=40, borderwidth=1, )
# aligning the input """

entry.grid(row=0, column=0, columnspan=3, padx=2, pady=2)


# Adding a function for button


def button_clicked(number):
    # entry.delete(0, END)
    e_numbers = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(e_numbers) + str(number))


def clear_button_pressed():
    entry.delete(0, END)


def add_button_button():
    first_number = entry.get()
    global current_number
    current_number = int(first_number)
    entry.delete(0, END)
    global flag
    flag = 1


def multiplication_button_pressed():
    m_number = entry.get()
    global current_number
    current_number = int(m_number)
    entry.delete(0, END)
    global flag
    flag = 2


def subtraction_button_pressed():
    sub_number = entry.get()
    global current_number
    current_number = int(sub_number)
    entry.delete(0, END)
    global flag
    flag = 3


def division_button_pressed():
    div_number = entry.get()
    global current_number
    current_number = int(div_number)
    entry.delete(0, END)
    global flag
    flag = 4


def equal_button_pressed():
    if flag == 1:
        second_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_number + int(second_number))

    elif flag == 2:
        mul_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_number * int(mul_number))

    elif flag == 3:
        subtract_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_number - int(subtract_number))

    elif flag==4:
        division_number=entry.get()
        entry.delete(0,END)
        entry.insert(0,current_number / int(division_number))


# defining buttons

button_1 = Button(window, text="1", padx=40.5, pady=20, command=lambda: button_clicked(1))
button_2 = Button(window, text="2", padx=40.5, pady=20, command=lambda: button_clicked(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_clicked(3))

button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_clicked(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_clicked(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_clicked(6))

button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_clicked(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_clicked(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_clicked(9))

button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_clicked(0))

# defining  additional button

button_add = Button(window, text="+", padx=40.5, pady=20, command=add_button_button)
button_subtraction = Button(window, text="-", padx=40, pady=20, command=subtraction_button_pressed)
button_equal = Button(window, text="=", padx=105, pady=20, command=equal_button_pressed)
button_multiplication = Button(window, text="*", padx=40.5, pady=20, command=multiplication_button_pressed)
button_division = Button(window, text="/", padx=40, pady=20, command=division_button_pressed)
button_clear = Button(window, text="clear", padx=95, pady=20, command=multiplication_button_pressed)

# putting the button on the screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

# adding additional buttons to the screen

button_add.grid(row=4, column=1)
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=2)
button_multiplication.grid(row=4, column=2)
button_subtraction.grid(row=5, column=0)
button_division.grid(row=6, column=0)

window.mainloop()
