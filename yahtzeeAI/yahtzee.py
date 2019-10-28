import random

initialState = [0, False]

class State:
    points = 0
    hasBeenUsed = False

yahtzeeChoices = {
    "aces": State(),
    "twos": State(),
    "threes": State(),
    "fours": State(),
    "fives": State(),
    "sixes": State(),
    "threeOfAKind": State(),
    "fourOfAKind": State(),
    "fullHouse": State(),
    "smallStraight": State(),
    "largeStraight": State(),
    "yahtzee": State(),
    "chance": State()
}

class YahtzeeTopScore:
    aces = initialState
    twos = initialState
    threes = initialState
    fours = initialState
    fives = initialState
    sixes = initialState
    bonus = 0
    def getTotal(self):
        return 0

class YahtzeeLowerScore:
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

# class YahtzeeScore:
#     topScore = yahtzeeTopScore()
#     lowerScore = yahtzeeLowerScore()
#     def getTotal(self)
#         return topScore.getTotal() + lowerScore.getTotal()

class YahtzeeScore:
    def hasGameFinished(self):
        for key in yahtzeeChoices:
            if (yahtzeeChoices[key].hasBeenUsed == False):
                return False
        return True
    
    # def getPossibleChoices():
    #     i = 0

def RollDice(numDice):
    diceMinimum = 1
    diceMaximum = 6
    diceRolls = []
    for x in range(numDice):
        diceRolls.append(random.randint(diceMinimum, diceMaximum))
    return diceRolls

def GetPossibleResults():
    maxNumberOfChoices = 13
    possibleChoices = []
    # for x in range(maxNumberOfChoices):
    #     if ()


# def ChooseResult(rolledDiceResult):
#     # TODO: Create algorithm to choose the correct score
#     # Choose Random Result
#     # 13
#     numberOfPossibleResults = 13
#     randomResult = random.randint(1, numberOfPossibleResults)
#     if (randomResult == 1):

        



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


# Testing
def hasGameFinishedTest_InitialState():
    yahtzeeScore = YahtzeeScore()
    hasGameFinished = yahtzeeScore.hasGameFinished()
    if (hasGameFinished):
        print('hasGameFinishedTest_InitialState Failed')
    else:
        print('hasGameFinishedTest_InitialState Passed')

for x in range(5):
  print(random.randint(1,6))
print('Hello world from Yahtzee analyzer')

hasGameFinishedTest_InitialState()