# File: swot_analysis_interactive.py

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from collections import Counter
import plotly.graph_objects as go


class SWOTAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced SWOT Analysis Tool")
        self.root.geometry("900x800")

        # SWOT data with priority scores
        self.swot_data = {
            "Strengths": [],
            "Weaknesses": [],
            "Opportunities": [],
            "Threats": []
        }

        self.filtered_data = {}  # Store filtered data for dynamic filtering

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Advanced SWOT Analysis with Filtering & Interactive Visualizations", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tabs = {}
        for category in self.swot_data.keys():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=category)
            self.tabs[category] = frame
            self.create_tab_content(frame, category)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        save_button = tk.Button(button_frame, text="Save", command=self.save_data, width=15)
        save_button.grid(row=0, column=0, padx=5)

        export_csv_button = tk.Button(button_frame, text="Export to CSV", command=self.export_csv, width=15)
        export_csv_button.grid(row=0, column=1, padx=5)

        export_pdf_button = tk.Button(button_frame, text="Export to PDF", command=self.export_pdf, width=15)
        export_pdf_button.grid(row=0, column=2, padx=5)

        visualize_button = tk.Button(button_frame, text="Interactive Visualization", command=self.visualize_interactive, width=20)
        visualize_button.grid(row=0, column=3, padx=5)

    def create_tab_content(self, frame, category):
        entry_label = tk.Label(frame, text=f"Add {category[:-1] if category.endswith('s') else category}:")
        entry_label.pack(pady=5)

        self.entry_var = tk.StringVar()
        entry_field = tk.Entry(frame, textvariable=self.entry_var, width=50)
        entry_field.pack(pady=5)

        priority_label = tk.Label(frame, text="Priority (1 - Low, 5 - High):")
        priority_label.pack(pady=5)

        self.priority_var = tk.IntVar(value=1)
        priority_spinbox = tk.Spinbox(frame, from_=1, to=5, textvariable=self.priority_var, width=5)
        priority_spinbox.pack(pady=5)

        add_button = tk.Button(frame, text=f"Add to {category}", command=lambda c=category: self.add_item(c))
        add_button.pack(pady=5)

        listbox_frame = tk.Frame(frame)
        listbox_frame.pack(fill="both", expand=True, pady=10)

        self.listboxes = {}
        listbox = tk.Listbox(listbox_frame, selectmode="single", height=15, width=60)
        listbox.pack(side="left", fill="both", expand=True)
        self.listboxes[category] = listbox

        scrollbar = tk.Scrollbar(listbox_frame, command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.config(yscrollcommand=scrollbar.set)

        filter_frame = tk.Frame(frame)
        filter_frame.pack(pady=10)

        filter_label = tk.Label(filter_frame, text="Filter by Priority Range:")
        filter_label.pack(side="left", padx=5)

        self.min_priority_var = tk.IntVar(value=1)
        min_spinbox = tk.Spinbox(filter_frame, from_=1, to=5, textvariable=self.min_priority_var, width=5)
        min_spinbox.pack(side="left", padx=5)

        self.max_priority_var = tk.IntVar(value=5)
        max_spinbox = tk.Spinbox(filter_frame, from_=1, to=5, textvariable=self.max_priority_var, width=5)
        max_spinbox.pack(side="left", padx=5)

        filter_button = tk.Button(filter_frame, text="Apply Filter", command=lambda c=category: self.filter_items_by_range(c))
        filter_button.pack(side="left", padx=5)

        remove_filter_button = tk.Button(filter_frame, text="Clear Filter", command=lambda c=category: self.clear_filter(c))
        remove_filter_button.pack(side="left", padx=5)

    def add_item(self, category):
        item = self.entry_var.get().strip()
        priority = self.priority_var.get()

        if item:
            self.swot_data[category].append((item, priority))
            self.update_listbox(category)
            self.entry_var.set("")
            self.priority_var.set(1)
        else:
            messagebox.showwarning("Input Error", f"Please enter a valid {category[:-1] if category.endswith('s') else category}.")

    def update_listbox(self, category):
        listbox = self.listboxes[category]
        listbox.delete(0, tk.END)

        data = self.filtered_data.get(category, self.swot_data[category])
        for item, priority in data:
            listbox.insert(tk.END, f"{item} (Priority: {priority})")

    def filter_items_by_range(self, category):
        min_priority = self.min_priority_var.get()
        max_priority = self.max_priority_var.get()

        if min_priority > max_priority:
            messagebox.showwarning("Filter Error", "Minimum priority cannot be greater than maximum priority.")
            return

        self.filtered_data[category] = [
            (item, priority)
            for item, priority in self.swot_data[category]
            if min_priority <= priority <= max_priority
        ]
        self.update_listbox(category)

    def clear_filter(self, category):
        if category in self.filtered_data:
            del self.filtered_data[category]
        self.update_listbox(category)

    def save_data(self):
        try:
            with open("swot_data.json", "w") as file:
                json.dump(self.swot_data, file, indent=4)
            messagebox.showinfo("Success", "SWOT data saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

    def export_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Category", "Item", "Priority"])
                    for category, items in self.swot_data.items():
                        for item, priority in items:
                            writer.writerow([category, item, priority])
                messagebox.showinfo("Success", f"SWOT data exported to {file_path}.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export data: {e}")

    def export_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                                 filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if file_path:
            try:
                c = canvas.Canvas(file_path, pagesize=letter)
                c.setFont("Helvetica", 12)
                y = 750
                for category, items in self.swot_data.items():
                    c.drawString(50, y, f"{category}:")
                    y -= 20
                    for item, priority in items:
                        c.drawString(70, y, f"- {item} (Priority: {priority})")
                        y -= 20
                    y -= 10
                c.save()
                messagebox.showinfo("Success", f"SWOT data exported to {file_path}.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export data: {e}")

    def visualize_interactive(self):
        priorities = {category: [priority for _, priority in items] for category, items in self.swot_data.items()}

        for category, priority_list in priorities.items():
            counter = Counter(priority_list)
            labels, values = zip(*sorted(counter.items()))

            fig = go.Figure(data=[go.Bar(x=[f"Priority {i}" for i in labels], y=values)])
            fig.update_layout(title=f"{category} - Priority Distribution",
                              xaxis_title="Priority Levels",
                              yaxis_title="Number of Items")
            fig
