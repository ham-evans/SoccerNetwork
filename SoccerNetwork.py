import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Player:
    xLoc = 0
    yLoc = 0
    angle = 0
    speed = 0
    accelData = [0,0,0]
    momentum =0
    
    def __init__(self, position, team):
        self.team = team
        self.position = position
    
    def addAccel(self, val):
         self.accelData=self.accelData[1:]+[val]
         self.momentum = self.accelData[-1] - self.accelData[0]
          
        
class Team:     
    def __init__ (self, team):
        self.team = team
        self.players = []
        for i in range (1,12): 
            self.players.append(Player(i,self.team))
      
            
test = Team('woooo')
players = test.players

players[0].addAccel(5)
print(players[0].momentum)