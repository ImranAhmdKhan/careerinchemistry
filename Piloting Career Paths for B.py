import tkinter as tk
from tkinter import ttk, messagebox

# Define career paths and criteria
career_paths = [
    "Higher Studies",
    "Competitive Exams",
    "Research & Development",
    "Industry Jobs",
    "Entrepreneurship",
    "Teaching & Academia",
    "Science Communication"
]

criteria = [
    "Interest Level",
    "Job Security",
    "Salary Potential",
    "Growth Opportunity",
    "Work-Life Balance"
]

# Initialize rating values (1 to 5)
rating_options = [1, 2, 3, 4, 5]

# Create the main application class
class CareerMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Career Decision Matrix for B.Sc Graduates")
        self.entries = {}

        heading = tk.Label(root, text="Rate Each Career Path (1 - Low, 5 - High)", font=("Arial", 14, "bold"))
        heading.pack(pady=10)

        canvas = tk.Canvas(root)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for path in career_paths:
            frame = ttk.LabelFrame(self.scrollable_frame, text=path)
            frame.pack(fill="x", padx=10, pady=5)

            self.entries[path] = {}
            for crit in criteria:
                label = ttk.Label(frame, text=crit, width=25)
                label.pack(side="left", padx=5)

                value = tk.IntVar()
                value.set(3)  # default value
                dropdown = ttk.OptionMenu(frame, value, value.get(), *rating_options)
                dropdown.pack(side="left", padx=5)

                self.entries[path][crit] = value

        submit_btn = ttk.Button(root, text="Calculate Scores", command=self.calculate_scores)
        submit_btn.pack(pady=10)

    def calculate_scores(self):
        scores = {}
        for path in self.entries:
            total = sum(self.entries[path][crit].get() for crit in criteria)
            scores[path] = total

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        result_window = tk.Toplevel(self.root)
        result_window.title("🎯 Career Decision Results")

        tk.Label(result_window, text="Career Path Scores", font=("Arial", 14, "bold")).pack(pady=10)

        for path, score in sorted_scores:
            tk.Label(result_window, text=f"{path}: {score}/25", font=("Arial", 12)).pack()

        best_path = sorted_scores[0][0]
        tk.Label(result_window, text=f"\n🏆 Best Match: {best_path}", font=("Arial", 14, "bold"), fg="green").pack(pady=10)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CareerMatrixApp(root)
    root.geometry("600x500")
    root.mainloop()
