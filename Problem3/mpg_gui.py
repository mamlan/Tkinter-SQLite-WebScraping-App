#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

class MyFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        self.distance_value = tk.StringVar()
        self.fuel_value = tk.StringVar()
        self.output_value = tk.StringVar()
        self.unit_mode = tk.StringVar(value="US(MPG)")

        self.build_layout()
        self.refresh_labels()

    def build_layout(self):
        ttk.Label(self, text="Mode:").grid(column=0, row=0, sticky=tk.E)
        selector = ttk.Combobox(self, textvariable=self.unit_mode, state="readonly", width=15,
                                values=["US(MPG)", "Metric(L/100km)"])
        selector.grid(column=1, row=0)
        selector.bind("<<ComboboxSelected>>", self.refresh_labels)

        self.dist_label = ttk.Label(self, text="")
        self.dist_label.grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, textvariable=self.distance_value, width=15).grid(column=1, row=1)

        self.fuel_label = ttk.Label(self, text="")
        self.fuel_label.grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, textvariable=self.fuel_value, width=15).grid(column=1, row=2)

        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, textvariable=self.output_value, width=15, state="readonly").grid(column=1, row=3)

        button_box = ttk.Frame(self)
        button_box.grid(column=0, row=4, columnspan=2, pady=10)

        ttk.Button(button_box, text="Calculate", command=self.run_calculation).grid(column=0, row=0, padx=5)
        ttk.Button(button_box, text="Clear", command=self.reset_fields).grid(column=1, row=0, padx=5)

        for item in self.winfo_children():
            item.grid_configure(padx=5, pady=3)

    def refresh_labels(self, event=None):
        if self.unit_mode.get() == "US(MPG)":
            self.dist_label.config(text="Miles Driven:")
            self.fuel_label.config(text="Gallons of Gas Used:")
            self.result_label.config(text="Miles Per Gallon:")
        else:
            self.dist_label.config(text="Kilometers Driven:")
            self.fuel_label.config(text="Liters of Fuel Used:")
            self.result_label.config(text="Liters Per 100 KM:")

    def run_calculation(self):
        try:
            d = float(self.distance_value.get())
            f = float(self.fuel_value.get())
            if d <= 0 or f <= 0:
                self.output_value.set("Invalid input")
                return

            if self.unit_mode.get() == "US(MPG)":
                result = d / f
                self.output_value.set(f"{result:.2f}")
            else:
                result = (f * 100) / d
                self.output_value.set(f"{result:.2f}")
        except:
            self.output_value.set("Invalid input")

    def reset_fields(self):
        self.distance_value.set("")
        self.fuel_value.set("")
        self.output_value.set("")
        self.unit_mode.set("US(MPG)")
        self.refresh_labels()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Fuel Efficiency Calculator")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    MyFrame(window)

    window.minsize(400, 250)
    window.update_idletasks()
    w = window.winfo_width()
    h = window.winfo_height()
    x_pos = (window.winfo_screenwidth() // 2) - (w // 2)
    y_pos = (window.winfo_screenheight() // 2) - (h // 2)
    window.geometry(f"{w}x{h}+{x_pos}+{y_pos}")

    window.mainloop()
