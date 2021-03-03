#!/usr/bin/python3.8

# MADE BY
# Kovács Norbert - mfw.kovcs.norbert@gmail.com
#  _____      _ _ _  __
# |  __ \    | | (_)/ _|
# | |  \/ ___| | |_| |_ _ __ ___  ___
# | | __ / _ \ | | |  _| '__/ _ \/ _ \
# | |_\ \  __/ | | | | | | |  __/  __/
#  \____/\___|_|_|_|_| |_|  \___|\___|

import menu, operators, syntaxChecker

op = operators.Operators()
sc = syntaxChecker.SyntaxChecker()


def slice(string):
    result = []
    number = ""
    for char in string:
        if(sc.isItOperator(char) == True):
            result.append(float(number))
            number = ""
            result.append(char)
        else:
            number += char
    result.append(float(number))
    return result

def connect(a, b, operator):
    if(operator == "+"):
        return op.add(a,b)
    if(operator == "-"):
        return op.subtract(a,b)
    if(operator == "*"):
        return op.times(a,b)
    if(operator == "/"):
        return op.divine(a,b)

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


def calculate(tasks):
    sTasks = tasks
    taskList = []
    taskList = slice(tasks)
    while(len(sTasks) > 1):
        print("Feladatok: ",taskList)
        operationDone = primaryOperation(taskList)
        calculationResult = connect(taskList[operationDone -1], taskList[operationDone + 1], taskList[operationDone])
        print("Részeredmény: ", calculationResult)
        del taskList[operationDone-1:operationDone+2]
        taskList.insert(operationDone-1, calculationResult)
        sTasks = taskList


def main():
    task = "2 * 2 + 7 - 3 * 2 -1"
    calculate(task)

if __name__ == '__main__':
    main()
