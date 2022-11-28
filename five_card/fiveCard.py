import pydealer
import time

from Player import Player
from HandAnalyzer import HandAnalyzer
import roundTimer

deck = None
players = []

@roundTimer.timeout(5) # 60
def playRound(player):
    print("Beginning round...")

    playerHand = player.getHand()
    print(f"Your Hand:\n{playerHand}")

    while True:
        cardPosition = int(input("Which card would you like to discard?"))
        player.swapCard(playerHand[cardPosition], deck.deal(1), cardPosition)
        print(f"Your Hand:\n{playerHand}")

if __name__ == "__main__":
    print("---- Five Card Draw ----")
    deck = pydealer.Deck()
    deck.shuffle()

    numberOfPlayers = int(input("How many people are playing: "))
    if numberOfPlayers < 2:
        print("You need at least two players to play Five Card Draw")
        exit()

    print("Dealing Players In...")
    for playerId in range(numberOfPlayers):
        players.append(
            Player(
                playerId,
                deck.deal(5)
            )
        )
    
    try:
        playRound(player=players[0])
        # simulate other hands (will require threading)
    except roundTimer.TimeoutError:
        print("\nRound is over")

    # calculate winning hand
    analyzer = HandAnalyzer()
    result = analyzer.calculate(players[0].getHand())
    print(result)