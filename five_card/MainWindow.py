import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

from pydealer import Deck, Card
from HandAnalyzer import HandAnalyzer

class CardButton(QAbstractButton):
    def __init__(self, pixmap: QPixmap, parent=None):
        super(CardButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Five Card Draw")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        # Card and Deck Info
        self.initializeCardData()
        self.confirm = True

        pngCodes = []
        for card in self.hand:
            if card.value == '10':
                pngCodes.append(f"T{card.suit[0]}")
            else:
                pngCodes.append(f"{card.value[0]}{card.suit[0]}")

        # Cards as Buttons
        self.card0Button = CardButton(QPixmap(f"GUI/card_images/{pngCodes[0]}.png"),self)
        self.card1Button = CardButton(QPixmap(f"GUI/card_images/{pngCodes[1]}.png"),self)
        self.card2Button = CardButton(QPixmap(f"GUI/card_images/{pngCodes[2]}.png"),self)
        self.card3Button = CardButton(QPixmap(f"GUI/card_images/{pngCodes[3]}.png"),self)
        self.card4Button = CardButton(QPixmap(f"GUI/card_images/{pngCodes[4]}.png"),self)

        self.card0Button.clicked.connect(self.clickCard0)
        self.card1Button.clicked.connect(self.clickCard1)
        self.card2Button.clicked.connect(self.clickCard2)
        self.card3Button.clicked.connect(self.clickCard3)
        self.card4Button.clicked.connect(self.clickCard4)

        self.handWidget = QWidget()
        self.handLayout = QHBoxLayout(self.handWidget)

        self.handLayout.addWidget(self.card0Button)
        self.handLayout.addWidget(self.card1Button)
        self.handLayout.addWidget(self.card2Button)
        self.handLayout.addWidget(self.card3Button)
        self.handLayout.addWidget(self.card4Button)

        # Confirmation Button
        self.buttonWidget = QWidget()
        self.buttonLayout = QHBoxLayout(self.buttonWidget)

        self.confirmButton = QPushButton("Confirm Hand")
        self.confirmButton.clicked.connect(self.clickConfirm)

        self.buttonLayout.addWidget(self.confirmButton)
        self.buttonLayout.setAlignment(Qt.AlignCenter)

        # Result Display
        self.resultWidget = QWidget()
        self.resultLayout = QHBoxLayout(self.resultWidget)

        self.resultLabel = QLabel("Click confirm to get your result!")

        self.resultLayout.addWidget(self.resultLabel)
        self.resultLayout.setAlignment(Qt.AlignCenter)

        # App Layout
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.addWidget(self.handWidget)
        self.verticalLayout.addWidget(self.buttonWidget)
        self.verticalLayout.addWidget(self.resultWidget)

    
    def initializeCardData(self):
        # TODO: this will come from fiveCard.py, update init to compensate
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = self.deck.deal(5)
        self.hand.sort()
        self.validPositions = [0,1,2,3,4]
        

    def swapCard(self, position: int):
        self.validPositions[position] = -1
        newCard: Card = self.deck.deal(1)[0]
        if newCard.value == '10':
            newPixmap = QPixmap(f"GUI/card_images/T{newCard.suit[0]}.png")
        else:
            newPixmap = QPixmap(f"GUI/card_images/{newCard.value[0]}{newCard.suit[0]}.png")
        self.hand.insert(newCard, position)
        del self.hand[position + 1]
        return newPixmap
    
    def clickCard0(self):
        if 0 in self.validPositions:
            self.card0Button.hide()
            self.card0Button.pixmap = self.swapCard(0)
            self.card0Button.show()

    def clickCard1(self):
        if 1 in self.validPositions:
            self.card1Button.hide()
            self.card1Button.pixmap = self.swapCard(1)
            self.card1Button.show()

    def clickCard2(self):
        if 2 in self.validPositions:
            self.card2Button.hide()
            self.card2Button.pixmap = self.swapCard(2)
            self.card2Button.show()

    def clickCard3(self):
        if 3 in self.validPositions:
            self.card3Button.hide()
            self.card3Button.pixmap = self.swapCard(3)
            self.card3Button.show()

    def clickCard4(self):
        if 4 in self.validPositions:
            self.card4Button.hide()
            self.card4Button.pixmap = self.swapCard(4)
            self.card4Button.show()
    
    def clickConfirm(self):
        if self.confirm :

            # Analyze hand and display result
            analyzer = HandAnalyzer()
            result = analyzer.calculate(self.hand)
            self.resultLabel.setText(f"You got {result[0].replace('-',' ')} ({result[1]})")

            # Update Button to play again!
            self.confirmButton.setText("Play Again?")
            self.confirm = False
        else:
            # Update Confirm Button and Result Label
            self.confirmButton.setText("Confirm Hand")
            self.resultLabel.setText("Click confirm to get your result!")

            # Reset Card data and deal again!
            self.initializeCardData()
            
            pngCodes = []
            for card in self.hand:
                if card.value == '10':
                    pngCodes.append(f"T{card.suit[0]}")
                else:
                    pngCodes.append(f"{card.value[0]}{card.suit[0]}")

            self.card0Button.hide()
            self.card0Button.pixmap = QPixmap(f"GUI/card_images/{pngCodes[0]}.png")
            self.card0Button.show()

            self.card1Button.hide()
            self.card1Button.pixmap = QPixmap(f"GUI/card_images/{pngCodes[1]}.png")
            self.card1Button.show()

            self.card2Button.hide()
            self.card2Button.pixmap = QPixmap(f"GUI/card_images/{pngCodes[2]}.png")
            self.card2Button.show()

            self.card3Button.hide()
            self.card3Button.pixmap = QPixmap(f"GUI/card_images/{pngCodes[3]}.png")
            self.card3Button.show()

            self.card4Button.hide()
            self.card4Button.pixmap = QPixmap(f"GUI/card_images/{pngCodes[4]}.png")
            self.card4Button.show()

            self.confirm = True

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
