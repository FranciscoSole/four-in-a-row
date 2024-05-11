import language
import matrix
import menu
import storage
import utils

def main(firstExec = True) -> None:
    try:
        if firstExec:
            language.chooseLanguage()

        menu.showMainMenu()
        option = utils.validateIntOption(1, 4, language.LANGUAGE["intChoose"])

        while(option != 4):
            if(option == 1): #If was selected start game
                game = matrix.gameTable()
                
                while (game == 0): #If it ended or some player wanted to came back
                    game = matrix.gameTable() #Create a new match
                
                if(game == -1): #If users want to go back to the main menu
                    main(False)
            elif(option == 2):
                if (storage.loadMatchesRecords()): #If log file exists print some style
                    print()
                    print("#"*54)
                
                print()
                menu.showMainMenu()
            else:
                main()

            option = utils.validateIntOption(1, 4, language.LANGUAGE["intChoose"])
        else:
            menu.exitGame()
            exit()
    
    except KeyboardInterrupt:
        menu.exitGame()
        exit()

    except Exception as e:
        utils.errorPrint(f"[{e}] in main.main()")
        utils.errorPrint(language.LANGUAGE["mainError"])

#Main program
if __name__ == "__main__":
    main()