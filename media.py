import webbrowser

class Movie():
        def __init__(self, set_title, set_storyline_text, set_poster_image, set_trailer_video):
            self.title = set_title
            self.storyline_text = set_storyline_text
            self.poster_image_url = set_poster_image
            self.trailer_video_url = set_trailer_video
        def play_trailer(self):
            webbrowser.open(self.trailer_video_url)
