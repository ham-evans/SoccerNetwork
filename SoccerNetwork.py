import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Player:
    angle = 0
    speed = 0
    accelData = [0,0,0]
    momentum =0
    
    def __init__(self, position, team, xLoc, yLoc):
        self.team = team
        self.position = position
        self.loc = [xLoc, yLoc]
    
    def addAccel(self, val):
         self.accelData=self.accelData[1:]+[val]
         self.momentum = self.accelData[-1] - self.accelData[0]
          
        
class Team:     
    def __init__ (self, team):
        self.team = team
        self.players = []
        for i in range (1, 12):
            self.players.append(Player(i,self.team, i, 10))
      
test = Team('woooo')
players = test.players
#
#players[0].addAccel(5)
#print(players[0].momentum)
            

xs = []
ys = []
for i in range(0, len(players)):
    xs.append(players[i].loc[0] * i)
    ys.append(players[i].loc[1])

fig = plt.figure()
plt.xlim(0, 120)
plt.ylim(0, 75)
graph = plt.scatter(xs, ys, s=100)
numframes = 100
#fig, ax = plt.subplots(figsize=(5,3))
#fig.set(xlim=(0, 120), ylim=(0, 75))
#graph = ax.scatter(xs, ys, color='orange')
def add (a, b): 
    return a+b

def animate(i, xs, graph):
    xs = []
    ys = []
    for j in range(0, len(players)):
        xs.append(players[j].loc[0] * i)
        ys.append(players[j].loc[1] + i)
    graph.set_offsets(np.c_[xs,ys])
    return graph
    
anim = animation.FuncAnimation(fig, animate, frames=range(numframes), fargs=(xs, graph))
 
plt.draw()
plt.show()