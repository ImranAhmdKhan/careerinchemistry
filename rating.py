import tkinter as tk
from tkinter import ttk

career_data = {
    "Higher Studies (M.Sc, MBA)": {
        "salary": "₹25,000–₹80,000 (initial stipend/job)",
        "hours": "6–8 hrs (plus study time)",
        "stress": "Moderate"
    },
    "Competitive Exams (UPSC, NET, GATE)": {
        "salary": "₹50,000–₹1,20,000 (post selection)",
        "hours": "Varies (initial prep ~8–12 hrs/day)",
        "stress": "High"
    },
    "Research & Development (R&D)": {
        "salary": "₹35,000–₹1,00,000",
        "hours": "8–9 hrs/day",
        "stress": "Moderate to High"
    },
    "Industry Jobs (Pharma, Tech, etc.)": {
        "salary": "₹20,000–₹90,000",
        "hours": "8–10 hrs/day",
        "stress": "Moderate"
    },
    "Entrepreneurship (Start your own venture)": {
        "salary": "Variable (risk-reward based)",
        "hours": "10+ hrs/day",
        "stress": "High but exciting"
    },
    "Teaching & Academia": {
        "salary": "₹20,000–₹60,000",
        "hours": "6–8 hrs/day",
        "stress": "Low to Moderate"
    },
    "Science Communication (YouTube, Blogs, etc.)": {
        "salary": "₹10,000–₹1,00,000+ (freelance)",
        "hours": "Flexible",
        "stress": "Low to Moderate"
    }
}

criteria = {
    "Interest Level": "How excited are you about this field?",
    "Job Security": "How stable is the job long-term?",
    "Salary Potential": "Expected income and financial growth",
    "Growth Opportunity": "Chances for promotions and learning",
    "Work-Life Balance": "How balanced is work with personal life?"
}

rating_options = [1, 2, 3, 4, 5]

class CareerMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Career Path Explorer for B.Sc Graduates")
        self.entries = {}

        title = tk.Label(root, text="🎓 Explore Career Options with Confidence!", font=("Helvetica", 16, "bold"), fg="#1a73e8")
        title.pack(pady=10)

        subtitle = tk.Label(root, text="Rate each career path based on your preferences and learn what suits YOU best.", font=("Helvetica", 11))
        subtitle.pack(pady=5)

        canvas = tk.Canvas(root)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for path, info in career_data.items():
            frame = ttk.LabelFrame(self.scrollable_frame, text=f"🧭 {path}", padding=10)
            frame.pack(fill="x", padx=10, pady=8)
            self.entries[path] = {}

            # Add career detail summary
            info_text = (
                f"💸 Salary: {info['salary']}\n"
                f"🕒 Working Hours: {info['hours']}\n"
                f"😰 Stress Level: {info['stress']}"
            )
            tk.Label(frame, text=info_text, justify="left", font=("Helvetica", 9, "italic"), fg="#444").pack(anchor="w", padx=5, pady=5)

            # Rating criteria dropdowns
            for crit, hint in criteria.items():
                row = ttk.Frame(frame)
                row.pack(fill="x", pady=2)

                label = ttk.Label(row, text=f"{crit}:", width=22)
                label.pack(side="left")

                val = tk.IntVar()
                val.set(3)

                dropdown = ttk.OptionMenu(row, val, val.get(), *rating_options)
                dropdown.pack(side="left", padx=5)

                hint_label = tk.Label(row, text=f"💡 {hint}", font=("Helvetica", 8), fg="gray")
                hint_label.pack(side="left", padx=10)

                self.entries[path][crit] = val

        submit_btn = tk.Button(root, text="🎯 Show My Best Career Option", font=("Helvetica", 12, "bold"),
                               bg="#28a745", fg="white", command=self.calculate_scores)
        submit_btn.pack(pady=15)

    def calculate_scores(self):
        scores = {}
        for path in self.entries:
            total = sum(self.entries[path][crit].get() for crit in criteria)
            scores[path] = total

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        best_path = sorted_scores[0][0]

        result_window = tk.Toplevel(self.root)
        result_window.title("🌈 Your Personalized Career Advice")
        tk.Label(result_window, text="🔍 Career Match Scores", font=("Helvetica", 14, "bold"), fg="#ff6f00").pack(pady=10)

        for path, score in sorted_scores:
            tk.Label(result_window, text=f"{path}: {score}/25", font=("Helvetica", 11)).pack()

        detail = career_data[best_path]
        result_text = f"""
🌟 Your Best Match: {best_path}

💸 Avg. Salary: {detail['salary']}
🕒 Working Hours: {detail['hours']}
😰 Stress Level: {detail['stress']}
"""
        tk.Label(result_window, text=result_text.strip(), font=("Helvetica", 12, "bold"), fg="#2b9348", justify="left").pack(pady=15)

        tk.Label(result_window, text="💪 Choose based on passion, not pressure!", font=("Helvetica", 10, "italic"), fg="gray").pack(pady=5)


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = CareerMatrixApp(root)
    root.geometry("800x630")
    root.mainloop()
