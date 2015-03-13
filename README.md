media center
=================

This project will display a webpage showcasing movie artwork, descriptions and trailers.



Getting Started:

1) Open entertainment_center.py in a text editor and add a new movie to the list of defined movies.

		Creating movies:
		The Movie base class creates a new movie object for viewing trailer, story line, and a poster image.

		class media.Movie
		__init__(self,movie_title, trailer_youtube, movie_storyline = None, poster_image = None)

		Parameters
		movie_title: The title of the movie to add.
		trailer_youtube: URL of a version of the moview trailers found on YouTube.com
		movie_storyline: a string of the movies description, if left unnassigned the app 
			will query the omdapi to search for movie description
		poster_image: A url where the movies poster artwork can be found, if left blank the 
			app will query the omdapi to search for the poster image


EXAMPLE:

		toy_story = media.Movie("Toy Story", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
		avatar = media.Movie("Avatar", "www.youtube.com/watch?v=cRdxXPV9GNQ")

2) Add the movie object name to the list of movies.

EXAMPLE:

		movies = [toy_story, avatar]



3) Start the webserver by running the fresh_tomatoes.py script

EXAMPLE:

		python fresh_tomatoes.py



Steven Marr
stevenmarr@me.com

