import pydealer
class Player:
    id: int = None
    hand = pydealer.Stack()
    validPositions = [0,1,2,3,4]

    def __init__(self, id, cards) -> None:
        self.id = id
        self.hand = cards

    def getHand(self):
        return self.hand
    
    def swapCard(self, oldCard, newCard, position):
        """Discard a card and Replace it with another from the deck"""
        if position not in self.validPositions:
            print("Invalid Position, please select another card")
            return
        del self.hand[self.hand.find(f"{oldCard.value} of {oldCard.suit}")[0]]
        del self.validPositions[position]
        self.hand.insert(newCard[0], position)
        

    def getPlayerState(self):
        return {
            'id': self.id,
            'size': len(self.getHand()),
            'validOptions': self.validPositions,
            'hand': self.getHand()
        }