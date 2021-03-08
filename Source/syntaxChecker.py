class SyntaxChecker():
    def __init__(self):
        self.operatorList = ["+", "-", "*", "/"]

    def containsParent(self, taskList):
        for task in taskList:
            if(self.isItInParent(task) == True):
                return True
        return False

    def isItOperator(self, char):
        for i in range(len(self.operatorList)):
            if(char == self.operatorList[i]):
                return True
        return False

    def isItValidTask(self, taskList):
        pass

    def isItInParent(self, string):
        if(string[0] == "(" and string[-1] == ")"):
            return True
        return False
