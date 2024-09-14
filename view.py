class KaraokeView:
    @staticmethod
    def get_song_details():
        song_name = input("Enter song name: ")
        song_duration = int(input("Enter song duration (in seconds): "))
        num_singers = int(input("Enter number of singers (1-3): "))
        singers = [input(f"Enter singer {i+1} name: ") for i in range(num_singers)]
        return song_name, song_duration, singers

    @staticmethod
    def display_score(score):
        print(f"The karaoke score is: {score}")

    @staticmethod
    def display_success_message(song_name, score):
        print(f"Song '{song_name}' with score {score} has been recorded successfully!")
