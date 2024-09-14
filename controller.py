from model import KaraokeModel
from view import KaraokeView

class KaraokeController:
    def __init__(self):
        self.model = KaraokeModel()
        self.view = KaraokeView()

    def run(self):
        song_name, song_duration, singers = self.view.get_song_details()
        num_singers = len(singers)
        previous_singers = self.model.get_previous_singers()

        score = self.model.calculate_score(num_singers, song_duration, singers, previous_singers)
        self.model.add_song(song_name, song_duration, singers, score)
        
        self.view.display_score(score)
        self.view.display_success_message(song_name, score)
