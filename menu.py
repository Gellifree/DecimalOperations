class MenuDrawer:
    def draw(self, elements):
        index = 0
        for element in elements:
            if(element == "Kilépés"):
                print("    [Q] {}".format(element))
            else:
                print("    [{}] {}".format(index, element))
            index += 1
        print()
        answer = input(" >> ")

        try:
            answer = int(answer)
            if(answer >= 0 and answer < len(elements)):
                if(elements[answer] == "Kilépés"):
                    return -1
                return answer
                # Normal answer between array indexes
            else:
                print("  >> Nem adhatsz meg ilyen opciót! <<")
                return -2
                #Errorcode = -2 (Over or under indexing)
        except:
            if(answer == "Q" or answer == "q"):
                return -1
                #Exitcode = -1 (Exiting)
            else:
                print("  >> A kérés értelmezhetetlen! <<")
                return -3
                #Errorcode = -3 (unidentified command)
