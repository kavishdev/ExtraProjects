import random
print("======== Hello lets play Uno! =============\n\n")
# for i in range(6):
    # print(i,end="Kavish \n")
NCardsPerPlayer=5
Nset=1
rcards= []
gcards=[]
bcards=[]
ycards=[]
UNOdeck=[] # Clean Fresh DECK packet
DIRECTION = 0 # clockwise direction , if DIRECTION=1, direction is anti-clockwise

NPLAYERS = 2
PLAYERS=[] # List of Player's Name
for p in range(NPLAYERS) :
    print("Enter Player %d Name " %(p+1), end= "" )
    pname = input()
    PLAYERS.append(pname)

PlayerCards={}
print("==== Welcome champions .. ",PLAYERS)





# Add numeric card 0-9
for card_no in range(10):
    rcards.append("r"+str(card_no))
    gcards.append("g"+str(card_no))
    bcards.append("b"+str(card_no))
    ycards.append("y"+str(card_no))

# Add Special cards of colors 
# '+' = 2+
# '<' = reverse game direction
# '#' = SKIP chance
specialcards=['+','<','#']
for spl in specialcards:
    rcards.append("r"+spl)
    gcards.append("g"+spl)
    bcards.append("b"+spl)
    ycards.append("y"+spl)

allcards = Nset*(rcards+gcards+bcards+ycards)
UNOdeck=allcards
tabledeck=[]
print("UNO Deck : %s" % UNOdeck )

# print("\nPlayer 1 Cards : ",allcards[0:NCardsPerPlayer])

random.shuffle(allcards)

print("Shuffled cards in Deck ",allcards)


for p in range (NPLAYERS):
    plcards = allcards[0:NCardsPerPlayer]
    PlayerCards=dict([(p,plcards)])
    print("Player 1 Cards : ",plcards)
    del allcards[0:NCardsPerPlayer]
    print("Remaining cards in Deck ",allcards)


print("Player 2 Cards : ", allcards[0:NCardsPerPlayer])
del allcards[0:NCardsPerPlayer]

print("All Player Cards ",PlayerCards)
# print("Remaining cards in Deck ",allcards)

# TAKE the topcard from the list and keep it on the TABLE deck (cards that are open)
topcard = allcards.pop(0) 
tabledeck.insert(0,topcard)

ClosedCards=allcards

# print("Card in front: ", topcard)
# putcard = input('Enter a card')
# print("You have put: ", putcard) 
# if putcard=topcard :



