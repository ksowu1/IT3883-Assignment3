# Program Name: Assignment3.py
# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Komi Sowu
# Assignment Number: Lab 3
# Due Date: 10/10/2026
# Purpose: This program creates a GUI application to convert Miles per Gallon into Kilometers per Liter. 
# The conversion updates automatically as the user types.
# Resources Used: Course notes and Python Tkinter documentation.

from tkinter import *


# Function to convert MPG to km/L
def convert(event=None):

    # Get mpg value from the user
    mpg_input = mpg_entry.get()

    try:
        # Convert the input to a number
        mpg = float(mpg_input)

        # Calculate kilometers per liter
        kml = mpg * 0.425143707

        # Display the result
        result_label.config(text=f"{kml:.4f}")

    except ValueError:
        # Clear the result if input is blank or invalid
        result_label.config(text="")


# The main window
root = Tk()
root.title("MPG to km/L Converter")
root.geometry("350x150")


# The MPG label
mpg_label = Label(root, text="Miles per Gallon (MPG):")
mpg_label.grid(row=0, column=0, padx=10, pady=20)


# The input box
mpg_entry = Entry(root)
mpg_entry.grid(row=0, column=1, padx=10, pady=20)


# The km/L label
kml_label = Label(root, text="Kilometers per Liter:")
kml_label.grid(row=1, column=0, padx=10, pady=10)


# The label that displays the answer
result_label = Label(root, text="")
result_label.grid(row=1, column=1, padx=10, pady=10)


# Run the convert function every time the user types
mpg_entry.bind("<KeyRelease>", convert)


# Start the GUI
root.mainloop()
