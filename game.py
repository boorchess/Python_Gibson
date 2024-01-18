from tkinter import *

def animate_square():
    current_color = square_colors.pop(0)
    canvas.itemconfig(square, fill=current_color)
    square_colors.append(current_color)
    window.after(500, animate_square)  # Adjust time for animation speed

window = Tk()
window.title('Animated Square')

canvas = Canvas(window, width=400, height=400)
canvas.pack()

# Create a square
square = canvas.create_rectangle(100, 100, 150, 150, fill='red')

# Define a list of colors for the animation
square_colors = ['red', 'green', 'blue', 'yellow', 'purple']

# Start the animation
animate_square()

window.mainloop()
