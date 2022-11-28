"""Calculates a relative hand ranking for traditional poker hands"""
# Derived from https://github.com/megacolorboy/ProjectEuler/blob/master/poker_lib.py
import pydealer

class HandAnalyzer:

    ranks = '2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace'
    ranksList = ranks.split(',')

    def __init__(self) -> None:
        pass
    
    def calculate(self, hand):
        rankOrder = [
            self._royalFlush,
            self._straightFlush,
            self._fourOfAKind,
            self._fullHouse,
            self._flush,
            self._straight,
            self._threeOfAKind,
            self._twoPair,
            self._onePair,
            self._highCard
        ]
        for rank in rankOrder:
            rank = rank(pydealer.tools.sort_cards(hand))

            if rank:
                break

        return rank

    def _royalFlush(self, hand):
        royalValue = '10JackQueenKingAce'
        if all(hand[0].suit == card.suit for card in hand[1:]):
            if ''.join(card.value for card in hand) in royalValue:
                return 'royal-flush', hand[-1].value
        return False

    def _straightFlush(self, hand):
        if all(hand[0].suit == card.suit for card in hand[1:]):
            if ''.join(card.value for card in hand) in ''.join(self.ranksList):
                return 'straight-flush', hand[-1].value
        return False

    def _fourOfAKind(self, hand):
        handValues = [card.value for card in hand]
        uniqueHandRanks = set(handValues)

        # if there are more than 2 ranks, it's not four of a kind
        if len(uniqueHandRanks) != 2:
            return False

        for f in uniqueHandRanks:
            # if there are 4 faces, it is four of a kind
            if handValues.count(f) == 4:
                uniqueHandRanks.remove(f)
                return "four-of-a-kind", f

        return False

    def _fullHouse(self, hand):
        handValues = [card.value for card in hand]

        rankFrequency = {}
        for value in handValues:
            if value in rankFrequency:
                rankFrequency[value] += 1
            else:
                rankFrequency[value] = 1

        # if there are 2 types of ranks and there's a card with 1 pair and 3 of a kind
        if len(rankFrequency) == 2 and (rankFrequency.values()[0] == 2 and rankFrequency.values()[1] == 3):
            return 'full-house'

        return False

    def _flush(self, hand):
        handValues = [card.value for card in hand]

        first_card = hand[0]
        other_cards = hand[1:]

        if all(hand[0].suit == card.suit for card in hand[1:]):
            return 'flush', handValues

        return False

    def _straight(self, hand):
        if ''.join(card.value for card in hand) in ''.join(self.ranksList):
            return 'straight', hand[-1].value
        return False

    def _threeOfAKind(self, hand):
        handValues = [card.value for card in hand]
        uniqueHandRanks = set(handValues)

        if len(uniqueHandRanks) != 3:
            return False

        for f in uniqueHandRanks:
            if handValues.count(f) == 3:
                uniqueHandRanks.remove(f)
                return "three-of-a-kind", f

        return False

    def _twoPair(self, hand):
        handValues = [card.value for card in hand]
        uniqueHandRanks = set(handValues)
        
        # collect pairs
        pairs = [f for f in uniqueHandRanks if handValues.count(f) == 2]
        
        # if there are more than two pairs
        if len(pairs) != 2:
            return False
        return 'two-pair', pairs

    def _onePair(self, hand):
        handValues = [card.value for card in hand]
        uniqueHandRanks = set(handValues)

        # collect pairs
        pairs = [f for f in uniqueHandRanks if handValues.count(f) == 2]

        # if there's more than one pair
        if len(pairs) != 1:
            return False
        return 'one-pair', pairs

    def _highCard(self, hand):
        return "high-card", hand[0].value