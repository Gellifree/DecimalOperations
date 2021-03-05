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
    direction = "in"

    isItInParent = False
    print("Kapott felvágandó szöveg: ", string)
    for char in string:
        if(char == "("):
            isItInParent = True
            direction = "in"


        if(char == ")"):
            direction = "out"
            isItInParent = False
        if(isItInParent == False):
            if(direction == "out"):
                number += char
                result.append(number.replace(" ", ""))
                direction = "undefined"
                number = ""

            if(char != ")"):
                if(sc.isItOperator(char) == True):
                    if(number.strip() == "" and direction != "undefined"):
                        result.append(0)
                    else:
                        if(number.strip() != ""):
                            result.append(float(number.replace(" ", "")))
                    number = ""
                    result.append(char)
                else:
                    number += char
        else:
            number += char



    if(number.strip() == "" and direction != "undefined"):
        result.append(0)
    else:
        if(number.strip() != ""):
            result.append(float(number.replace(" ", "")))
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

def dissolveParent(list):
    print("Kapott feladat: ",list)
    list = slice(list)
    print("Szeletelt lista: ", list)
    inParent = ""
    index = 0
    for element in list:
        if type(element) is str:
            if(element[0] == "("):
                for i in range(1, len(element)-1):
                    inParent += element[i]
                print("inParent: ", inParent)
                result = calculate(inParent)

                print(result)

                print("korai lista: ", list)
                del list[index]

                list.insert(index, result)
                print("Új lista: ", list)
        index += 1


def calculate(tasks):
    sTasks = tasks
    taskList = []
    taskList = slice(tasks)
    print(taskList)
    while(len(sTasks) > 1):
        print("Feladatok: ",taskList)
        operationDone = primaryOperation(taskList)
        calculationResult = connect(taskList[operationDone -1], taskList[operationDone + 1], taskList[operationDone])
        print("Részeredmény: ", calculationResult)
        del taskList[operationDone-1:operationDone+2]
        taskList.insert(operationDone-1, calculationResult)
        sTasks = taskList
    return calculationResult


def main():
    task = "(3 + 3) -2 * (3 * 1) - 1 * (3 / 3) - (2 - 4)"
    #task = "2 * 2 + 2 - 8"
    #task = input("Add meg az elvégezendő műveletet: ")
    #calculate(task)
    print(slice(task))

if __name__ == '__main__':
    main()
