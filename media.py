import webbrowser

class Movie:

    def __init__(self,title,trailer_youtube_url,movie_storyline,poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        return

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        return

    
    
