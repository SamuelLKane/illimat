"""Simulates a human player for Five Card Draw"""
import random
from typing import List
from Player import Player
from pydealer import Card, Deck, Stack, tools
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
    """Medium players understand strategy and will analyze their hand but still behave randomly"""
    for _ in range(5):
        if random.randrange(2^3) == 0:
            positionToSwap = _determineBestMove(player.getHand(), player.validPositions)
            if positionToSwap != -1:
                player.swapCard(deck.deal(1),position=positionToSwap)


def simulateHard(player: Player, deck: Deck):
    """Hard players will try and optimize their hands with zero randomness"""
    for _ in range(5):
        positionToSwap = _determineBestMove(player.getHand(), player.validPositions)
        if positionToSwap != -1:
            player.swapCard(deck.deal(1),position=positionToSwap)


def _determineBestMove(hand: Stack, validPositions: List[int]):
    """Analyzes a hand for the 'best move' and returns the position to drop,
    returns -1 if hand is already optimal"""
    analyzer = HandAnalyzer()
    currentHandRank = analyzer.calculate(hand)

    handRank = currentHandRank[0]
    highCard = currentHandRank[1]

    goodRanks = [
        'a-royal-flush',
        'a-straight-flush',
        'four-of-a-kind',
        'a-full-house',
        'a-flush',
        'a-straight'
    ]
    if(handRank in goodRanks):
        return -1

    if(handRank in ['two-pair','one-pair','three-of-a-kind']):
        for i, card in enumerate(hand):
            if card.value in highCard:
                continue
            if validPositions[i] == -1:
                continue
            return i

    if(handRank == 'high-card'): # * working!
        sortedHand = tools.sort_cards(hand)
        cardToDrop: Card = None
        for i, card in enumerate(sortedHand):
            if validPositions[i] == -1:
                continue
            if i == 4: 
                continue
            cardToDrop = card
            break

        if cardToDrop:
            return hand.find(cardToDrop.name)[0]

    return -1