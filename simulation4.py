#3 players, strategies with random componend, blinds change every 6th(every 5th in sim2)
#players have to pay blinds more often
#with these settings the achieved rounds during a 1000 trials from player 1 and player 2 are printed
from random import randint
print()
print("*********")
print("P O K E R")
print("*********")
#starting hand categories
superexcellentsuited =[[12, 12], [11, 11], [10, 10], [9, 9], [12, 11], [12, 10], [11, 10], [10, 9], [9, 8]]
excellentsuited =[[12, 12], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [12, 11], [12, 10], [12, 9], [12, 8], [11, 10], [11, 9], [11, 8], [10, 9], [10, 8], [9, 8], [9, 7], [8, 7]]
goodsuited =[[3, 3], [4, 4], [12, 4], [12, 5], [12, 6], [12, 7], [10, 7], [11, 7], [7, 6], [8, 6], [9, 6], [10, 6]]
okaysuited =[[0, 0], [1, 1], [2, 2], [12, 0], [12, 1], [12, 2], [12, 3], [11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [6, 5], [7, 5], [8, 5], [9, 5], [5, 4], [6, 4], [7, 4], [4, 3], [5, 3], [3, 2]]
fouldsuited =[]

excellent =[[12, 8], [12, 9], [12, 10], [12, 11], [11, 9], [11, 10]]
good =[[9, 8], [10, 8], [11, 8], [10, 9]]
okay =[[12, 5], [12, 6], [12, 7], [8, 7], [9, 7], [10, 7], [11, 7], [7, 6], [8, 6], [9, 6], [6, 5], [7, 5]]
fold =[]

#Values for the simulation
completedround = []
completedround2 = []
totalrounds = []



for i in range (1000):
    #creation of a game
    rounds = 0
    round = 0 
    round2 = 0
    stack = 500
    stack2 = 500
    smallblind = 25
    pot = 0
    bet = 0

    def strategy (name, color):
        if rounds > 6:
            if color[0] == color[1]:
                if name in superexcellentsuited and randint(1,4)== 2:
                    return True
            else:
                if name in excellent and randint(1,4)== 2:
                    return True

    def strategy2 (name, color):
        if color[0] == color[1]:
            if name in excellentsuited:
                return True
        elif randint(1,10) == 2:
            return True
        else:
            if name in excellent:
                return True

    def strategy3 (name, color):
        if color[0] == color[1]:
            if name in excellentsuited or name in goodsuited:
                return True
        elif randint(1,10) == 2:
            return True
        else:
            if name in excellent or name in good:
                return True


    def validation(name, color):
        value = 0
        if name[0]+3 == name[3]: #if it is a order
            if name[0]+4 == name[4]:
                #straight
                value += 5 + name[4]/100
            elif name[4] == 13 and name[0]== 0:
                #straight with ace
                value += 5+ name[4]/100

        if color[0] == color[1] == color[2] == color[3] == color[4]: #if it is the same color
            # sorted
            if 5 < value > 5.13:
                #straight flush
                value += 4
            elif value == 5.13:
                #royal flush
                value += 5
            else:
                #flush
                value += 6 + name[4]/100
        
        else: # making it dependend because straight and pairs is possible but should not be validaded, pairs
            name.reverse() #from high to low
            i = 0
            highestcard = name[0]/100
            while i < (len(name)-1):
                quant = name.count(name[i]) 
                if  quant > 1:#quantity
                    for y in range(quant):
                        name.remove(name[i])
                    i = -1
                    if quant == 2:
                        if value == 4:
                            value += 3
                        elif value == 2:
                            value += 1
                        elif value == 0:
                            value += 2

                    elif quant == 3:
                        if value == 2:
                            value += 5
                        elif value == 0:
                            value += 4


                    elif quant == 4:
                        value += 8 
                i += 1      
            value += highestcard     
                    
        return value

    def blinds(smallblind, rounds):
        if rounds % 6 == 0:
            if rounds // 6 <= 3:
                smallblind += 25
            else:
                smallblind += smallblind
        return smallblind

    while stack > 2*smallblind and stack2 > 2*smallblind and rounds < 50:
        rounds += 1
        hand = []
        hand2 = []
        hand3 = []
        communitycards = []
        communityname = []
        communitycolor =[]
        validations = 0
        #making a card deck
        karten = []
        for i in range (0,53):
            karten.append(i)
        #distributing cards
        for i in range (0,2):
            n=randint(0,(51 - 3*i))
            hand.append(karten[n])
            karten.pop(n)
            n=randint(0,(50-3*i))
            hand2.append(karten[n])
            karten.pop(n)
            n=randint(0,(49 - 3*i))
            hand3.append(karten[n])
            karten.pop(n)
        #spliting up the hand in color hand rank

        handname = []
        handfarbe = []
        handname2 = []
        handfarbe2 = []
        handname3 = []
        handfarbe3 = []
        
        for i in range (0,2):
            handname.append(hand[i]%13)
            handfarbe.append(hand[i]//13)
            handname2.append(hand2[i]%13)
            handfarbe2.append(hand2[i]//13)
            handname3.append(hand3[i]%13)
            handfarbe3.append(hand3[i]//13)
        hand = []
        hand2 = []
        hand3 = []
        handname.sort(reverse=True)
        handname2.sort(reverse=True)
        handname3.sort(reverse=True)
        #blinds
        if rounds % 3 == 0: # every fith turn the player has to pay the big bilnd
            stack -= 2* smallblind
        elif rounds % 3 == 1:
            stack2 -= 2* smallblind
            stack -= smallblind
        elif rounds % 3 == 2:
            stack2 -= smallblind
        pot += 3*smallblind
        
        for i in range (0,3):
                    n=randint(0,(41 - i))
                    communitycards.append(karten[n])
                    karten.pop(n)                
        for i in range (0,3):
            communityname.append(communitycards[i]%13)
            communitycolor.append(communitycards[i]//13)

        if strategy2(handname3, handfarbe3):
            hand3 += communitycards
            handname3 += communityname
            handfarbe3 += communitycolor
            handname3.sort()
            validations = validation(handname3, handfarbe3)

        #ask if want to play    
        if strategy(handname,handfarbe):
            hand += communitycards
            handname += communityname
            handfarbe += communitycolor
            handname.sort()
            validation1 = validation(handname,handfarbe)

            if strategy2(handname2, handfarbe2):
                if stack <= stack2:
                    bet += stack
                else:
                    bet += stack2
                pot += 2*bet
                stack2 -= bet
                stack -= bet
                #both play

                #remaining cards are uncovered 
                hand2 += communitycards
                handname2 += communityname
                handfarbe2 += communitycolor
                handname2.sort()
                validation2 = validation(handname2,handfarbe2) 
                #determine the winner
                
                if validations > 0:
                    pot += bet
                

                if validation1 > validation2 and validation1 > validations:
                    stack += pot
                elif validation1 < validation2 and validation2 > validations:
                    stack2 += pot

            else:
                bet += stack
                stack = 0
                if validations > 0:
                    pot += bet
                if validation1 > validations:
                    stack += pot
        else:
            if strategy2(handname2,handfarbe2):
                hand2 += communitycards
                handname2 += communityname
                handfarbe2 += communitycolor
                handname2.sort()
                validation2 = validation(handname2,handfarbe2) 
                bet += stack2
                stack2 = 0
                if validations > 0:
                    pot += bet
                if validation2 > validations:
                    stack2 += pot
        pot = 0
        bet = 0
        smallblind = blinds(smallblind, rounds)
    if stack < 2*smallblind+1 and stack2 > 2*smallblind: #if p1 ran out of chips but p2 didn't:
        round += rounds
        while stack2 > 2*smallblind and rounds < 50:
            rounds += 1
            hand2 = []
            hand3 = []
            communitycards = []
            communityname = []
            communitycolor =[]
            validations = 0
            #Erstellen eines Kartendecks
            karten = []
            for i in range (0,53):
                karten.append(i)
            #Karten verteilen
            for i in range (0,2):
                n=randint(0,(51-2*i))
                hand2.append(karten[n])
                karten.pop(n)
                n=randint(0,(50 - 2*i))
                hand3.append(karten[n])
                karten.pop(n)
               
            #Aufteilen der Hand in farbe und zahl

            handname2 = []
            handfarbe2 = []
            handname3 = []
            handfarbe3 = []
            for i in range (0,2):
                handname2.append(hand2[i]%13)
                handfarbe2.append(hand2[i]//13)
                handname3.append(hand3[i]%13)
                handfarbe3.append(hand3[i]//13)
            hand2 = []
            hand3 = []
            handname2.sort(reverse=True)
            handname3.sort(reverse=True)
            #blinds
            if rounds % 2 == 1:
                stack2 -= 2* smallblind
            elif rounds % 2 == 0:
                stack2 -= smallblind
            pot += 3*smallblind
        
            for i in range (0,3):
                n=randint(0,(41 - i))
                communitycards.append(karten[n])
                karten.pop(n)    
            for i in range (0,3):
                communityname.append(communitycards[i]%13)
                communitycolor.append(communitycards[i]//13)

            if strategy2(handname3, handfarbe3):
                hand3 += communitycards
                handname3 += communityname
                handfarbe3 += communitycolor
                handname3.sort()
                validations = validation(handname3, handfarbe3)

            #ask if want to play    
            if strategy2(handname2,handfarbe2):
                hand2 += communitycards
                handname2 += communityname
                handfarbe2 += communitycolor
                handname2.sort()
                validation2 = validation(handname2,handfarbe2) 
                bet += stack2
                stack2 = 0
                if validations > 0:
                    pot += bet
                if validation2 > validations:
                    stack2 += pot
                
            pot = 0
            bet = 0
            smallblind = blinds(smallblind, rounds)
        round2 += rounds
        
    elif stack2 < 2*smallblind+1 and stack > 2*smallblind: #elif the opposite
        round2 += rounds
        while stack > 2*smallblind and rounds < 50:
            rounds += 1
            hand = []
            hand3 = []
            communitycards = []
            communityname = []
            communitycolor =[]
            validations = 0
            #Erstellen eines Kartendecks
            karten = []
            for i in range (0,53):
                karten.append(i)
            #Karten verteilen
            for i in range (0,2):
                n=randint(0,(51-2*i))
                hand.append(karten[n])
                karten.pop(n)
                n=randint(0,(50 - 2*i))
                hand3.append(karten[n])
                karten.pop(n)
            #Aufteilen der Hand in farbe und zahl

            handname = []
            handfarbe = []
            handname3 = []
            handfarbe3 = []
            for i in range (0,2):
                handname.append(hand[i]%13)
                handfarbe.append(hand[i]//13)
                handname3.append(hand3[i]%13)
                handfarbe3.append(hand3[i]//13)
            hand = []
            hand3 = []
            handname.sort(reverse=True)
            handname3.sort(reverse=True)
            #blinds
            if rounds % 2 == 1:
                stack -= 2* smallblind
            elif rounds % 2 == 0:
                stack -= smallblind
            pot += 3*smallblind
        
            for i in range (0,3):
                n=randint(0,(41 - i))
                communitycards.append(karten[n])
                karten.pop(n)    
            for i in range (0,3):
                communityname.append(communitycards[i]%13)
                communitycolor.append(communitycards[i]//13)

            if strategy2(handname3, handfarbe3):
                hand3 += communitycards
                handname3 += communityname
                handfarbe3 += communitycolor
                handname3.sort()
                validations = validation(handname3, handfarbe3)

            #ask if want to play    
            if strategy(handname,handfarbe):
                hand += communitycards
                handname += communityname
                handfarbe += communitycolor
                handname.sort()
                validation1 = validation(handname,handfarbe) 
                bet += stack
                stack = 0
                if validations > 0:
                    pot += bet
                if validation1 > validations:
                    stack += pot
            pot = 0
            bet = 0
            smallblind = blinds(smallblind, rounds)
        round += rounds
    else:#if both ran out of money in the same round
        round += rounds
        round2 += rounds
    completedround.append(round)
    completedround2.append(round2)
for i in range (1,51):
    print(completedround.count(i),completedround2.count(i))

