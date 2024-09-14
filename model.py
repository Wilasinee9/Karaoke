import json

class KaraokeModel:
    def __init__(self):
        self.songs_data = self.load_data()

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.songs_data, f, indent=4)

    def calculate_score(self, num_singers, song_duration, singer_names, previous_names):
        if num_singers == 1:
            previous_seconds = sum(song['duration'] for song in self.songs_data)
            score = previous_seconds % 100
        elif num_singers == 2:
            total_characters = sum(len(name) for name in singer_names)
            score = (song_duration * total_characters) % 100
        elif num_singers == 3:
            previous_chars = sum(len(name) for name in previous_names)
            current_chars = sum(len(name) for name in singer_names)
            score = (previous_chars * current_chars) % 100
        return score

    def add_song(self, song_name, song_duration, singers, score):
        new_entry = {
            "song_name": song_name,
            "duration": song_duration,
            "singers": singers,
            "score": score
        }
        self.songs_data.append(new_entry)
        self.save_data()

    def get_previous_singers(self):
        previous_singers = []
        for song in self.songs_data:
            previous_singers.extend(song['singers'])
        return previous_singers
