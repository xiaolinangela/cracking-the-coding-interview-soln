import random
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Dimonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Card:
    def __init__(self,s,v):
        self.suit = s
        self.value = v
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    def showHand(self):
        for card in self.hand:
            card.show()
    
    def score(self):
        score = 0
        for card in self.hand:
            score += card.value
        return print(score)

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    playerA = Player("Angela")
    playerA.draw(deck)
    playerA.draw(deck)
    playerA.showHand()
    playerA.score()