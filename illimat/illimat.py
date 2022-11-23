import random
import pydealer

from Board import Board
from Player import Player
# https://www.reddit.com/r/Illimat/wiki/luminaries/

# Game Variables
LUMINARIES = {
    'The Maiden': "While the Maiden is on the board, winter has no effect. Cards may be Harvested from the Winter Field. This effect occurs even if the Maiden isn't in the Winter Field.",
    'The Changling': "Once during your turn, you may exchange a card from your hand with a card in the same Field as the Changeling. You may do this at any point in your turn, either before or after your play. You can't exchange card hat are part of a Stockpile. This act of exchange dos not change the season. When you Claim the Changeling, you may immediately exchange two card from your hand for any other two cards on the board.",
    'The Forest Queen': "It is always Summer in the Field of the Forest Queen. When the Forest Queen is revealed turn the Illimat so that it is Summer in her Field. As long as the Forest Queen is on the board, the seasons do not change for any reason. When you claim the Forest Queen, you may immediately turn the Illimat to any new position.",
    'The River': "When the River is revealed, deal six cards into the River's Field instead of the usual thee cards. If, at the end of the hand, you have claimed the RIver and you are Frostbit, you gain two points instead of losing two points.",
    'The Children': "When the Children is revealed, deal three cards (if available) beneath the Children. These cards are kept hidden and aren't revealed to any player. When you claim the Children, these card s are added to your Harvest pile. You may examine them, but do not have to reveal their values to the other players.",
    'The Rake': "Once during your turn, you must Sow one card into the Field containing the Rake. You may do this at any point in your turn, either before or after play. This ignores restrictions of season, and Sowing a Face card turns the Illimat as usual. When you claim the Rake, each player must give you one Summer card from their Harvest pile, if they have one.",
    'The Union': "When you perform the Harvest action in the field of the Union, you may play two cards from your hand instead of one. Combine these two cards and proceed as if you had played a single card of that combined value. So if you play a Seven and a Knight (11) from your hand, you may harvest as if you'd played one card with a value of eighteen. At the end of your turn, draw until you have four cards in your hand.",
    'The Newborn': "When the is revealed, it reveals the Luminary in the opposite field; so if the Newborn is revealed in the field that is currently Summer, reveal the Luminary in the field that is in Winter. If there is no Luminary in that field (because it's already been claimed), randomly deal and reveal a new Luminary from those not currently in use. If there is already a revealed Luminary in the field, the Newborn has no effect."
}
numberOfPlayers = 0

# Round Variables
roundDeck = None
roundNumber = 0
roundLuminaries = []
players = []

def setupRound():
    pass

def startGame():
    pass

if __name__ == "__main__":
    print("----- Seasons Settle on a new board -----\n")
    roundDeck = pydealer.Deck()
    roundLuminaries = random.sample(LUMINARIES.items(),4)
    gameBoard = Board()

    print("----- Sowing the fields -----")
    for field in gameBoard.getBoardState():
        field.setup(roundDeck.deal(3), roundLuminaries.pop())
    

    numberOfPlayers = int(input("How many people are playing: "))
    if numberOfPlayers > 3 or numberOfPlayers < 2:
        print("----- this illimat only supports 2 or 3 players")
        exit()
    
    print("----- Dealing players in -----")
    for playerId in range(numberOfPlayers):
        players.append(
            Player(
                playerId,
                roundDeck.deal(
                    3 if playerId == roundNumber % numberOfPlayers else 4
                )
            )
        )
    
    print("----- And so The Society begins this round -----")