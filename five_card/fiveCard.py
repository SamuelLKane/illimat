import pydealer

from Player import Player
from HandAnalyzer import HandAnalyzer
import RoundTimer
import PlayerSimulator

deck = None
players = []

@RoundTimer.timeout(60)
def playRound(player: Player):
    print("Beginning round...")

    playerHand = player.getHand()
    print(f"Your Hand:\n{playerHand}")

    count = 0
    while True:
        cardPosition = int(input("Which card would you like to discard?"))
        player.swapCard(deck.deal(1), cardPosition)
        print(f"Your Hand:\n{playerHand}")
        count += 1
        if count == 5:
            break

if __name__ == "__main__":
    print("---- Five Card Draw ----")
    deck = pydealer.Deck()
    deck.shuffle()

    numberOfPlayers = int(input("How many people are playing: "))
    if numberOfPlayers < 2:
        print("You need at least two players to play Five Card Draw")
        exit()

    print("Dealing Players In...")
    players = [Player(playerId, deck.deal(5)) for playerId in range(numberOfPlayers)]
    
    try:
        # TODO: Thread this and move to playRound method so they are both wrapped in the timer
        for i, player in enumerate(players):
            if i == 0:
                pass
                playRound(player)
            else:
                inputDiff = input("Choose a difficulty for this player:\n1 - easy\n2 - medium\n3 - hard\n")
                print(inputDiff)
                PlayerSimulator.simulatePlayer(player, deck, inputDiff)
            
    except RoundTimer.TimeoutError:
        print("\nRound is over")

    # calculate winning hand
    analyzer = HandAnalyzer()
    results = [analyzer.calculate(player.getHand()) for player in players]

    print(f"Player {results.index(max(results))} won with {max(results)[0].replace('-',' ')}")