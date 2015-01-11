import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his awesome toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print toy_story.storyline

avatar = media.Movie("Avatar",
                     "A marine on an alien planet")

print avatar.storyline

#avatar.show_trailer()
toy_story.show_trailer()
