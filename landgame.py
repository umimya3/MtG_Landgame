#更新履歴
#220128 LandGame
#220202 CUIで雑に実装
#220203 pip8準拠でリファクタ

"""
220201 森　1ドロー　赤：ランダムに戦場の土地破壊　黒：ランダムに2ハンデス
       5色揃えば勝　まで
       対戦相手はツモ切りマシン
#1 平地　墓地のカード回収
#2 島　ピーピング/将来的にはFoW
#3 沼　相手が1枚選んで捨てる
#4 山　場のカード一枚破壊
#5 森　1ドロー
       
""" 

import random


#デッキクラス(デッキを触る処理はここ)
class Deck:

    
    #deck=[]
    
    def __init__(self,deck_size):
    #変数初期化
        symbol=["W","U","B","R","G"]
        self.deck=symbol*int(deck_size/5)
        self.card_shuffle()
        

    def card_shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        #print("********************:")
        drawcard=(self.deck).pop(0)
        #print(f"draw card is {drawcard}")
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

#プレイヤーとその場(デッキは除く)を管理するクラス
class Player:
    #クラス変数 これをもとにしたインスタンスすべてが同じ値を共有
    
    def __init__(self,name="Player01",hand=[],GY=[],BF=[],exile=[],life=20):
    #変数初期化
        #インスタンス変数(それぞれのインスタンスで固有の値)
        self.name=name
        self.hand=hand
        self.GY=GY
        self.BF=BF
        self.exile=exile
        self.life=life
        
    def show_all(self):
        (self.hand).sort
        (self.GY).sort
        (self.BF).sort
        (self.exile).sort
        print(f"{self.name}\nBattleField{self.BF}\nGY{self.GY}\nHand{self.hand}\n")

        
    def show_name(self):
        print(f"myname is {self.name}")
    
    def hand_add(self,card):
        #print("+++++++++")
        #print(self.hand)
        #print(card)
    
        (self.hand).append(card)
        
        #gain or loss
    def life_loss(self,dmg):
        self.life = self.life-(dmg)
        print(f"{self.name} life is  {self.life}")
        
    def life_gain(self,dmg):
        self.life = self.life+(dmg)
        print(f"{self.name} life is  {self.life}")  


####
#変数初期化
my_victory=False
turn_counter=1

victory_list=["W","U","B","R","G"]

########################################
#######################################
#########################################

my_deck   = Deck(50)
your_deck = Deck(50)

my_player   =Player(name="Tom",hand=[],GY=[],BF=[],exile=[],life=20)
your_player =Player(name="KEITH",hand=[],GY=[],BF=[],exile=[],life=20)

my_player.show_name()
your_player.show_name()


#main
#初手ドロー
for i in range (0,5):
    my_player.hand_add( my_deck.draw() )
    your_player.hand_add( your_deck.draw() )

print(your_player.hand)
print(my_player.hand)

#ゲーム開始
while not my_victory:
    print("*************************************")
    print(f"<{turn_counter} Turn>")
    
    #1ドロー
    my_player.hand_add( my_deck.draw() )
    
    #盤面整理
    my_player.show_all()
    your_player.show_all()
    exit()
    #どのカードを唱えるか(一文字だけとする)
    
    right_spell=False
    while(not right_spell):
        what_cast_spell=input(f"what's cast a spell?(W,U,B,R,G)")
        
        if what_cast_spell in my_hand:
            print("cast ok!")
            right_spell=True
        else:
            print("no cast!!!! choose another!!!!")

    #print(my_hand)
    cast_spell=my_hand.pop(my_hand.index(what_cast_spell))

    print(f"you cast {cast_spell} Spell!")
    my_BF.append(cast_spell)

    #castしたスペルの効果
    if "G" in cast_spell:        
        print(f"{cast_spell} effects 1 draw!!!!")
        my_hand.append(my_deck.pop(0))
    
    elif "R" in cast_spell:        
        
        #len(your_BF)
        
        if(len(your_BF)== 0):
            print("No broken (-_-)")
        
        else:
            print(f"{cast_spell} effects broken Land!!!!")
            target=random.randint(0,len(your_BF)-1 )
            your_BF.pop(target)

    elif "B" in cast_spell:        
        
        #len(your_BF)
        #精神腐敗(2ハンデス)
        for k in range(0,1):

            if len(your_hand)== 0:
                print("No broken (-_-)")
        
            else:
                print(f"{cast_spell} effects Hand destory!!!!")
                target=random.randint(0,len(your_hand)-1 )
                print(target)
                your_hand.pop(target)


    else:
        print(f"{cast_spell} effects noeffect(-_-)")  

    #勝利条件の確認
    #print("END of Turn")
    victory_counter=0
    for j in (victory_list):
        if j in my_BF:
            victory_counter=victory_counter+1

    #print(victory_counter)
    if victory_counter>4:
        print("My Victory!!!")
        my_victory=True
    else:
        victory_counter=0

    ######################################################################
    #EnemyTurn
    your_hand.append(your_deck.pop(0))
    #盤面整理
    your_hand.sort()
    yourGY.sort()
    your_BF.sort()
    #print(f"BattleField{your_BF}\nGY{yourGY}\n\nHand{your_hand}\n")
    
    #ツモ切りマシン
    target=0
    cast_spell=your_hand.pop(int(target))
    print(f"ENEMY cast {cast_spell} Spell!")
    your_BF.append(cast_spell)
#print(f"BattleField{my_BF}\nHand{my_hand}\nGY{my_GY}\n")
