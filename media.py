import webbrowser

class Movie():
    def __init__(self,movie_title,
                movie_storyline = None,
                poster_image = None,
                trailer_youtube = None ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        try:
            webbrowser.open(self.trailer_youtube_url)
        except:
            webbrowser.open("https://www.google.com/search?q=youtube+ %s +trailer" % self.title)
