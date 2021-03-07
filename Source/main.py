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

    for char in string:
        if(char == "("):
            parentDeepness += 1
        if(char == ")"):
            parentDeepness -= 1

        if(sc.isItOperator(char) == False and parentDeepness == 0):
            collector += char
            if(char == string[-1]):
                result.append(collector)
        elif(sc.isItOperator(char) == True and parentDeepness == 0):
            result.append(collector)
            collector = ""
            operator = char
            result.append(operator)
        elif(parentDeepness > -1):
            collector += char

    return result

def disolve(taskList):
    for task in taskList:
        if(sc.isItInParent(task) == True):
            newTask = task[1:-1]
            print("inTask: ", newTask)
            disolve(slice(newTask))
        else:
            print("calculated!!: ",calculate(task))
            #ez még nemjo

def calculate(taskList):
    return -1

def main():
    tasks = " 3 + 1 -  4 /     9"
    tasks = "3 - (1 + (3 + (1 -1) + 3)) - 4 + 88.3 - 2 + (3 + 3 -1) - 3"
    tasks = tasks.replace(" ", "")
    print(tasks)
    disolve(slice(tasks))


if __name__ == '__main__':
    main()
