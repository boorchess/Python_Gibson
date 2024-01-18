from tkinter import *

# Function to update button text and style
def update_button():
    if button.config('text')[-1] == 'Hello World':
        button.config(text='Hi World', bg='yellow', fg='black')
    else:
        button.config(text='Hello World', bg='default', fg='default')

# Create the main window
window = Tk()
window.title('GUI')

# Create a button and add it to the window
button = Button(window, text='Hello World', command=update_button)
button.pack()

# Start the main loop
window.mainloop()
