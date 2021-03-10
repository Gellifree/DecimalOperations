#!/usr/bin/python3.8

# MADE BY
# Kovács Norbert - mfw.kovacs.norbert@gmail.com
#  _____      _ _ _  __
# |  __ \    | | (_)/ _|
# | |  \/ ___| | |_| |_ _ __ ___  ___
# | | __ / _ \ | | |  _| '__/ _ \/ _ \
# | |_\ \  __/ | | | | | | |  __/  __/
#  \____/\___|_|_|_|_| |_|  \___|\___|

import menu, solver

slr = solver.Solver()

def main():
    tasks = "3 / (6* -1)"
    tasks = slr.clear(tasks)
    print("Kapott feladat: ", tasks)
    result = slr.disolve(tasks)
    print("Végeredmény:", result)



if __name__ == '__main__':
    main()
