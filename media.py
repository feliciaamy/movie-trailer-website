import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    def __init__(self,title,storyline,poster,youtube,rating,rank):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube
        self.rating = rating
        self.rank = rank
        
    def show_trailer(self):
        #Open youtube to show the trailer of the movie
        webbrowser.open(self.trailer_youtube_url)
    
        
