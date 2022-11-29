"""Simulates a human player for Five Card Draw"""
import random
from Player import Player
from pydealer import Deck

def simulatePlayer(player: Player, deck: Deck ,difficulty='easy',):
    difficultyMap = {
        'easy': simulateEasy,
        'medium': simulateMedium,
        'hard': simulateHard
    }
    difficultyMap[difficulty](player, deck)

def simulateEasy(player: Player, deck: Deck):
    """Easy players don't understand the game and thus will do things at random"""
    for position in range(5):
        if random.randrange(2^5) == 0:
            player.swapCard(deck.deal(1),position)
            

def simulateMedium(player: Player, deck: Deck):
    """Medium players understand strategy and will analyze their hand but still behave randomly"""
    for position in range(5):
        if random.randrange(2^5) == 0:
            #TODO: Add intelligent swapping here using hand analyzer
            player.swapCard(deck.deal(1),position)

def simulateHard(player: Player, deck: Deck):
    """Hard players will try and optimize their hands with zero randomness"""
    for position in range(5):
        #TODO: Add intelligent swapping here using hand analyzer
        player.swapCard(deck.deal(1),position)
    simulateEasy(player, deck)