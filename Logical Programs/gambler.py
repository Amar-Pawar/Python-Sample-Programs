'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-29
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-29
@Title : To get win and loose percent for gambler placing bets
/**********************************************************************************
'''
import random

def gambler():
    """
    Description:
        This function takes stakes and goal for gambler as input and
        runs till he reaches his goal or looses all his money and
        calculates its number of wins, losses, total bet numbers and
        win percent and losing percent.     
    """
    # initializing variables
    BET_AMOUNT = 1
    WIN = 0
    LOSE = 0
    TOTAL_PLAYS = 0
    
    try:
        # taking input for stakes and goal amount
        GOAL = int(input("Enter a goal amount: "))
        STAKE = int(input("Enter initial stake amount: "))
    except Exception as e:
        print("Please enter correct input")
        gambler()
        return
    # using while loop to loop till given condition is met
    while(STAKE != GOAL) or (STAKE != 0):
        bets = random.randint(0,1)
        if (bets == 0):
            STAKE = STAKE - BET_AMOUNT
            # counting number of losses
            LOSE+=1
            print(f"Number of times bet lost {LOSE}")
            print(f"Bet lost!!, Now gambler has {STAKE} stakes")
            if (STAKE == 0):
                print("GAMBLER HAS LOST ALL HIS MONEY!!!")
                break
        else:
            STAKE = STAKE + BET_AMOUNT
            # counting number of wins
            WIN+=1
            print(f"Number of times bet won {WIN}")
            print(f"Bet won!!, Now gambler has {STAKE} stakes")
            if (STAKE == 200):
                print("GAMBLER HAS REEACHED HIS GOAL!!!!!")
                break
        # counting total number of plays
        TOTAL_PLAYS+=1
        print("Total number of times gambler played: ", TOTAL_PLAYS+1)
    # calculate win percent
    WIN_PERCENT = (WIN/TOTAL_PLAYS)*100
    print(f"Win percent are {round(WIN_PERCENT, 2)}")
    # calculate loose percent
    LOSE_PERCENT = (LOSE/TOTAL_PLAYS)*100
    print(f"Lose percent are {round(LOSE_PERCENT, 2)}")

gambler()
