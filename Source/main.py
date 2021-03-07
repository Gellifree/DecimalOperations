#!/usr/bin/python3.8

# MADE BY
# Kovács Norbert - mfw.kovacs.norbert@gmail.com
#  _____      _ _ _  __
# |  __ \    | | (_)/ _|
# | |  \/ ___| | |_| |_ _ __ ___  ___
# | | __ / _ \ | | |  _| '__/ _ \/ _ \
# | |_\ \  __/ | | | | | | |  __/  __/
#  \____/\___|_|_|_|_| |_|  \___|\___|

import menu, operators, syntaxChecker

op = operators.Operators()
sc = syntaxChecker.SyntaxChecker()

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
            result.append(collector)
            collector = ""
            operator = char
            result.append(operator)
        elif(parentDeepness > -1):
            collector += char
        index += 1

    return result

def disolve(taskList):
    print("kapott lista: ", taskList)
    index = 0
    resultList = taskList
    for task in taskList:
        if(sc.isItInParent(task) == True):
            newTask = task[1:-1]
            print("inTask: ", newTask)
            slicedNewTask = slice(newTask)
            calculatedResult = 0
            if(containsParent(slicedNewTask) == False):
                calculatedResult = calculate(slicedNewTask)
                del resultList[index]
                resultList.insert(index, calculatedResult)

            else:
                disolve(slice(newTask))
        else:
            pass
            #resultList.append(task)
            #print("calculated!!: ",calculate(task))
            #ez még nemjo
        index += 1
    print(resultList)


def disolve_v2(taskList):
    print("kapott lista: ", taskList)

    result = []

def clean(string):
    return string.replace(" ", "")

def calculate(taskList):
    return "-1"

def main():
    tasks = " 3 + 1 -  4 /     9"
    tasks = "3 - (1 + (3 + 3))"
    #tasks = "3 + 3 - (6 / 6)"
    tasks = clean(task)
    disolve_v2(slice(tasks))


if __name__ == '__main__':
    main()
