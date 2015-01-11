import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his awesome toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print toy_story.storyline

avatar = media.Movie("Avatar",
                     "A marine on an alien planet","",
                     "www.youtube.com/watch?v=cRdxXPV9GNQ")

mystery_alaska = media.Movie("Mystery Alaska",
                            "This comedy is about the residents of a small town who get over-excited when their hockey team gets chosen to host a televised event",
                            "http://ia.media-imdb.com/images/M/MV5BMjE2MDM2NzcyMl5BMl5BanBnXkFtZTYwMzA2NjQ3._V1_SX300.jpg",
                            "www.youtube.com/watch?v=a80x06Wn91U")

movies = [toy_story, avatar, mystery_alaska]

fresh_tomatoes.open_movies_page(movies)
