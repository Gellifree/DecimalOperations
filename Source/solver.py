import operators, syntaxChecker, corrector

class Solver():
    def __init__(self):
        self.op = operators.Operators()
        self.sc = syntaxChecker.SyntaxChecker()
        self.cr = corrector.Corrector()


    def slice(self,string):

        result = []

        collector = ""
        operator = ""

        parentDeepness = 0 #0 - Out
        index = 0

        for char in string:
            if(char == "("):
                parentDeepness += 1
            if(char == ")"):
                parentDeepness -= 1

            if(self.sc.isItOperator(char) == False and parentDeepness == 0):
                collector += char
                if(index == len(string) -1):
                    result.append(collector)
            elif(self.sc.isItOperator(char) == True and parentDeepness == 0):
                if(collector == ''):
                    operator = char
                    collector = "(0" + char
                else:
                    result.append(collector)
                    collector = ""
                    operator = char
                    result.append(operator)
            elif(parentDeepness > -1):
                collector += char
            index += 1
        result = self.cr.correctBrackets(result)
        return result

    def clear(self, string):
        return string.replace(" ", "")

    def disolve(self, task):
        index = 0
        task = self.slice(task)
        if(self.sc.containsParent(task)):
            for t in task:
                if(self.sc.isItInParent(t)):
                    t = t[1:-1]
                    del task[index]
                    task.insert(index,self.disolve(t))
                index += 1
            return self.calculateValue(task)
        else:
            return self.calculateValue(task)

    def maximumSearch(self,list):
        max = -10
        index = 0
        for i in range(len(list)):
            if(list[i] > max):
                max = list[i]
                index = i

        return index

    def primaryOperation(self, taskList):
        result = []
        for i in range(len(taskList)):
            if(self.sc.isItOperator(taskList[i]) == True):
                if(taskList[i] == "+" or taskList[i] == "-"):
                    result.append(1)
                elif(taskList[i] == "*" or taskList[i] == "/"):
                    result.append(2)
            else:
                result.append(-1)
        return self.maximumSearch(result)

    def connect(self,a, b, operator):
        if(operator == "+"):
            return self.op.add(a,b)
        if(operator == "-"):
            return self.op.subtract(a,b)
        if(operator == "*"):
            return self.op.times(a,b)
        if(operator == "/"):
            return self.op.divine(a,b)

    def calculateValue(self,tasks):
        if(len(tasks) == 1):
            return tasks[0]
        sTasks = tasks
        taskList = []
        taskList = tasks
        calculationResult = 0
        #print(taskList)
        while(len(sTasks) > 1):
            #print("Feladatok: ",taskList)
            operationDone = self.primaryOperation(taskList)
            calculationResult = self.connect(float(taskList[operationDone -1]), float(taskList[operationDone + 1]), taskList[operationDone])
            #print("Részeredmény: ", calculationResult)
            del taskList[operationDone-1:operationDone+2]
            taskList.insert(operationDone-1, calculationResult)
            sTasks = taskList
        return calculationResult
