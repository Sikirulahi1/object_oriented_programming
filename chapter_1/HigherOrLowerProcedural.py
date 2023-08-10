# HigherOrLower
import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck

def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop one off the top of the deck and return
    return thisCard

# Pass in a deck of this function and return a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # copy the deck list
    random.shuffle(deckListOut) # shuffle the deck list
    return deckListOut # Return the deck list after shuffling
 
# Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)
        
score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    
    currentCardDict = getCard(gameDeckList)
    currentCardValue = currentCardDict['value']
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    
    print('Starting card is: ', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): # Play one game of this many cards
        
        answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l):')

        answer = answer.casefold() # Force lower case
        
        
        nextCardDict = getCard(gameDeckList)
        nextCardValue = currentCardDict['value']
        nextCardRank = currentCardDict['rank']
        nextCardSuit = currentCardDict['suit']
        
        print('Next card is: ', nextCardRank + ' of ' + nextCardSuit)
        
        
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right , it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15
        
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You got it right , it was lower')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15
            
        else:
            print('Incorrect choice !!')
        print('Your score is ' + str(score))
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue #don't need to change suit
        
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break
    
print('Ok bye')