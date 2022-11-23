class Player:
    id: int = None
    hand = []

    def __init__(self, id, cards):
        self.id = id
        self.hand = cards
    
    def getHand(self):
        return self.hand

    def drawCard(self, card):
        self.hand.append(card)

    def getPlayerState(self):
        return {
            'id': self.id,
            'hand': self.hand
        }