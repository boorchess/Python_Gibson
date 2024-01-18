from tkinter import *

def convert():
    # Check if the input is not empty and is a number
    if inch_data.get().isdigit():
        cm_string = str(float(inch_data.get()) * 2.54)  # Convert to float for decimal inch values
        cm_display.configure(text=cm_string)
    else:
        cm_display.configure(text="Invalid input")  # Display error for invalid input

# Create the main window
window = Tk()
window.title('Inch to Centimeter Converter')

# Create an Entry widget for inches input
inch_data = Entry(window)
inch_data.pack()

# Create a Label widget to display the result
cm_display = Label(window, text='')
cm_display.pack()

# Create a Button to trigger the conversion
button = Button(window, text='Convert to centimeter(s)', command=convert)
button.pack()

# Run the application
window.mainloop()
