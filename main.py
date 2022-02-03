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

#変数初期化
my_deck=["W","U","B","R","G"]*10
your_deck=["W","U","B","R","G"]*10

random.shuffle(my_deck)
random.shuffle(your_deck)

my_hand=[]
your_hand=[]

my_GY=[]
yourGY=[]

#戦場
my_BF=[]
your_BF=[]

my_victory=False
turn_counter=1

victory_list=["W","U","B","R","G"]

########################################
#######################################
#########################################


#main
#初手ドロー
for i in range (0,5):
    my_hand.append(my_deck.pop(0))

#your
for i in range (0,5):
    your_hand.append(your_deck.pop(0))


while not my_victory:
    print("*************************************")
    print(f"<{turn_counter} Turn>")
    
    #1ドロー
    my_hand.append(my_deck.pop(0))
    
    #盤面整理
    my_hand.sort()
    my_GY.sort()
    my_BF.sort()
    #print(f"BattleField{my_BF}\nGY{my_GY}\n\nHand{my_hand}\n")
    #print(f"BattleField{your_BF}\nGY{yourGY}\n\nHand{your_hand}\n")

    print(f"[Your]    \nBattleField{your_BF}\nGY{yourGY}\nHand{your_hand}\n")

    print("==================")
    #print(f"[Your] BattleField{your_BF}\n")
    print(f"[ My ]        \nBattleField{my_BF}\nGY{my_GY}\nHand{my_hand}\n")        
    
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
