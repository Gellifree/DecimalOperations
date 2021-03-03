class SyntaxChecker():
    def __init__(self):
        self.operatorList = ["+", "-", "*", "/"]


    def isItOperator(self, char):
        for i in range(len(self.operatorList)):
            if(char == self.operatorList[i]):
                return True
        return False

    def isItValidTask(self, taskList):
        if(self.isItOperator(taskList[0]) == True):
            return -1
            #Az első elem nem szám, hanem operátor (pl.: - 2 + 1)
