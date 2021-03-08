import syntaxChecker

class Corrector():
    def __init__(self):
        self.sc = syntaxChecker.SyntaxChecker()

    def correctBrackets(self,list):
        for i in range(len(list)):
            if(list[i][0] == "(" and list[i][-1] != ")"):
                list[i] += ')'
        return list
