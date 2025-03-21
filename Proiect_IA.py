import tkinter as tk
from tkinter.ttk import Label

class FeedbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Feedback Utilizatori")
        self.root.geometry("800x800")

        self.votes = {
            "foarte_slab": 0,
            "slab": 0,
            "neutru": 0,
            "satisfacut": 0,
            "foarte_satisfacut": 0,
            "excelent": 0
        }

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.voting_frame = tk.Frame(self.main_frame)
        self.voting_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.label_foarte_slab = tk.Label(self.voting_frame, text="Foarte Slab", font=("Arial", 18))
        self.label_foarte_slab.pack(pady=5)

        self.button_foarte_slab = tk.Button(self.voting_frame, text="Votează", command=self.vote_foarte_slab, width=40, height=2, bg="#FF3333", fg="white")
        self.button_foarte_slab.pack(pady=5)

        self.label_slab = tk.Label(self.voting_frame, text="Slab", font=("Arial", 18))
        self.label_slab.pack(pady=5)
        
        self.button_slab = tk.Button(self.voting_frame, text="Votează", command=self.vote_slab, width=40, height=2, bg="#FF6666", fg="white")
        self.button_slab.pack(pady=5)
        self.label_neutru = tk.Label(self.voting_frame, text="Neutru", font=("Arial", 18))
        self.label_neutru.pack(pady=5)
        self.button_neutru = tk.Button(self.voting_frame, text="Votează", command=self.vote_neutru, width=40, height=2, bg="#CCCCCC", fg="black")
        self.button_neutru.pack(pady=5)
        self.label_satisfacut = tk.Label(self.voting_frame, text="Satisfăcut", font=("Arial", 18))
        self.label_satisfacut.pack(pady=5)
        self.button_satisfacut = tk.Button(self.voting_frame, text="Votează", command=self.vote_satisfacut, width=40, height=2, bg="#FFD700", fg="black")
        self.button_satisfacut.pack(pady=5)
        self.label_foarte_satisfacut = tk.Label(self.voting_frame, text="Foarte Satisfăcut", font=("Arial", 18))
        self.label_foarte_satisfacut.pack(pady=5)
        self.button_foarte_satisfacut = tk.Button(self.voting_frame, text="Votează", command=self.vote_foarte_satisfacut, width=40, height=2, bg="#66CC66", fg="white")
        self.button_foarte_satisfacut.pack(pady=5)
        self.label_excelent = tk.Label(self.voting_frame, text="Excelent", font=("Arial", 18))
        self.label_excelent.pack(pady=5)

        self.button_excelent = tk.Button(self.voting_frame, text="Votează", command=self.vote_excelent, width=40, height=2, bg="#66B2FF", fg="white")
        self.button_excelent.pack(pady=5)

        self.results_frame = tk.Frame(self.main_frame)
        self.results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.result_label = tk.Label(self.results_frame, text="Rezultatele voturilor", font=("Arial", 18, "bold"))
        self.result_label.pack(pady=20)

        self.result_text = tk.Label(self.results_frame, text=self.format_votes(), font=("Arial", 14))
        self.result_text.pack(pady=5)

        self.average_label = tk.Label(self.results_frame, text="Evaluare medie: Stele:", font=("Arial", 18, "bold"))
        self.average_label.pack(pady=10)

        self.stars_frame = tk.Frame(self.results_frame)
        self.stars_frame.pack(pady=5)

        self.stars = []
        for i in range(5):
            star = tk.Label(self.stars_frame, text="☆", font=("Arial", 24), fg="#FFD700")
            star.pack(side=tk.LEFT, padx=5)
            self.stars.append(star)
        self.comments_label = tk.Label(self.results_frame, text="Secțiunea de Comentarii", font=("Arial", 18, "bold"))
        self.comments_label.pack(pady=20)

        self.comment_box = tk.Text(self.results_frame, width=40, height=10, font=("Arial", 12))
        self.comment_box.pack(pady=10)

        self.add_comment_button = tk.Button(self.results_frame, text="Adaugă Comentariu", command=self.add_comment, width=30, height=2, bg="#87CEEB", fg="white")
        self.add_comment_button.pack(pady=10)
        self.comments_display = tk.Text(self.results_frame, width=40, height=10, font=("Arial", 12), state=tk.DISABLED)
        self.comments_display.pack(pady=10)

    def format_votes(self):
        return (f"Foarte Slab: {self.votes['foarte_slab']} | Slab: {self.votes['slab']} | Neutru: {self.votes['neutru']} | "
                f"Satisfăcut: {self.votes['satisfacut']} | Foarte Satisfăcut: {self.votes['foarte_satisfacut']} | Excelent: {self.votes['excelent']}")
    def calculate_average(self):
        total_votes = sum(self.votes.values())
        if total_votes == 0:
            return 0
        weighted_sum = (self.votes['foarte_slab'] * 0.5 +
                        self.votes['slab'] * 1 +
                        self.votes['neutru'] * 3 +
                        self.votes['satisfacut'] * 4 +
                        self.votes['foarte_satisfacut'] * 4.5 +
                        self.votes['excelent'] * 5)
        average = weighted_sum / total_votes
        return round(average, 1)

    def update_average_label(self):
        average = self.calculate_average()
        stars_count = int(round(average))
        self.average_label.config(text=f"Evaluare medie: Stele: {average}")

        for i in range(5):
            if i < stars_count:
                self.stars[i].config(text="★")
            else:
                self.stars[i].config(text="☆")

    def update_results(self):
        self.result_text.config(text=self.format_votes())
        self.update_average_label()

    def add_comment(self):
        comment = self.comment_box.get("1.0", tk.END).strip()
        if comment:
            self.comments_display.config(state=tk.NORMAL)
            self.comments_display.insert(tk.END, f"{comment}\n")
            self.comments_display.config(state=tk.DISABLED)
            self.comment_box.delete("1.0", tk.END)

    def vote_foarte_slab(self):
        self.votes["foarte_slab"] += 1
        self.update_results()

    def vote_slab(self):
        self.votes["slab"] += 1
        self.update_results()

    def vote_neutru(self):
        self.votes["neutru"] += 1
        self.update_results()
    def vote_satisfacut(self):
        self.votes["satisfacut"] += 1
        self.update_results()
    def vote_foarte_satisfacut(self):
        self.votes["foarte_satisfacut"] += 1
        self.update_results()
    def vote_excelent(self):
        self.votes["excelent"] += 1
        self.update_results()
if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()
