import random

wallet = 0


def addToWallet():
    global wallet
    wallet = int(input("How much would you like in your wallet? "))


def firstRollDice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print([die1], [die2])
    if die1 + die2 == 7 or die1 + die2 == 11:
        print("You win!")
        return "win"
    elif die1 + die2 == 2 or die1 + die2 == 3 or die1 + die2 == 12:
        print("You lose...")
        return "lose"
    else:
        return die1 + die2


def secondRollDice(point):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print([die1], [die2])
    if die1 + die2 == 7:
        print("You lose...")
        return "lose"
    elif die1 + die2 == point:
        print("You win!")
        return "win"


def playOneRound():
    global wallet
    print("You have", wallet, "in your wallet.")
    bet = int(input("How much would you like to bet? "))
    while bet > wallet:
        print("You do not have enough money in your wallet.")
        bet = int(input("How much would you like to bet? "))
    point = firstRollDice()
    if point == "win":
        wallet = wallet + bet
    elif point == "lose":
        wallet = wallet - bet
    elif point != "win" and point != "lose":
        newpoint = secondRollDice(point)
        while newpoint != "win" and newpoint != "lose":
            newpoint = secondRollDice(point)
        if newpoint == "win":
            wallet = wallet + bet
        elif newpoint == "lose":
            wallet = wallet - bet


def playGame():
    addToWallet()
    answer = input("Would you like to start playing? (y/n)").lower()
    while answer == "y" and wallet > 0:
        playOneRound()
        if wallet == 0:
            print("You have no more money.")
        else:
            answer = input("Would you like to play again? (y/n)").lower()


playGame()
