import language
import menu
import utils

def showMainMenu() -> None:
    print(language.LANGUAGE["mainMenuWelcome"])
    print(language.LANGUAGE["mainMenuOpt1"])
    print(language.LANGUAGE["mainMenuOpt2"])
    print(language.LANGUAGE["mainMenuOpt3"])
    print(language.LANGUAGE["mainMenuOpt4"])
    print()

def showTable(matrix:list) -> None:
    try:
        menu.formatString("   0  1  2  3  4  5  ", "-", False)

        for i, row in enumerate(matrix):
            rowNumber = (i-len(matrix)) + 1

            if(rowNumber < 0):
                rowNumber = -rowNumber

            print(f"{rowNumber}| ", end="")
            for column in row:
                print(f"{column}  ", end="")
            print()
        print()
    except Exception as e:
        utils.errorPrint(f"[{e}] in menu.showTable()")

def showWinner(player:str) -> None:
    print(("\n")*2 + language.LANGUAGE["winner"].replace("X", player))

def newGame() -> None:
    try:
        if utils.validateStringOption(language.LANGUAGE["newMatch"]):
            print(language.LANGUAGE["startingNewMatch"])
            return True
        else:
            if utils.validateStringOption(language.LANGUAGE["backToMainMenu"]):
                print("\n"*10)
                mainMenu()
            else:
                print()
                exitGame()
    except Exception as e:
        errorPrint(f"[{e}] in menu.newGame()")

def exitGame() -> None:
    print(language.LANGUAGE["thank"])
    print(language.LANGUAGE["author"])

def formatString(string:str, sign="#", space=True) -> None:
    cover = sign*len(string)

    print(f"\n{cover}")
    print(string)
    print(cover)

    if(space):
        print("\n"*2)

def showMatchesRecords(matches:object) -> int:
    """
        Gets:
            matches = actual matches record

        Prints all matches records
        Return last match number
    """
    try:
        for matchNumber in matches:
            print(f"{language.LANGUAGE['match']} {matchNumber}: {matches[matchNumber]['date']}")
        print()

        return matchNumber
    except Exception as e:
        utils.errorPrint(f"[{e}] in menu.showMatchesRecords()")

#Main program
if __name__ == "__main__":
    pass