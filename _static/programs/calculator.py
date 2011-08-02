from Tkinter import *

w = Tk()
buttons_frame = Frame(w)

# Use three models:
# one to save the operation (+, -, * or /),
# another to save the previous value, and
# another to save the current value
v_operation = StringVar()
v_operation.set('+')
v_previous = StringVar()
v_previous.set('0')
v_actual = StringVar()
v_actual.set('')

visor = Entry(w, textvariable=v_actual, fg='green', bg='black', width=10,
                 font=('Courier', 20, 'bold'), justify='right')

def agregator_create(i):
    def a():
        x = v_actual.get()
        y = x + str(i)
        v_actual.set(y)
    return a

def operator_create(op):
    def o():
        v_operation.set(op)
        v_previous.set(v_actual.get())
        v_actual.set('')
    return o

# Missing implementation!.
def calculate():
    pass

# Create buttons with digits and the point.
for pos, d in enumerate('7894561230.'):
    b = Button(buttons_frame, text=d, width=2, command=agregator_create(d))
    b.grid(row=pos / 3, column=pos % 3)

# Create operator buttons.
for pos, op in enumerate('/*-+'):
    b = Button(buttons_frame, text=op, width=2, command=operator_create(op))
    b.grid(row=pos, column=3)

# Create "=" button.
b = Button(buttons_frame, text='=', width=2, command=calculate)
b.grid(row=3, column=2)

visor.pack()
buttons_frame.pack()

w.title('Calculator')
w.mainloop()

