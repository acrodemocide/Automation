import random

initialState = [0, False]

class yahtzeeTopScore:
    aces = initialState
    twos = initialState
    threes = initialState
    fours = initialState
    fives = initialState
    sixes = initialState
    bonus = 0
    def getTotal(self):
        return 0

class yahtzeeLowerScore:
    ThreeOfAKind = initialState
    FourOfAKind = initialState
    FullHouse = initialState
    SmallStraight = initialState
    LargeStraight = initialState
    Yahtzee = initialState
    Chance = initialState
    YahtzeeBonus = [
        initialState,
        initialState,
        initialState
    ]
    def getTotal(self):
        return 0

class yahtzeeScore:
    topScore = yahtzeeTopScore()
    lowerScore = yahtzeeLowerScore()
    def getTotal(self)
        return topScore.getTotal() + lowerScore.getTotal()

def RollDice(numDice):
    diceMinimum = 1
    diceMaximum = 6
    diceRolls = []
    for x in range(numDice):
        diceRolls.append(random.randint(diceMinimum, diceMaximum))
    return diceRolls

def ChoosePoints(rolledDiceResult):
    # TODO: Create algorithm to choose the correct score


def YahtzeeTurn():
    maxNumberOfDiceRolls = 3
    maxNumberOfKeptDice = 4
    maxNumberOfRolledDice = 5
    endResultDice = []
    for x in range(maxNumberOfDiceRolls):
        # TODO: Create algorithm to determine the best strategy here
        chosenNumberOfDiceToRoll = 5
        endResultDice = RollDice(chosenNumberOfDiceToRoll)
    # TODO: Create algorithm to determine the best choice for the dice.

for x in range(5):
  print(random.randint(1,6))
print('Hello world from Yahtzee analyzer')