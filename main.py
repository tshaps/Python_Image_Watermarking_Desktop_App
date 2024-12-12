""" Image Watermarking App
This app is for watermarking images
"""
# Importing required modules
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

# Global variable to store the currently selected file
current_image_path = None
current_pil_image = None


def displayimage():
    global current_image_path, current_pil_image

    # If no image has been selected yet, open the file dialog
    if not current_image_path:
        current_image_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=(
            ('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*')))

    # If the user cancels or no file is selected, do nothing
    if not current_image_path:
        return None

    # Open the image only if it's not already loaded
    if not current_pil_image:
        current_pil_image = Image.open(current_image_path)
        current_pil_image.thumbnail((600, 650))

    # Create a Tkinter-compatible image
    tk_img = ImageTk.PhotoImage(current_pil_image)

    # Display the image
    image_lbl = ttk.Label(root)
    image_lbl.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
    image_lbl.config(image=tk_img)
    image_lbl.image = tk_img  # Store reference to prevent garbage collection

    # Add buttons
    save_btn = ttk.Button(frame, text='Save Image', command=save_image)
    save_btn.grid(row=1, column=2, sticky='ew')
    wm_btn = ttk.Button(frame, text='Watermark', command=watermarkimage)
    wm_btn.grid(row=1, column=3, sticky='ew')

    # Return the PIL image
    return current_pil_image


def watermarkimage():
    global current_pil_image

    if not current_pil_image:
        print("No image selected!")
        return

    # Create a drawable image object
    drawable = ImageDraw.Draw(current_pil_image)

    # Add text to the image
    text = "Tshaps"
    font_size = 20

    # Load a font (you can specify a TTF file or use a default one)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_position = (10, 10)  # Position for the watermark
    text_color = (255, 255, 255)  # White color

    # Add text to the image
    drawable.text(text_position, text, fill=text_color, font=font)

    # Update the displayed image
    tk_img = ImageTk.PhotoImage(current_pil_image)
    image_lbl = ttk.Label(root)
    image_lbl.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
    image_lbl.config(image=tk_img)
    image_lbl.image = tk_img  # Store reference to prevent garbage collection


def save_image():
    global current_pil_image

    if not current_pil_image:
        print("No image to save!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(
        ("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")))

    if save_path:
        current_pil_image.save(save_path)
        print(f"Image saved at {save_path}")


root = tk.Tk()
root.title('Image Watermarking')
root.geometry('600x650')
root.config(background='black')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

select_btn = ttk.Button(frame, text='Select Image', command=displayimage)
select_btn.grid(row=1, column=0, sticky='ew')

exit_btn = ttk.Button(frame, text='Exit', command=lambda: exit())
exit_btn.grid(row=1, column=1, sticky='ew')

root.mainloop()
