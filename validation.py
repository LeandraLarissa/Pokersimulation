from random import randint
print()
print("*********")
print("P O K E R")
print("*********")
hand = []
#Erstellen eines Kartendecks
karten = []
for i in range (0,52):
    karten.append(i)
#Karten verteilen
for i in range (0,5):
    n=randint(0,(51 - i))
    hand.append(karten[n])
    karten.pop(n)
#Aufteilen der Hand in farbe und zahl
kartenfarben = ["Herz", "Karo", "Pik", "Kreuz"]
kartennamen =[2,3,4,5,6,7,8,9,10,"Junge","Dame","König","Ass"]

handname = []
handfarbe = []
for i in range (0,5):
    handname.append(hand[i]%13)
    handfarbe.append(hand[i]//13)
print(hand)
handname.sort()

#Erkennen der Kombination
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
print(handname, handfarbe)
print(validation(handname,handfarbe))   
