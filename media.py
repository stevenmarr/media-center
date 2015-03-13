import webbrowser
import json
import urllib

class Movie():
    def __init__(self,movie_title,
                trailer_youtube,
                movie_storyline = None,
                poster_image = None):
     """Creates a new movie object for viewing trailer, story line, and a poster image.
    
    Args:
      movie_title: The title of the movie to add.
      trailer_youtube: URL of a version of the moview trailers found on YouTube.com
      movie_storyline: a string of the movies description, if left unnassigned the app 
      will query the omdapi to search for movie description
      poster_image: A url where the movies poster artwork can be found, if left blank the 
      app will query the omdapi to search for the poster image
    """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if (self.storyline == None or
            self.poster_image_url == None):
            try:
                url = ("http://www.omdbapi.com/?t=%s&y=&plot=short&r=json"%self.title)
                response = urllib.urlopen(url)
                string = response.read().decode('utf-8')
                json_obj = json.loads(string)
                if self.storyline == None:
                    self.storyline = json_obj['Plot']
                if self.poster_image_url == None:
                    self.poster_image_url = json_obj['Poster']
            except:
                self.storyline = "No plot information available"
                self.poster_image_url = "http://uploads.neatorama.com/images/posts/95/58/58095/1360112719-0.jpg"
    def show_trailer(self):
        """Open window in webbrowser to view trailer"""
        try:
            webbrowser.open(self.trailer_youtube_url)
        except:
            webbrowser.open("https://www.google.com/search?q=youtube+%s+trailer" % self.title)
