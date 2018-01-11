import fresh_tomatoes
import media

im_juli = media.Movie("Im Juli", "Can Daniel follow the sun from Hamburg to the Bosporus by Friday to meet his love?",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIwMTM0MzMzNF5BMl5BanBnXkFtZTcwMTczNTUyMQ@@._V1_.jpg",
                      "https://www.youtube.com/watch?v=S5PzL-M3aWM", "Fatih Akin")
last_emperor = media.Movie("The Last Emperor ", "The story of the final Emperor of China. ",
                           "https://upload.wikimedia.org/wikipedia/en/e/e5/The_Last_Emperor_filmposter.jpg",
                           "https://www.youtube.com/watch?v=QBUbmT8cCkM",
                           "Bernardo Bertolucci")

seven_years_in_tibet = media.Movie("Seven Years in Tibet",
                             "True story of Heinrich Harrer, an Austrian mountain climber who became friends with the Dalai Lama at the time of China's takeover of Tibet. ",
                             "https://upload.wikimedia.org/wikipedia/en/9/97/Seven_Years_in_Tibet_cover.jpeg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             "Jean-Jacques Annaud")

kundun = media.Movie("Kundun", "From childhood to adulthood, Tibet's fourteenth Dalai Lama deals with Chinese oppression and other problems.",
                          "https://upload.wikimedia.org/wikipedia/en/1/1c/Kundun_film_poster.jpg",
                          "https://www.youtube.com/watch?v=TW2USm6wTSA&hl=en-GB&gl=SG",
                          "Martin Scorsese" )

three_idiots = media.Movie("3 Idiots",
                           "Two friends looking for a lost buddy deal with a forgotten bet, a wedding they are forced to crash and an out of control funeral.",
                           "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w",
                           "Rajkumar Hirani")

# list that holds the Movie objects
movies = [im_juli, last_emperor, seven_years_in_tibet, kundun, three_idiots]
fresh_tomatoes.open_movies_page(movies)