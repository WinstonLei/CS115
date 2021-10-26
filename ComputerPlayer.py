from pigPlayer import PigPlayer

class ComputerPlayer(PigPlayer):


    def __init__(self, owner, name, target=20):
        PigPlayer.__init__(self, owner, name)
        self.targetPointsPerRound = target

    def wantsHandOver(self):
        '''Return boolean if the AI wants to end the round based on target'''
        if self.roundScore >= self.targetPointsPerRound:
            return bool(True)
        else:
            return bool(False)
        
    def is_human(self):
        return False
