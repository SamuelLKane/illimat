import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap

from pydealer import Deck

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Five Card Draw")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        deck = Deck()
        deck.shuffle()
        hand = deck.deal(5)
        hand.sort()

        pngCodes = []
        for card in hand:
            pngCodes.append(f"{card.value[0]}{card.suit[0]}")

        layout = QHBoxLayout(self.central_widget)

        # Cards
        card0 = QLabel(self)
        card1 = QLabel(self)
        card2 = QLabel(self)
        card3 = QLabel(self)
        card4 = QLabel(self)


        card0.setPixmap(QPixmap(f"card_images/{pngCodes[0]}.png"))
        card1.setPixmap(QPixmap(f"card_images/{pngCodes[1]}.png"))
        card2.setPixmap(QPixmap(f"card_images/{pngCodes[2]}.png"))
        card3.setPixmap(QPixmap(f"card_images/{pngCodes[3]}.png"))
        card4.setPixmap(QPixmap(f"card_images/{pngCodes[4]}.png"))

        layout.addWidget(card0)
        layout.addWidget(card1)
        layout.addWidget(card2)
        layout.addWidget(card3)
        layout.addWidget(card4)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
