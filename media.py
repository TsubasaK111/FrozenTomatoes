import webbrowser

"""
This class is designed to construct movie/song objects that will store related
information such as storyline, trailer/music video url, and poster image url.
"""


class Movie():
    """Constructs & plays movie objects with storyline, trailer, and poster."""
    def __init__(self, set_title, set_storyline_text,
                 set_poster_image, set_trailer_video):
        self.title = set_title
        self.storyline_text = set_storyline_text
        self.poster_image_url = set_poster_image
        self.trailer_video_url = set_trailer_video

    def play_trailer(self):
        webbrowser.open(self.trailer_video_url)


class Song():
    """Constructs & plays song objects with title, music video, and image."""
    def __init__(self, set_title, set_description_text,
                 set_song_image, set_song_url):
        self.title = set_title
        self.description_text = set_description_text
        self.image = set_song_image
        self.play_url = set_song_url

    def play_song(self):
        webbrowser.open(self.play_url)
