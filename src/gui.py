
import tkinter as tk
from tkinter import messagebox
from core import FileHandler

class FileApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Handler")
        self.master.geometry("400x300")

        self.src_label = tk.Label(master, text="Source Path:")
        self.src_label.pack(pady=5)
        self.src_entry = tk.Entry(master, width=50)
        self.src_entry.pack(pady=5)

        self.dst_label = tk.Label(master, text="Destination Path:")
        self.dst_label.pack(pady=5)
        self.dst_entry = tk.Entry(master, width=50)
        self.dst_entry.pack(pady=5)

        self.copy_button = tk.Button(master, text="Copy File", command=self.copy_file)
        self.copy_button.pack(pady=5)

        self.move_button = tk.Button(master, text="Move File", command=self.move_file)
        self.move_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete File", command=self.delete_file)
        self.delete_button.pack(pady=5)

    def copy_file(self):
        src = self.src_entry.get()
        dst = self.dst_entry.get()
        result = FileHandler.copy_file(src, dst)
        messagebox.showinfo("Result", result)

    def move_file(self):
        src = self.src_entry.get()
        dst = self.dst_entry.get()
        result = FileHandler.move_file(src, dst)
        messagebox.showinfo("Result", result)

    def delete_file(self):
        filepath = self.src_entry.get()
        result = FileHandler.delete_file(filepath)
        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileApp(root)
    root.mainloop()
