from random import randint
#poker simulation without cards and only 3 players
ss1 = 200
ss2 = 200
bs1 = 800

pot = []

rss1 = 0
rss2 = 0

def pss1():
    if randint(1,3) > 1: #possible outcome 1,2 or 3
        return True
    else:
        return False

def pss2():
    if randint(1,3) > 2:
        return True
    else:
        return False

def pbs():
    if randint(1,3) > 2:
        return True
    else:
        return False

#while ss1 > 0 or ss2 > 0:
for i in range (4):
    if pss1(): 
        pot.append(ss1)
        if pss2():
            pot.append(ss2)
        if pbs():
            pot.append(bs1)
    if pss2(): 
        pot.append(ss2)
    if pbs(): 
        pot.append(bs1)

    pot.sort() #aufsteigend
    print(pot)
    bet = pot[0]
    for i in range (len(pot)):
        pot[i] -= bet
    print(pot)


    