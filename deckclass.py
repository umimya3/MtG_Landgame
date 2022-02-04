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

        
class Player:

    hand=[]
    GY=[]
    BF=[]
    Exile=[]
    life=20
    name=""
    
    def __init__(self,name):
    #変数初期化
        self.name=name
        #手札・墓地・戦場・除外
        """
        hand=[]
        GY=[]
        BF=[]
        Exile=[]
        Life=20
        """
        #name=""
        pass
        
    def show_name(self):
        print(f"myname is {self.name}")
    
    def hand_add(self,card):
        self.hand=(self.hand).append(card)
        
        #gain or loss
    def life_loss(self,dmg):
        self.life = self.life-(dmg)
        print(f"Life is  {self.life}")
        
    def life_gain(self,dmg):
        self.life = self.life+(dmg)
        print(f"Life is  {self.life}")        
        
        
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
