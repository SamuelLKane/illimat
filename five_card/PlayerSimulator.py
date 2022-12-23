"""Simulates a human player for Five Card Draw"""
import random
from Player import Player
from pydealer import Deck
from HandAnalyzer import HandAnalyzer

def simulatePlayer(player: Player, deck: Deck ,difficulty='1',):
    difficultyMap = {
        '1': simulateEasy,
        '2': simulateMedium,
        '3': simulateHard
    }
    difficultyMap[difficulty](player, deck)

def simulateEasy(player: Player, deck: Deck):
    """Easy players don't understand the game and thus will do things at random"""
    for position in range(5):
        if random.randrange(2^5) == 0:
            player.swapCard(deck.deal(1),position)
            

def simulateMedium(player: Player, deck: Deck):
    analyzer = HandAnalyzer()
    """Medium players understand strategy and will analyze their hand but still behave randomly"""
    for position in range(5):
        if random.randrange(2^3) == 0:
            currentHandRank = analyzer.calculate(player.getHand())
            if(currentHandRank[0] < 'a-royal-flush'):
                #TODO: Add intelligent swapping here using hand analyzer
                pass
            player.swapCard(deck.deal(1),position)

def simulateHard(player: Player, deck: Deck):
    analyzer = HandAnalyzer()
    """Hard players will try and optimize their hands with zero randomness"""
    for position in range(5):
        currentHandRank = analyzer.calculate(player.getHand())
        if(currentHandRank[0] < 'a-royal-flush'):
            #TODO: Add intelligent swapping here using hand analyzer
            pass
        player.swapCard(deck.deal(1),position)
    simulateEasy(player, deck)