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

def slice(string):

    result = []

    collector = ""
    operator = ""

    parentDeepness = 0 #Out

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

    print(result)



def main():
    tasks = " 3 + 1 -  4 /     9"
    tasks = "3 - (1 + (3 + (1 -1) + 3)) - 4 + 88.3 - 2 + (3 + 3 -1) - 3"
    tasks = tasks.replace(" ", "")
    print(tasks)
    slice(tasks)


if __name__ == '__main__':
    main()
