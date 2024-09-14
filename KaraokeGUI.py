import tkinter as tk
from tkinter import ttk

class KaraokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Karaoke Score System")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")

        # Start with the welcome screen
        self.show_welcome_screen()

    def show_welcome_screen(self):
        # Welcome screen
        self.clear_screen()
        title_label = tk.Label(self.root, text="Welcome to Karaoke Scoring", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366")
        title_label.pack(pady=20)

        gui_button = tk.Button(self.root, text="Start", font=("Arial", 12, "bold"), command=self.show_song_info_input, bg="#4682B4", fg="#41596e", borderwidth=0, highlightthickness=0, relief="flat", padx=0, pady=3)
        gui_button.pack(pady=10)

    def show_song_info_input(self):
        # Song information input screen
        self.clear_screen()

        title_label = tk.Label(self.root, text="Enter Song Information", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366")
        title_label.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#f0f8ff")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Song Name:", font=("Arial", 12), bg="#f0f8ff", fg="#003366").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.song_name = tk.Entry(form_frame, font=("Arial", 12), bg="#e3dac5")
        self.song_name.grid(row=0, column=1, padx=10, pady=5)
        self.song_name.focus_set()

        tk.Label(form_frame, text="Song Duration (sec):", font=("Arial", 12), bg="#f0f8ff", fg="#003366").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.song_duration = tk.Entry(form_frame, font=("Arial", 12), bg="#e3dac5")
        self.song_duration.grid(row=1, column=1, padx=10, pady=5)

        next_button = tk.Button(self.root, text="Next", font=("Arial", 12, "bold"), command=self.show_singer_info_input, bg="#4682B4", fg="#41596e", borderwidth=0, highlightthickness=0, relief="flat", padx=0, pady=3)
        next_button.pack(pady=10)

    def show_singer_info_input(self):
        # Singer information input screen
        self.clear_screen()

        title_label = tk.Label(self.root, text="Enter Singer Information", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366")
        title_label.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#f0f8ff")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Number of Singers:", font=("Arial", 12), bg="#f0f8ff", fg="#003366").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.num_singers = ttk.Combobox(form_frame, values=[1, 2, 3], font=("Arial", 12), state="readonly")
        self.num_singers.grid(row=0, column=1, padx=10, pady=5)
        self.num_singers.current(0)
        self.num_singers.bind("<<ComboboxSelected>>", self.update_singer_entries)

        self.singers_frame = tk.Frame(form_frame, bg="#f0f8ff")
        self.singers_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.update_singer_entries()  # Call to display input fields

        next_button = tk.Button(self.root, text="Next", font=("Arial", 12, "bold"), command=self.show_score_display, bg="#4682B4", fg="#41596e", borderwidth=0, highlightthickness=0, relief="flat", padx=0, pady=3)
        next_button.pack(pady=10)

    def update_singer_entries(self, event=None):
        # Update singer input fields based on the number selected
        num_singers = int(self.num_singers.get())
        for widget in self.singers_frame.winfo_children():
            widget.destroy()

        self.singers_entries = []
        for i in range(num_singers):
            tk.Label(self.singers_frame, text=f"Singer {i+1}:", font=("Arial", 12), bg="#f0f8ff", fg="#003366").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            singer_entry = tk.Entry(self.singers_frame, font=("Arial", 12), bg="#e3dac5")
            singer_entry.grid(row=i, column=1, padx=10, pady=5)
            self.singers_entries.append(singer_entry)

    def show_score_display(self):
        # Display the score result
        self.clear_screen()

        title_label = tk.Label(self.root, text="Score Result", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366")
        title_label.pack(pady=10)

        try:
            song_name = self.song_name.get()
            song_duration = int(self.song_duration.get())
            num_singers = int(self.num_singers.get())
            singers = [self.singers_entries[i].get() for i in range(num_singers)]

            # Debug output
            print(f"Song Name: {song_name}")
            print(f"Song Duration: {song_duration}")
            print(f"Number of Singers: {num_singers}")
            print(f"Singers: {singers}")

            score = self.calculate_karaoke_score(song_duration, num_singers, singers)
            result_text = f"Score for '{song_name}': {score}"
        except ValueError as e:
            result_text = "Error: Please enter valid numbers in all fields."
            print(f"ValueError: {e}")
        except Exception as e:
            result_text = f"Error: {e}"
            print(f"Exception: {e}")

        result_label = tk.Label(self.root, text=result_text, font=("Arial", 14), bg="#f0f8ff", fg="#003366")
        result_label.pack(pady=10)

        finish_button = tk.Button(self.root, text="Finish", font=("Arial", 12, "bold"), command=self.show_welcome_screen, bg="#4682B4", fg="#41596e", borderwidth=0, highlightthickness=0, relief="flat", padx=0, pady=3)
        finish_button.pack(pady=10)

    def calculate_karaoke_score(self, song_duration, num_singers, singers):
        # Calculate the karaoke score based on the rules
        if num_singers == 1:
            score = song_duration % 100
        elif num_singers == 2:
            total_chars = sum(len(singer) for singer in singers)
            score = (song_duration * total_chars) % 100
        elif num_singers == 3:
            total_chars = sum(len(singer) for singer in singers)
            score = (total_chars * total_chars) % 100
        else:
            score = 0  # Default case for safety
        return score

    def clear_screen(self):
        # Clear all widgets from the root window
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KaraokeApp(root)
    root.mainloop()
