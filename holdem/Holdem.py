import sys
import os
import itertools
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from pydealer import Deck
from HandAnalyzer import HandAnalyzer

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("* Texas Hold'em *")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        # Card and Deck Info
        self.initializeCardData()

        handCardPNGCodes = []
        for card in self.hand:
            if card.value == '10':
                handCardPNGCodes.append(f"T{card.suit[0]}")
            else:
                handCardPNGCodes.append(f"{card.value[0]}{card.suit[0]}")

        self.communityCardPNGCodes = []
        for card in self.communityCards:
            if card.value == '10':
                self.communityCardPNGCodes.append(f"T{card.suit[0]}")
            else:
                self.communityCardPNGCodes.append(f"{card.value[0]}{card.suit[0]}")
        self.communityCardPNGCodes.append(f"1B")

        # Hand Display
        self.handWidget = QWidget()
        self.handLayout = QHBoxLayout(self.handWidget)

        self.card0 = QLabel()
        self.card1 = QLabel()

        self.card0.setPixmap(QPixmap(f"{basedir}/images/cards/{handCardPNGCodes[0]}.png"))
        self.card1.setPixmap(QPixmap(f"{basedir}/images/cards/{handCardPNGCodes[1]}.png"))

        self.handLayout.addWidget(self.card0)
        self.handLayout.addWidget(self.card1)
        self.handLayout.setAlignment(Qt.AlignCenter)

        # Community Cards Display
        self.communityCardsWidget = QWidget()
        self.communityCardsLayout = QHBoxLayout(self.communityCardsWidget)

        self.flopCard1 = QLabel()
        self.flopCard2 = QLabel()
        self.flopCard3 = QLabel()
        self.turnCard = QLabel()
        self.riverCard = QLabel()

        self.flopCard1.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[5]}.png"))
        self.flopCard2.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[5]}.png"))
        self.flopCard3.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[5]}.png"))
        self.turnCard.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[5]}.png"))
        self.riverCard.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[5]}.png"))

        self.communityCardsLayout.addWidget(self.flopCard1)
        self.communityCardsLayout.addWidget(self.flopCard2)
        self.communityCardsLayout.addWidget(self.flopCard3)
        self.communityCardsLayout.addWidget(self.turnCard)
        self.communityCardsLayout.addWidget(self.riverCard)
        self.communityCardsLayout.setAlignment(Qt.AlignCenter)

        # Action Buttons
        self.buttonWidget = QWidget()
        self.buttonLayout = QHBoxLayout(self.buttonWidget)

        self.revealFlopButton = QPushButton("Reveal Flop")
        self.revealTurnButton = QPushButton("Reveal Turn")
        self.revealRiverButton = QPushButton("Reveal River")
        self.determineWinnerButton = QPushButton("Determine Winner")
        self.revealFlopButton.clicked.connect(self.revealFlop)
        self.revealTurnButton.clicked.connect(self.revealTurn)
        self.revealRiverButton.clicked.connect(self.revealRiver)
        self.determineWinnerButton.clicked.connect(self.determineWinner)

        self.buttonLayout.addWidget(self.revealFlopButton)
        self.buttonLayout.addWidget(self.revealTurnButton)
        self.buttonLayout.addWidget(self.revealRiverButton)
        self.buttonLayout.addWidget(self.determineWinnerButton)
        self.buttonLayout.setAlignment(Qt.AlignCenter)

        # Result Display
        self.resultWidget = QWidget()
        self.resultLayout = QHBoxLayout(self.resultWidget)

        self.resultLabel = QLabel("")

        self.resultLayout.addWidget(self.resultLabel)
        self.resultLayout.setAlignment(Qt.AlignCenter)

        # App Layout
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.addWidget(self.handWidget)
        self.verticalLayout.addWidget(self.communityCardsWidget)
        self.verticalLayout.addWidget(self.buttonWidget)
        self.verticalLayout.addWidget(self.resultWidget)

    def initializeCardData(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = self.deck.deal(2)
        self.hand.sort()
        self.communityCards = self.deck.deal(5)

    def revealFlop(self):
        self.flopCard1.hide()
        self.flopCard2.hide()
        self.flopCard3.hide()
        self.flopCard1.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[0]}.png"))
        self.flopCard2.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[1]}.png"))
        self.flopCard3.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[2]}.png"))
        self.flopCard1.show()
        self.flopCard2.show()
        self.flopCard3.show()

    def revealTurn(self):
        self.turnCard.hide()
        self.turnCard.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[3]}.png"))
        self.turnCard.show()

    def revealRiver(self):
        self.riverCard.hide()
        self.riverCard.setPixmap(QPixmap(f"{basedir}/images/cards/{self.communityCardPNGCodes[4]}.png"))
        self.riverCard.show()

    def determineWinner(self):
        # determine all unique 3 card combinations of the community cards
        analyzer = HandAnalyzer()
        bestResult = ('high-card','2') # worst possible hand
        for combo in itertools.combinations(self.communityCards, 3):
            [self.hand.add(c) for c in combo]
            # create temp "hand" with hand + combo (five cards total now)
            result = analyzer.calculate(self.hand)
            if result > bestResult:
                bestResult = result
            # reset the hand back to the default state
            del self.hand[4]
            del self.hand[3]
            del self.hand[2]
        self.resultLabel.setText(f"You got {bestResult[0].replace('-',' ')} ({bestResult[1]})")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()