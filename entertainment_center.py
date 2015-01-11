import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "www.youtube.com/watch?v=cRdxXPV9GNQ")

mystery_alaska = media.Movie("Mystery Alaska",
                            "www.youtube.com/watch?v=a80x06Wn91U")

the_princess_bride = media.Movie("The Princess Bride",
                                "https://www.youtube.com/watch?v=njZBYfNpWoE")
clue = media.Movie("Clue",
                    "https://www.youtube.com/watch?v=NHEpuz_gUGM")
despicable_me = media.Movie("Despicable Me",
                    "https://www.youtube.com/watch?v=sUkZFetWYY0")








movies = [toy_story, avatar, mystery_alaska, the_princess_bride, clue,
            despicable_me]

fresh_tomatoes.open_movies_page(movies)
