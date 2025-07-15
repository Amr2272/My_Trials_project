from tkinter import *  # Import all classes and functions from tkinter
from tkinter import messagebox  # Import messagebox for displaying alerts

# Create the main application window
frame = Tk()
frame.geometry("300x450")  # Set window size
frame.title("Calculatour")  # Set window title
frame.configure(bg="#1E1E1E")  # Set background color

# Add a title label to the window
L = Label(frame, text="Standard", font="Verdana 20 bold", bg="#1E1E1E", fg="silver")
L.place(x=10, y=0)  # Position the label

# Display label for showing current input/result
label = Label(frame, text="0", font="Verdana 20 bold", bg="#1E1E1E", fg="silver")
label.place(x=140, y=80)

# --- Calculator State Variables ---
L = []        # List to store input sequence
result = ""   # String to store current result
sq = ""       # Temporary string for square root calculation
exp = ""      # Temporary string for exponent calculation

# --- Button Press Handlers ---
def show(bt):
    """Handles button press, updates input list and display."""
    global L, result
    r = get(bt)         # Get the value for the button
    L.append(r)         # Add to input list
    result = "".join(L) # Update result string
    equation()          # Update display

def get(btn):
    """Returns the string value for a button."""
    if btn == btn_mul:
        return "*"
    if btn == btn_div:
        return "/"
    if btn == btn_pow2:
        return "²"
    if btn == btn_pm:
        return "--"
    return btn["text"]  # For number and other buttons

def clear():
    """Clears all input and resets display."""
    global L, result
    L = []
    label.config(text="0")

def dele():
    """Deletes last input character."""
    global L, result
    if len(L) != 0:
        L.pop()
    result = "".join(L)
    label.config(text=result)

def equal():
    """Evaluates the current input and displays the result."""
    global L, result, r, sq, exp
    try:
        if len(L) != 0:
            # Handle square root operations
            while "√(" in L:
                if ")" in L:
                    for i in range(L.index("√(") + 1, L.index(")")):
                        sq += L[i]
                    # Replace sqrt expression with its result
                    L[L.index("√("):L.index(")") + 1] = [str(eval(sq) ** 0.5)]
                else:
                    messagebox.showerror("Error", "Error syntax ')'")
                    clear()
                    break
                sq = ""
            result = round(eval("".join(L)), 6)
            label.config(text=result)
            # Handle negative sign operation
            while "--" in L:
                i = L.index("--")
                r = eval((L[i + 1])) * (-1)
                L.pop(i)
                L.pop(i)
                L.insert(i, str(r))
                result = round(eval("".join(L)), 6)
                label.config(text=result)
            # Handle square operation
            if "²" in L:
                i = L.index("²") - 1
                while i not in ["+", "-", "*", "/", "%"]:
                    exp = L[i] + exp
                    if i == 0:
                        break
                    i -= 1
                L[i:L.index("²") + 1] = [str((eval(exp)) ** 2)]
                result = round(eval("".join(L)), 6)
                exp = ""
                label.config(text=result)
            # Final evaluation
            result = round(eval("".join(L)), 6)
            label.config(text=result)
        else:
            result = "0"
    except ZeroDivisionError:
        messagebox.showerror("Error", "Not Allowed Dividie By Zero")
    except SyntaxError:
        pass

def equation():
    """Updates the display label with the current result."""
    label.config(text=result)

# --- Number Buttons ---
btn_1 = Button(frame, text="1", font="Verdana 10 bold", width=7, command=lambda: show(btn_1))
btn_1.place(x=10, y=350)

btn_2 = Button(frame, text="2", font="Verdana 10 bold", width=7, command=lambda: show(btn_2))
btn_2.place(x=80, y=350)

btn_3 = Button(frame, text="3", font="Verdana 10 bold", width=7, command=lambda: show(btn_3))
btn_3.place(x=150, y=350)

btn_4 = Button(frame, text="4", font="Verdana 10 bold", width=7, command=lambda: show(btn_4))
btn_4.place(x=10, y=300)

btn_5 = Button(frame, text="5", font="Verdana 10 bold", width=7, command=lambda: show(btn_5))
btn_5.place(x=80, y=300)

btn_6 = Button(frame, text="6", font="Verdana 10 bold", width=7, command=lambda: show(btn_6))
btn_6.place(x=150, y=300)

btn_7 = Button(frame, text="7", font="Verdana 10 bold", width=7, command=lambda: show(btn_7))
btn_7.place(x=10, y=250)

btn_8 = Button(frame, text="8", font="Verdana 10 bold", width=7, command=lambda: show(btn_8))
btn_8.place(x=80, y=250)

btn_9 = Button(frame, text="9", font="Verdana 10 bold", width=7, command=lambda: show(btn_9))
btn_9.place(x=150, y=250)

btn_0 = Button(frame, text="0", font="Verdana 10 bold", width=7, command=lambda: show(btn_0))
btn_0.place(x=80, y=400)

btn_dot = Button(frame, text=".", font="Verdana 10 bold", width=7, command=lambda: show(btn_dot))
btn_dot.place(x=150, y=400)

btn_pm = Button(frame, text="(+/-)", font="Verdana 10 bold", width=7, command=lambda: show(btn_pm))
btn_pm.place(x=10, y=400)

# --- Operator Buttons ---
btn_eq = Button(frame, text="=", font="Verdana 10 bold", width=7, bg="#039BE5", fg="white", command=lambda: equal())
btn_eq.place(x=220, y=400)

btn_add = Button(frame, text="+", font="Verdana 10 bold", width=7, command=lambda: show(btn_add))
btn_add.place(x=220, y=350)

btn_sub = Button(frame, text="-", font="Verdana 10 bold", width=7, command=lambda: show(btn_sub))
btn_sub.place(x=220, y=300)

btn_mul = Button(frame, text="x", font="Verdana 10 bold", width=7, command=lambda: show(btn_mul))
btn_mul.place(x=220, y=250)

btn_div = Button(frame, text="÷", font="Verdana 10 bold", width=7, command=lambda: show(btn_div))
btn_div.place(x=220, y=200)

# --- Function Buttons ---
btn_del = Button(frame, text="⌫", font="Verdana 10 bold", width=7, command=lambda: dele())
btn_del.place(x=220, y=150)

btn_clear = Button(frame, text="C", font="Verdana 10 bold", width=7, command=lambda: clear())
btn_clear.place(x=150, y=150)

btn_sqr = Button(frame, text="√(", font="Verdana 10 bold", width=7, command=lambda: show(btn_sqr))
btn_sqr.place(x=150, y=200)

btn_pow2 = Button(frame, text="x²", font="Verdana 10 bold", width=7, command=lambda: show(btn_pow2))
btn_pow2.place(x=80, y=200)

btn_percent = Button(frame, text="%", font="Verdana 10 bold", width=7, command=lambda: show(btn_percent))
btn_percent.place(x=10, y=200)

btn_per_right = Button(frame, text=")", font="Verdana 10 bold", width=7, command=lambda: show(btn_per_right))
btn_per_right.place(x=80, y=150)

btn_per_left = Button(frame, text="(", font="Verdana 10 bold", width=7, command=lambda: show(btn_per_left))
btn_per_left.place(x=10, y=150)

# Start the Tkinter event loop
frame.mainloop()