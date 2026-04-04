import tkinter as tk
from tkinter import messagebox
import numpy as np

# Import your backend
from main import run_tsqs   # we will modify main slightly


def solve_tsp():
    try:
        n = int(entry_n.get())

        matrix = []

        for i in range(n):
            row = list(map(int, entries[i].get().split()))
            matrix.append(row)

        matrix = np.array(matrix)

        route, cost = run_tsqs(matrix)

        result_label.config(
            text=f"Optimal Route: {route}\nMinimum Cost: {cost}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def generate_matrix_inputs():
    global entries

    for widget in frame_matrix.winfo_children():
        widget.destroy()

    n = int(entry_n.get())
    entries = []

    for i in range(n):
        entry = tk.Entry(frame_matrix, width=30)
        entry.insert(0, " ".join(["0"] * n))
        entry.grid(row=i, column=0, pady=2)
        entries.append(entry)


# GUI Window
root = tk.Tk()
root.title("TSQS TSP Solver")

tk.Label(root, text="Enter number of cities:").pack()

entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Generate Matrix Input", command=generate_matrix_inputs).pack()

frame_matrix = tk.Frame(root)
frame_matrix.pack()

tk.Button(root, text="Solve TSP", command=solve_tsp).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()