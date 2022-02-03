#220202 deck部分のclass化

import random

class Deck:

    
    def __init__(self,deck_size):
    #変数初期化
        symbol=["W","U","B","R","G"]
        self.deck=symbol*int(deck_size/5)

    def card_shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        #print("********************:")
        drawcard=(self.deck).pop(0)
        print(f"draw card is {drawcard}")
        #print(drawcard)
        return(drawcard)
    
    def show_all(self):
        print(self.deck)
    
    def card_Sort(self):
        (self.deck).sort()
    
    def card_count(self):
        #データがどれだけあるか
        print(f"deck size is {len(self.deck)}")
        #配列の要素数のマックス
        #print(len(self.deck)-1)

########################################
#main

myDeck = Deck(50)
myDeck.show_all()
myDeck.card_shuffle()
myDeck.show_all()
myDeck.card_count()

card=myDeck.draw()
print(card)

myDeck.show_all()
myDeck.card_count()
