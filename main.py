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

def main():
    task = input("Add meg a kifejezést: ")
    print(slice(task))

if __name__ == '__main__':
    main()
