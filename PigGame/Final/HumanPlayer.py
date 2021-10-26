from pigPlayer import PigPlayer


class HumanPlayer(PigPlayer):
    
    def wantsHandOver(self):
        '''Asks a human player if they want to play again'''
        
        print("\tYour current score: " + str(self.getCurrentScore()))
        print("\tRoll again? (yes or no)")
        if not self.wantsContinue(""):
            self.isPlayerTurn = False
        return self.isPlayerTurn

    def is_human(self):
        return True
