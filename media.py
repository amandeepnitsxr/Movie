import webbrowser
import time
class Movie():
     '''constructor'''

    def __init__(self,movie_title,movie_story,movie_poster,movie_trailor):
        '''__init__'''
        self.title = movie_title
        self.storyline = movie_story
        self.poster = movie_poster
        self.trailor = movie_trailor


    
    def show_trailor(self):

        '''show trailor'''
        time.sleep(10)
        webbrowser.open(self.trailor)


          
