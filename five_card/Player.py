import pydealer
class Player:
    id: int = None
    hand = pydealer.Stack()

    def __init__(self, id, cards) -> None:
        self.id = id
        self.hand = cards

    def getHand(self):
        return self.hand
    
    def swapCard(self, oldCard, newCard):
        del self.hand[self.hand.find(f"{oldCard.value} of {oldCard.suit}")[0]]
        self.hand.add(newCard)

    def getPlayerState(self):
        return {
            'id': self.id,
            'size': len(self.getHand()),
            'hand': self.getHand()
        }