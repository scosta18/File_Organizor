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

# Label and Entry for the file path
label_path = tk.Label(root, text="Enter the file path:")
label_path.pack()
entry_path = tk.Entry(root)
entry_path.pack()

# Button to browse for a directory
def browse_directory():
    path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, path)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack()

# Button to organize files
organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.pack()

# Start the GUI main loop
root.mainloop()
