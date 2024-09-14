import tkinter as tk
from tkinter import ttk, messagebox
from model import KaraokeModel  # Import the model used in CLI

class KaraokeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Karaoke Score System")
        self.root.geometry("600x400")
        self.root.configure(bg="#e3f2fd")  # Light Blue Background

        self.model = KaraokeModel()

        # Create Notebook for multiple pages
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Create pages
        self.create_welcome_page()
        self.create_song_info_page()
        self.create_singers_info_page()
        self.create_score_calculation_page()
        self.create_score_history_page()

        # Navigation Buttons
        self.nav_frame = tk.Frame(root, bg="#e3f2fd")
        self.nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.prev_button = tk.Button(self.nav_frame, text="Previous", command=self.go_previous, bg="#0d47a1", fg="#0d47a1", font=("Arial", 12))
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.nav_frame, text="Next", command=self.go_next, bg="#0d47a1", fg="#0d47a1", font=("Arial", 12))
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.current_page_index = 0
        self.update_navigation_buttons()

    def create_welcome_page(self):
        page = ttk.Frame(self.notebook, padding="10", style="TFrame")
        self.notebook.add(page, text="Welcome")

        page.configure(style="TFrame")

        # Welcome Message
        tk.Label(page, text="Welcome to the Karaoke Score System!", font=("Arial", 16), bg="#e3f2fd", fg="#0d47a1").pack(pady=20)
        tk.Label(page, text="This application helps you score your karaoke performance.", font=("Arial", 12), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)
        tk.Label(page, text="Navigate through the tabs to input song details, singers, calculate scores, and view history.", font=("Arial", 12), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

    def create_song_info_page(self):
        page = ttk.Frame(self.notebook, padding="10", style="TFrame")
        self.notebook.add(page, text="Song Information")

        page.configure(style="TFrame")

        # Song Information Widgets
        tk.Label(page, text="Song Name:", font=("Arial", 12), fg="#0d47a1").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.song_name = tk.Entry(page, font=("Arial", 12), bg="white", fg="#0d47a1")
        self.song_name.grid(row=0, column=1, pady=5)

        tk.Label(page, text="Song Duration (sec):", font=("Arial", 12), fg="#0d47a1").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.song_duration = tk.Entry(page, font=("Arial", 12), bg="white", fg="#0d47a1")
        self.song_duration.grid(row=1, column=1, pady=5)

    def create_singers_info_page(self):
        page = ttk.Frame(self.notebook, padding="10", style="TFrame")
        self.notebook.add(page, text="Singers Information")

        page.configure(style="TFrame")

        # Singers Information Widgets
        tk.Label(page, text="Number of Singers (1-3):", font=("Arial", 12), fg="#0d47a1").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_singers = tk.Entry(page, font=("Arial", 12), bg="white", fg="#0d47a1")
        self.num_singers.grid(row=0, column=1, pady=5)

        self.singers_entries = []
        for i in range(3):
            tk.Label(page, text=f"Singer {i+1}:", font=("Arial", 12), fg="#0d47a1").grid(row=1+i, column=0, sticky=tk.W, pady=5)
            singer_entry = tk.Entry(page, font=("Arial", 12), bg="white", fg="#0d47a1")
            singer_entry.grid(row=1+i, column=1, pady=5)
            self.singers_entries.append(singer_entry)

    def create_score_calculation_page(self):
        page = ttk.Frame(self.notebook, padding="10", style="TFrame")
        self.notebook.add(page, text="Score Calculation")

        page.configure(style="TFrame")

        # Calculate Button
        self.calculate_button = tk.Button(page, text="Calculate Score", command=self.calculate_score, bg="#0d47a1", fg="yellow", font=("Arial", 12))
        self.calculate_button.pack(pady=20)

        self.score_label = tk.Label(page, text="", font=("Arial", 12), bg="#e3f2fd", fg="#0d47a1")
        self.score_label.pack(pady=10)

    def create_score_history_page(self):
        page = ttk.Frame(self.notebook, padding="10", style="TFrame")
        self.notebook.add(page, text="Score History")

        page.configure(style="TFrame")

        # Score History Listbox
        self.score_history_listbox = tk.Listbox(page, font=("Arial", 12), width=50, height=10, bg="white", fg="#0d47a1")
        self.score_history_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def go_previous(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1
            self.notebook.select(self.current_page_index)
            self.update_navigation_buttons()

    def go_next(self):
        if self.current_page_index < self.notebook.index("end") - 1:
            self.current_page_index += 1
            self.notebook.select(self.current_page_index)
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        # Enable/Disable buttons based on current page
        self.prev_button.config(state=tk.NORMAL if self.current_page_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_page_index < self.notebook.index("end") - 1 else tk.DISABLED)

    def calculate_score(self):
        try:
            song_name = self.song_name.get()
            song_duration = int(self.song_duration.get())
            num_singers = int(self.num_singers.get())
            singers = [self.singers_entries[i].get() for i in range(num_singers)]

            if num_singers < 1 or num_singers > 3:
                raise ValueError("Number of singers must be between 1 and 3.")

            previous_singers = self.model.get_previous_singers()
            score = self.model.calculate_score(num_singers, song_duration, singers, previous_singers)

            self.model.add_song(song_name, song_duration, singers, score)

            self.score_label.config(text=f"Song '{song_name}' has a score of {score}.")
            self.score_history_listbox.insert(tk.END, f"{song_name} - Score: {score}")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TFrame", background="#e3f2fd")
    style.configure("TNotebook", background="#0d47a1")
    style.configure("TNotebook.Tab", background="#003c8f", foreground="yellow")
    app = KaraokeGUI(root)
    root.mainloop()
