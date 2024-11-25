class TV:
    def turn_on(self):
        return""


class Speakers:
    def turn_on(self):
        return""


class HomeFacade:
    def __init__(self):
        self.tv = TV()
        self.spaekers = Speakers()

    def start_movie(self):
        return f"{self.tv} and {self.speakes} start the movie "
    