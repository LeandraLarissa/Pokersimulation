from random import randint
print()
print("*********")
print("P O K E R")
print("*********")
#starting hand categories
excellentsuited =[[12, 12], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [12, 11], [12, 10], [12, 9], [12, 8], [11, 10], [11, 9], [11, 8], [10, 9], [10, 8], [9, 8], [9, 7], [8, 7]]
goodsuited =[[3, 3], [4, 4], [12, 4], [12, 5], [12, 6], [12, 7], [10, 7], [11, 7], [7, 6], [8, 6], [9, 6], [10, 6]]
okaysuited =[[0, 0], [1, 1], [2, 2], [12, 0], [12, 1], [12, 2], [12, 3], [11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [6, 5], [7, 5], [8, 5], [9, 5], [5, 4], [6, 4], [7, 4], [4, 3], [5, 3], [3, 2]]
fouldsuited =[]

excellent =[[12, 8], [12, 9], [12, 10], [12, 11], [11, 9], [11, 10]]
good =[[9, 8], [10, 8], [11, 8], [10, 9]]
okay =[[12, 5], [12, 6], [12, 7], [8, 7], [9, 7], [10, 7], [11, 7], [7, 6], [8, 6], [9, 6], [6, 5], [7, 5]]
fold =[]
#creation of a game
round = 0
stack = 2000
smallblind = 100
pot = 0

def validation(name, color):
    value = 0

    if name[0]+3 == name[3]: #if it is a order
        if name[0]+4 == name[4]:
            #straight
            value += 5 + name[4]/100
        if name[4] == 13 and name[0]== 0:
            #straight with ass
            value += 5+ name[4]/100

    if color[0] == color[1] == color[2] == color[3] == color[4]: #if it is the same color
        # sorted
        if 5 < value > 5.13:
            #straight flush
            value += 4
        if value == 5.13:
            #royal flush
            value += 5
        else:
            #flush
            value += 6 + name[4]/100
    
    else: # making it dependend because straight and pairs is possible but should not be validaded, pairs
        name.reverse() #von hoch zu tief
        i = 0
        highestcard = name[0]/100
        while i < (len(name)-1):
            quant = name.count(name[i]) 
            if  quant > 1:#quant for quantity
                for y in range(quant):
                    name.remove(name[i])
                i = -1
                if quant == 2:
                    if value == 4:
                        value += 3
                    if value == 2:
                        value += 1
                    if value == 0:
                        value += 2

                if quant == 3:
                    if value == 2:
                        value += 5
                    if value == 0:
                        value += 4


                if quant == 4:
                    value += 8 
            i += 1      
        value += highestcard     
                
    return value

while stack > 200 and round < 7:
    round += 1
    print("round", round)
    hand = []
    #Erstellen eines Kartendecks
    karten = []
    for i in range (0,52):
        karten.append(i)
    #Karten verteilen
    for i in range (0,2):
        n=randint(0,(51 - i))
        hand.append(karten[n])
        karten.pop(n)
    #Aufteilen der Hand in farbe und zahl
    kartenfarben = ["Herz", "Karo", "Pik", "Kreuz"]
    kartennamen =[2,3,4,5,6,7,8,9,10,"Junge","Dame","König","Ass"]

    handname = []
    handfarbe = []
    for i in range (0,2):
        handname.append(hand[i]%13)
        handfarbe.append(hand[i]//13)
    hand = []
    handname.sort(reverse=True)

    #ask if want to play
    if round % 2 == 0: # every second turn the player has to pay the bilnd
        stack -= 200
        pot += 200
    print("stack",stack)    
    if handfarbe[0] == handfarbe[1]:
        if handname in excellentsuited or handname in goodsuited:
            pot += stack
            stack = 0
            print("all-in")
    else:
        if handname in excellent or handname in good:
            pot += stack
            stack = 0
            print("all-in")

    #distribute the remaining 3 cards
    for i in range (0,3):
        n=randint(0,(49 - i))
        hand.append(karten[n])
        karten.pop(n)
    
    for i in range (0,3):
        handname.append(hand[i]%13)
        handfarbe.append(hand[i]//13)
    handname.sort()
    #determine the winner
    print("pot",pot)
    if validation(handname, handfarbe) > 2 and stack == 0:
        stack += pot
    pot = 0

print (stack, round)
