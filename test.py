import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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

    # Organize files
    file_types = {
        'pdf files': ['.pdf', '.docx', '.txt', '.xlsx'],
        'images files': ['.png', '.jpg', '.jpeg'],
        'Audio files': ['.mp3']
    }

    for file in file_names:
        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    destination = os.path.join(path, folder, file)
                    if not os.path.exists(destination):
                        shutil.move(os.path.join(path, file), destination)

    messagebox.showinfo("Success", "Files organized successfully!")

# Create the main window
root = tk.Tk()
root.title("File Organizer")


for i in range(10):
    root.grid_columnconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

fr = tk.Frame(root)
fr.grid(row=0, column=0, rowspan=6, columnspan=6, sticky='nsew')

for i in range(10):
    root.grid_columnconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Label and Entry for the file path
label_path = tk.Label(fr, text="Enter the file path:")
label_path.grid(row=0, column=0, padx=10, pady=10)
entry_path = tk.Entry(fr)
entry_path.grid(row=0, column=1, padx=10, pady=10)

# Button to browse for a directory
def browse_directory():
    path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, path)

browse_button = tk.Button(fr, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Button to organize files
organize_button = tk.Button(fr, text="Organize Files", command=organize_files)
organize_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
