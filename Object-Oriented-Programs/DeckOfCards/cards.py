'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-2
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-2
@Title : Deck of Cards
/**********************************************************************************
'''
import random

class DeckOfCards:
    # creating a constructor
    def __init__(self):
        pass

    def cards(self):
        """
        Description:
            This function generates random numbers for suit and rank of card and stores in list.
        """
        suit = ("Clubs", "Diamonds", "Hearts", "Spades")
        rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        # creating a list
        card_list = []
        # using while loop till the condition of 36 cards is reached
        while len(card_list) < 36:
            # for loop for 9 cards which to be distributed to each player
            for i in range(0, 9):
                # generating random number for rank
                random_rank = random.randint(0, 12)
                # generating random number for suit
                random_suit = random.randint(0, 3)
                rank_val = rank[random_rank]
                suit_val = suit[random_suit]

                rank_val = rank_val + "-" + suit_val

                if rank_val not in card_list:
                    if len(card_list) != 36:
                        card_list.append(rank_val)

        row = 4
        column = 9
        # using list comprehension to loop through rows and colums
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0

        for i in range(row):
            for j in range(column):
                two_d_array[i][j] = card_list[index]
                index += 1

        for i in range(len(two_d_array)):
            player_id = i+1
            print("player "+str(player_id)+": ", two_d_array[i])

card_spread = DeckOfCards()
card_spread.cards()

