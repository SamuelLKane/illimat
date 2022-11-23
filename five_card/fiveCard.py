import pydealer

from Player import Player

deck = None
# deck.shuffle()
players = []

if __name__ == "__main__":
    print("---- Five Card Draw ----")
    deck = pydealer.Deck()
    # deck.shuffle()

    numberOfPlayers = int(input("How many people are playing: "))
    # if numberOfPlayers < 2:
    #     print("You need at least two players to play Five Card Draw")
    #     exit()

    print("Dealing Players In...")
    for playerId in range(numberOfPlayers):
        players.append(
            Player(
                playerId,
                deck.deal(5)
            )
        )

    
    player0 = players[0]
    player0Hand = player0.getHand()
    print(f"Player 0's Hand:\n{player0Hand}")
    player0.swapCard(player0Hand[0], deck.deal(1))
    print(f"Player 0's Hand:\n{player0Hand}")
