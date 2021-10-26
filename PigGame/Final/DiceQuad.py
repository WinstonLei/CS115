from Die import Die

class DiceQuad():

    def __init__(self):
        '''Initilizes dieList as a list of 4 Die objects
            To create a die object, call Die()'''
        ob1 = Die()
        ob2 = Die()
        ob3 = Die()
        ob4 = Die()
        self.dieList = [ob1, ob2, ob3, ob4]

    def roll(self):
        '''Rolls all four dice in dieList'''
        for i in range(0, len(self.dieList)):
            self.dieList[i].roll()
        return self.dieList

    
    def num1s(self):
        '''return the number of ones rolled'''
        counter = 0
        for die in self.dieList:
            if die.getFaceValue() == 1:
                counter += 1
        return counter
    
    
    def getDiceTotal(self):
        '''return the sum of the dice'''
        total = 0
        for die in self.dieList:
            total += die.getFaceValue()
        return total

    def __str__(self):
        '''String representation of the dice roll'''
        s = "("+str(self.dieList[0])
        for x in range(1, len(self.dieList)):
            s = s+","+str(self.dieList[x])
        s = s+")"
        return s
