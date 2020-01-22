import test
import random
# import settings


# ---- All const  ---- #
CARD_COLORS = ["pique" , "carreau" , "trèfle" , "coeur"]
CARD_VALUES = [0 , 1 , "2" , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13]


#  __________________________
# /  Init Cards with values  \ #
# \__________________________/


class Card:


    # ---- Cards init Attributes ---- #
    def __init__(self , color , value):

        self.color = color
        self.value = value

    # ---- Compare cards ---- #
    def __lt__(self , other):

        return self.value < other.value


#  __________________________________
# /  Link lists -> Class atrributes  \ #
# \__________________________________/

    def __str__(self):

        return '%s de %s' % (self.value , CARD_COLORS[self.color])
#  _________________________
# /         Init Deck        \ #
# \__________________________/


class Deck:


    # ---- Deck init Attributes ---- #
    def __init__(self):

        self.cards = []
        for color in range(4):
            for value in range(1 , 14):
                card = Card(color , value)
                self.cards.append(card)

    # ---- Render deck ---- #
    def __str__(self):

        render_deck = []
        for card in self.cards:
            render_deck.append(str(card))
        return '\n'.join(render_deck)

    # ---- Add / Pop / Shuffle and filter ---- #
    def pop_card(self):
        return self.cards.pop()
    
    def append_card(self, card):
        self.card.append(card)

    def shuffle_card(self):
        random.shuffle(self.cards)
        
    
if __name__ == "__main__":
    deck = Deck()
    print(deck)


#  ____________________________________
# /         Init HiLow function        \ #
# \____________________________________/


# class HiLow:

#     def __init__(self):

#         cpt = 0

#         for i in range ((CARD_VALUES[1:6])):
#             cpt = cpt + 1
#         for j in range((CARD_VALUES[7:10])): 
#             cpt = cpt
#         for k in range(len(CARD_VALUES[11:13])): 

        

#  ____________________________________
# /         Init Player function       \ #
# \____________________________________/


class Player:

    def __init__(self , hand , probability ):

        self.hand = [] 
        self.probability = probability

    