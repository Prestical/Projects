import random
import time

players = []

landDict = {0:["A100",60,30,None],1:["A101",70,35,None],
            2:["B100",100,50,None],3:["B101",100,50,None],4:["B102",120,60,None],
            5:["C100",140,70,None],6:["C101",140,70,None],7:["C102",160,80,None],
            8:["D100",180,90,None],9:["D101",180,90,None],10:["D102",200,100,None],
            11:["E100",220,110,None],12:["E101",220,110,None],13:["E102",240,120,None],
            14:["F100",260,130,None],15:["F101",260,130,None],16:["F102",280,140,None],
            17:["G100",300,150,None],18:["G101",300,150,None],19:["G102",320,160,None],
            20:["H100",340,170,None],21:["H101",360,180,None]}

class Player():
   
    def __init__(self,name,money,ownLand,position,ownLands,past):
        self.name = name
        self.money = money
        self.ownLand = ownLand
        self.position = position
        self.ownLands = ownLands
        self.funds = []
        self.past = past
    
    def allOwnLands(self):
        self.funds.append(self.ownLands)
        return self.funds
    
    def __str__(self):
        return f"{self.name} {self.money} {self.ownLand} {self.position}"

def mainMenu():
    print("*"*58)
    print("\t\t\tWELCOME TO THE MONOPOLIE")
    print("*"*58)
    

def playerGenerator():
    pl = int(input("How many person will play the game ?: "))
    for i in range(pl):
        n = input(f"Player{i+1} enter your name: ")
        a = Player(n,1500,None,0,None,0)
        players.append(a)

def position(n):
    dice = random.randint(1,12)
    newPosition = n + dice
    if newPosition > 21 :
        return newPosition - 22
    else:
        return newPosition
    
def buyingLand(player,position):
    buy = input(f"\t{player.name} do you want to buy {landDict[position][0]} for {landDict[position][1]}$ ?(y/n):")
    if buy.lower() == "y":
        player.money -= landDict[position][1]
        landDict[position][3] = player.name
        print(f"\t{player.name} taked {landDict[position][0]} ")
    else:
        print("\tLand did not taken!!")

def checkMoney(playerMoney):
    if playerMoney < 0:
        return True

def showAllLands(player):
    player.funds = []
    print(f"\t\t\t{player.name} Own Lands")
    for v in landDict.values():
        if v[3] == player.name:
            player.ownLands = v[0]
            player.allOwnLands()
    print(f"\t{player.funds}")
    

def payRent(player,landPosition):
    a = 0
    for i in players:
        if landDict[landPosition][3] == i.name:
            print(f"\t{player.name} paid rent to {players[a].name}")
            player.money -= landDict[landPosition][2]
            players[a].money += landDict[landPosition][2]
            print(f"\t{player.name} has {player.money}$, {players[a].name} has {players[a].money}$")
        a += 1           

def winner():
    maxi = []
    for i in players:
        if i.money >= 0:
            maxi.append(len(i.funds))
    maxi.sort()
    for i in players:
        if len(i.funds) == maxi[-1]:
            print(f"Winner is {i.name}. Congratulations!! ")
        
def gameEnding(player): 
    check = []
    for v in landDict.values():
        check.append(v[3])
    if not None in check:
        print("\t\t\tGame Ended - There is not ownless land")
        winner()
        return True
    if checkMoney(player.money) == True:
        print(f"\t\t\tGame Ended - {player.name} go bankrupt.")
        winner()
        return True

def salary(player,past):
    if player.position < past:
        print(f"\t\t\t{player.name} got his salary +100$")
        player.money += 100
        


def midMenu(player):
    print("*"*58)
    print(f"\t\t\t{player.name} Plays ")
    salary(players[i],players[i].past)
    print(f"\t\t\tYour Money:{player.money}")
    
ending = False
mainMenu()     
playerGenerator()
while not ending:
    for i in range(len(players)):
        players[i].position = position(players[i].position)
        print(f"{players[i].name} position is {players[i].position} / Land: {landDict[players[i].position][0]}")
        midMenu(players[i])
        if landDict[players[i].position][3] == None:
            buyingLand(players[i],players[i].position)
            print(f"\t{players[i].name} has {players[i].money}$")
            showAllLands(players[i])
            time.sleep(.5)
        elif landDict[players[i].position][3] != players[i].name:
            payRent(players[i],players[i].position)
            time.sleep(.5)
        elif landDict[players[i].position][3] == players[i].name:
            print("\tYou are in your own land")
        print("*"*58)
        ending = gameEnding(players[i])
        players[i].past = players[i].position 
        if ending == True:
            break
        time.sleep(.5)