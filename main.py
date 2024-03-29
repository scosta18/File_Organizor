import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk

def organize_files():
    path = entry_path.get()

    if not os.path.exists(path):
        messagebox.showerror("Error", "Invalid path. Please enter a valid path.")
        return

    file_names = os.listdir(path)

    # Create necessary folders
    folder_names = ['pdf files', 'images files', 'text files', 'Audio files']
    for folder_name in folder_names:
        full_path = os.path.join(path, folder_name)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    # Organize files and count file types
    file_types = {
        'pdf files': ['.pdf', '.docx', '.txt', '.xlsx'],
        'images files': ['.png', '.jpg', '.jpeg'],
        'Audio files': ['.mp3']
    }
    
    file_counts = {folder: 0 for folder in folder_names}

    for file in file_names:
        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    destination = os.path.join(path, folder, file)
                    if not os.path.exists(destination):
                        shutil.move(os.path.join(path, file), destination)
                        file_counts[folder] += 1

    # Show a pop-up bar with file counts
    popup = tk.Toplevel(root)
    popup.title("File Counts")
    popup.geometry("300x100")
    
    for i, (folder, count) in enumerate(file_counts.items()):
        label = tk.Label(popup, text=f"{folder}: {count} files")
        label.pack(padx=10, pady=5)
        progress = Progressbar(popup, length=100, mode='determinate', maximum=len(file_names))
        progress.pack(padx=10, pady=5)
        progress["value"] = count
        popup.update_idletasks()
        
    messagebox.showinfo("Success", "Files organized successfully!")

# Create the main window
root = tk.Tk()
root.title("File Organizer")

# Set a background image
bg_image = Image.open("background_image.jpg")  # Replace with your image path
bg_image = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Create a 6x6 grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Frame for the existing file organizer interface
frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.grid(row=0, column=0, rowspan=6, columnspan=6, sticky='nsew')

# Adjust the frame size to fill the window
for i in range(6):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

# Label and Entry for the file path
label_path = tk.Label(frame, text="Enter the file path:")
label_path.grid(row=0, column=0, padx=10, pady=10)
entry_path = tk.Entry(frame)
entry_path.grid(row=0, column=1, padx=10, pady=10)

# Button to browse for a directory
def browse_directory():
    path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, path)

browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Button to organize files
organize_button = tk.Button(frame, text="Organize Files", command=organize_files)
organize_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
