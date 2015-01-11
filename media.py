class Movie():
    def __init__(self,movie_title, movie_storyline = None, poster_image = None, trailer_youtube = None ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
