#!/usr/bin/env python3
from business import Investment
import tkinter as tk
from tkinter import ttk
import locale

class FutureValueFrame(ttk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, padding="10 10 10 10", relief=tk.RIDGE, borderwidth=2)
        self.investment = Investment()
        self.title = title

        # Locale setup
        result = locale.setlocale(locale.LC_ALL, '')
        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')

        # Variables
        self.monthlyInvestment = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        ttk.Label(self, text=self.title, font=("Arial", 12, "bold")).grid(
            column=0, row=0, columnspan=2, pady=5)

        ttk.Label(self, text="Monthly Investment:").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(self, width=20, textvariable=self.monthlyInvestment).grid(column=1, row=1)

        ttk.Label(self, text="Yearly Interest Rate:").grid(column=0, row=2, sticky=tk.W)
        ttk.Entry(self, width=20, textvariable=self.yearlyInterestRate).grid(column=1, row=2)

        ttk.Label(self, text="Years:").grid(column=0, row=3, sticky=tk.W)
        ttk.Entry(self, width=20, textvariable=self.years).grid(column=1, row=3)

        ttk.Label(self, text="Future Value:").grid(column=0, row=4, sticky=tk.W)
        ttk.Entry(self, width=20, textvariable=self.futureValue, state="readonly").grid(column=1, row=4)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def makeButtons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=5, columnspan=2, pady=10)

        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=1, row=0, padx=5)

    def calculate(self):
        try:
            monthly = float(self.monthlyInvestment.get().replace(",", "").strip())
            rate = float(self.yearlyInterestRate.get().replace(",", "").strip())
            years = float(self.years.get().replace(",", "").strip())

            # Safely cast years to int
            years = int(years)

            self.investment.monthlyInvestment = monthly
            self.investment.yearlyInterestRate = rate
            self.investment.years = years

            result = self.investment.calculateFutureValue()
            self.futureValue.set(f"${result:,.2f}")
        except Exception as e:
            self.futureValue.set("Invalid input")
            print("DEBUG ERROR:", e)

    def clear(self):
        self.monthlyInvestment.set("")
        self.yearlyInterestRate.set("")
        self.years.set("")
        self.futureValue.set("")

class FutureValueApp:
    def __init__(self, root):
        root.title("Future Value Calculator")
        root.geometry("700x400")
        root.configure(bg="#333333")

        self.left = FutureValueFrame(root, "Calculator 1")
        self.left.place(x=20, y=20, width=320, height=250)

        self.right = FutureValueFrame(root, "Calculator 2")
        self.right.place(x=360, y=20, width=320, height=250)

        self.makeBottomPanel(root)

    def makeBottomPanel(self, root):
        bottom = tk.Frame(root, bg="#333333")
        bottom.place(x=400, y=300, width=200, height=50)

        ttk.Button(bottom, text="Clear All", command=self.clearAll).pack(side="left", padx=10)
        ttk.Button(bottom, text="Exit", command=root.destroy).pack(side="left", padx=10)

        tk.Label(root, text="Future Value Calculator is running",
                 font=("Arial", 10), fg="#00FF00", bg="#333333").place(x=20, y=300)

    def clearAll(self):
        self.left.clear()
        self.right.clear()

if __name__ == "__main__":
    print("Starting the Future Value Calculator...")
    root = tk.Tk()
    app = FutureValueApp(root)
    root.mainloop()
    print("Application closed.")
