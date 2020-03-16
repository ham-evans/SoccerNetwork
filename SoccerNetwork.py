class Player:
    xLoc = 0
    yLoc = 0
    angle = 0
    speed = 0
    accelData = [0,0,0]
    
    def __init__(self, team=0):
        self.team = team
    
    def add(self, val):
         self.accelData=self.accelData[1:]+[val]
          
#    def momentum (self):
        

test = Player()

