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

    def getHumanReadableHand(self):
        handString = []
        for position in range(len(self.validPositions)):
            if self.validPositions[position] == -1:
                handString.append(f"  - {self.hand[position]}")
            else:
                handString.append(f"{position} - {self.hand[position]}")
        return "\n".join(handString)
    
    def swapCard(self, newCard:Card, position: int):
        """Discard a card and Replace it with another from the deck"""
        if position >= 5 or position < 0:
            print("Invalid Position, please input a number between 0 and 4")
            return
        if self.validPositions[position] == -1:
            print("Invalid Position, please select another card")
            return
        #! Somehow multiple positions are getting set to -1
        self.validPositions[position] = -1
        self.hand.insert(newCard[0], position)
        del self.hand[position + 1]
        

    def getPlayerState(self):
        return {
            'id': self.id,
            'size': len(self.getHand()),
            'validOptions': self.validPositions,
            'hand': [card for card in self.getHand()]
        }