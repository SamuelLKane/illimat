from pydealer import Stack, Card
class Player:
    id: int = None
    hand = Stack()
    validPositions = [0,1,2,3,4]

    def __init__(self, id: int, cards: Stack) -> None:
        self.id = id
        self.hand = cards

    def getHand(self):
        return self.hand
    
    def swapCard(self, newCard:Card, position: int):
        """Discard a card and Replace it with another from the deck"""
        if position >= 5 or position < 0:
            print("Invalid Position, please input a number between 0 and 4")
            return
        if self.validPositions[position] == -1:
            print("Invalid Position, please select another card")
            return
        del self.hand[0]
        self.validPositions[position] = -1
        #? Check that this correctly inserts the card at the right position
        self.hand.insert(newCard[0], position)
        

    def getPlayerState(self):
        return {
            'id': self.id,
            'size': len(self.getHand()),
            'validOptions': self.validPositions,
            'hand': self.getHand()
        }