import tkinter as tk
from tkinter import messagebox
from model import KaraokeModel  # Import โมเดลเดียวกันที่ใช้ใน CLI

class KaraokeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Karaoke Score System")
        self.model = KaraokeModel()  # สร้างอ็อบเจกต์โมเดล

        # สร้าง Label และ Entry สำหรับกรอกข้อมูล
        tk.Label(root, text="Song Name:").grid(row=0, column=0)
        self.song_name = tk.Entry(root)
        self.song_name.grid(row=0, column=1)

        tk.Label(root, text="Song Duration (sec):").grid(row=1, column=0)
        self.song_duration = tk.Entry(root)
        self.song_duration.grid(row=1, column=1)

        tk.Label(root, text="Number of Singers (1-3):").grid(row=2, column=0)
        self.num_singers = tk.Entry(root)
        self.num_singers.grid(row=2, column=1)

        # กรอกชื่อคนร้อง
        self.singers_entries = []
        for i in range(3):
            tk.Label(root, text=f"Singer {i+1}:").grid(row=3+i, column=0)
            singer_entry = tk.Entry(root)
            singer_entry.grid(row=3+i, column=1)
            self.singers_entries.append(singer_entry)

        # ปุ่มคำนวณคะแนน
        self.calculate_button = tk.Button(root, text="Calculate Score", command=self.calculate_score)
        self.calculate_button.grid(row=6, columnspan=2)

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

            messagebox.showinfo("Score", f"Song '{song_name}' has a score of {score}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = KaraokeGUI(root)
    root.mainloop()
