#!/usr/bin/python3.8

# MADE BY
# Kovács Norbert - mfw.kovacs.norbert@gmail.com
#  _____      _ _ _  __
# |  __ \    | | (_)/ _|
# | |  \/ ___| | |_| |_ _ __ ___  ___
# | | __ / _ \ | | |  _| '__/ _ \/ _ \
# | |_\ \  __/ | | | | | | |  __/  __/
#  \____/\___|_|_|_|_| |_|  \___|\___|

import menu, operators, syntaxChecker, corrector

op = operators.Operators()
sc = syntaxChecker.SyntaxChecker()
cr = corrector.Corrector()

def containsParent(taskList):
    for task in taskList:
        if(sc.isItInParent(task) == True):
            return True
    return False

def slice(string):

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

        if(sc.isItOperator(char) == False and parentDeepness == 0):
            collector += char
            if(index == len(string) -1):
                result.append(collector)
        elif(sc.isItOperator(char) == True and parentDeepness == 0):
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
    result = cr.correctBrackets(result)
    return result

def clear(string):
    return string.replace(" ", "")

def disolve(task):
    index = 0
    task = slice(task)
    if(containsParent(task)):
        for t in task:
            if(sc.isItInParent(t)):
                t = t[1:-1]
                del task[index]
                task.insert(index,disolve(t))
            index += 1
        return calculateValue(task)
    else:
        return calculateValue(task)

def maximumSearch(list):
    max = -10
    index = 0
    for i in range(len(list)):
        if(list[i] > max):
            max = list[i]
            index = i

    return index

def primaryOperation(taskList):
    result = []
    for i in range(len(taskList)):
        if(sc.isItOperator(taskList[i]) == True):
            if(taskList[i] == "+" or taskList[i] == "-"):
                result.append(1)
            elif(taskList[i] == "*" or taskList[i] == "/"):
                result.append(2)
        else:
            result.append(-1)
    return maximumSearch(result)

def connect(a, b, operator):
    if(operator == "+"):
        return op.add(a,b)
    if(operator == "-"):
        return op.subtract(a,b)
    if(operator == "*"):
        return op.times(a,b)
    if(operator == "/"):
        return op.divine(a,b)

def calculateValue(tasks):
    if(len(tasks) == 1):
        return tasks[0]
    sTasks = tasks
    taskList = []
    taskList = tasks
    calculationResult = 0
    #print(taskList)
    while(len(sTasks) > 1):
        #print("Feladatok: ",taskList)
        operationDone = primaryOperation(taskList)
        calculationResult = connect(float(taskList[operationDone -1]), float(taskList[operationDone + 1]), taskList[operationDone])
        #print("Részeredmény: ", calculationResult)
        del taskList[operationDone-1:operationDone+2]
        taskList.insert(operationDone-1, calculationResult)
        sTasks = taskList
    return calculationResult


def main():
    tasks = "3 + 2 * 4 + -5"
    tasks = clear(tasks)
    print("Kapott feladat: ", tasks)
    result = disolve(tasks)
    print("Végeredmény:", result)



if __name__ == '__main__':
    main()
