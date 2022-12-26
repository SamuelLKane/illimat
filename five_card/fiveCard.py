import pydealer
import threading
from typing import List

from Player import Player
from HandAnalyzer import HandAnalyzer
import RoundTimer
import PlayerSimulator

deck = None
players = []

@RoundTimer.timeout(60)
def playThreadedRound(players: List[Player], difficulty: str):
    print("Playing threaded Round")

    threads = []
    for i, player in enumerate(players):
        t = None
        if i == 0:
            t = threading.Thread(target=playHumanHand, args=[player])
        else:
            t = threading.Thread(target=PlayerSimulator.simulatePlayer, args=[player, deck, difficulty])
        t.start()
        threads.append(t)
    
    [thread.join() for thread in threads]

def playHumanHand(player: Player):
    count = 0
    while True:
        print(f"Your Hand:\n{player.getHumanReadableHand()}")
        cardPosition = int(input("Which card would you like to discard?"))
        player.swapCard(deck.deal(1), cardPosition)
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
    
    difficulty = input("Choose a difficulty for this player:\n1 - easy\n2 - medium\n3 - hard\n")
    try:
        playThreadedRound(players, difficulty)            
    except RoundTimer.TimeoutError:
        print("\nRound is over")

    # calculate winning hand
    analyzer = HandAnalyzer()
    results = [analyzer.calculate(player.getHand()) for player in players]

    print(f"Player {results.index(max(results))} won with {max(results)[0].replace('-',' ')}")