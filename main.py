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
    result = {
        "value" : max,
        "index" : index
    }

    return result


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


def main():
    task = "2 + 2 - 2 * 3"
    #task = input("Add meg a kifejezést: ")
    taskList = slice(task)
    print(taskList)
    result = primaryOperation(taskList)

    print(connect(taskList[result["index"] -1], taskList[result["index"] + 1], taskList[result["index"]]))
    #for i in range(len(taskList)):
    #    if(sc.isItOperator(taskList[i]) == True):
    #        print(connect(taskList[i -1], taskList[i + 1], taskList[i]))

if __name__ == '__main__':
    main()
