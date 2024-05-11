import language
import menu

def validateStringOption(msg:str) -> bool:
    """
        Gets a msg to print and ask for a "s", "n" or "y" input

        Returns True if input is equal to "s" or "y", else False 
    """
    try:
        opt = input(f"{msg} {language.LANGUAGE['checkString']}: ").lower()

        while not (opt == "s" or opt == "n" or opt == "y"):
            menu.formatString(language.LANGUAGE['stringError'])
            opt = input(f"{msg} {language.LANGUAGE['checkString']}: ").lower()

        return (opt == "s" or opt == "y")
    except Exception as e:
        errorPrint(f"[{e}] in utils.validateOption()")

def validateIntOption(minValue:int, maxValue:int, msg:str, player="0", matrix=[]) -> int: 
    """
        Gets: 
            minValue and maxValue to ask a new int input value between those values
            msg to print
            player and matrix as optionals just for matrix.addCoin() or storage.loadMatchesRecords()

        Returns chosen value
    """
    try:
        while True:
            try:
                if(player in ["1", "2"]): #If player, some value was sent
                    msg = msg.replace("X", player)

                opt = int(input(msg))
                assert minValue<=opt<=maxValue
                break
            except AssertionError:
                error = language.LANGUAGE['intErrorBetween'].replace("X", str(minValue)).replace("Y", str(maxValue))
                menu.formatString(error, space=False)

            except ValueError:
                menu.formatString(language.LANGUAGE['intError'], space=False)

            if(player in ["1", "2"]):
                menu.showTable(matrix)
            elif(player == "-1"):
                menu.showMatchesRecords(matrix)

        return opt
    except Exception as e:
        errorPrint(f"[{e}] in utils.validateIntOption()")

def errorPrint(msg:str) -> None:
    RESET_FONT_COLOR = "\033[0m"

    print("\033[91m" + f"[Error] {msg}" + RESET_FONT_COLOR)

def winnerPrint(char:str) -> None:
    ...

#Main program
if __name__ == "__main__":
    pass