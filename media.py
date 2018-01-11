import webbrowser
class Movie():
    """Movie class
    Movie class with title, storyline, poster, trailer and director information.
    Attributes:
        movie_title: A string storing the title of the movie.
        movie_storyline: A string storing storyline of the movie
        poster_image: A string storing url for the poster image of the movie.
        trailer_youtube: A string storing url for youtube trailer of the movie.
        director: A string for storing name of the director of the movie,
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director):
        """Inits Movie Class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director

    def show_trailer(self):
        """Shows trailer from the url"""
        webbrowser.open(self.trailer_youtube_url)