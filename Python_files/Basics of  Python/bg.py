import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Background Image Example")

# Load the image file
image = Image.open("awais.jpeg")
photo = ImageTk.PhotoImage(image)

# Create a label with the image
background_label = tk.Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

# Add other widgets to the window
# For example:
label = tk.Label(root, text="Hello, world!", bg="white")
label.pack()

# Run the main event loop
root.mainloop()
