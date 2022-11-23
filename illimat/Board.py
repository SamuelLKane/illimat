from Field import Field


class Board:

    fields = []
    seasons = ['summer','autumn','winter','spring']
    okusTokensRemaining = 0

    def __init__(self):
        self.setupBoardState()

    def getBoardState(self):
        return [field for field in self.fields]

    def setupBoardState(self):
        self.okusTokensRemaining = 4
        self.fields = [Field(season) for season in self.seasons]