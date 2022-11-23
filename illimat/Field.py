import string
import pydealer

class Field:

    cardsInField = []
    luminary = None
    season:string = None
    
    def __init__(self, season:string):
        self.season = season

    def getFieldState(self):
        return {
            'season': self.season,
            'cards': self.cardsInField,
            'luminary': self.luminary
        }

    def setSeason(self, season: string):
        self.season = season

    def getSeason(self):
        return self.season

    def setup(self, cards, luminary):
        self.cardsInField = cards
        self.luminary = luminary

    def sow(self):
        pass

    def stockpile(self):
        pass

    def harvest(self):
        pass