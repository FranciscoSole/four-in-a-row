import language
import menu
import time
import utils

def saveMatch(matrix: list, player:str) -> None:
    try:
        log = open("matches.txt", "at") #Opens the records file
        log.write(time.asctime() + ";") #Get actual time

        for row in matrix:
            log.write("".join(row) + ";") #Adds all matrix rows
        log.write(player+"\n") #And the winner as the last character
    except FileNotFoundError as e:
        utils.errorPrint(f"[{e}] in storage.saveMatch(). File wasn't created.")
    except OSError as e:
        utils.errorPrint(f"[{e}] in storage.saveMatch().")
    finally:
        try:
            log.close()
        except NameError:
            pass

def loadMatchesRecords(matches = {}):
    try:
        if not(matches):
            matches = getMatchesRecords()
        
        if(matches):
            matchNumber = menu.showMatchesRecords(matches)
            option = utils.validateIntOption(-1, matchNumber, language.LANGUAGE["matchSelection"], "-1", matches)

            if(option == -1):
                return
            else:
                menu.showTable(matches[option]["data"])
                print(language.LANGUAGE["matchWinner"].replace("X", matches[option]["winner"]))

                if(utils.validateStringOption(language.LANGUAGE["wantToSeeAnotherMatch"])):
                    print()
                    return loadMatchesRecords(matches)
        
        return len(matches) >= 1
    except Exception as e:
        utils.errorPrint(f"[{e}] in storage.loadMatchesRecords().")

def getMatchesRecords() -> object:
    """
        Try to open match records file and create an object with the matches info
        
        Return this matchesObject
    """
    matchesObject = {}

    while True:
        try:
            logFile = open("matches.txt", "rt")

            for matchNumber, match in enumerate(logFile):
                array = []
                match = match.strip("\n").split(";")

                for index in range(1, len(match) - 1):
                    array.append(match[index])
                
                matchesObject[matchNumber] = {
                    "date": match[0],
                    "data": array,
                    "winner": match[-1]
                }

            break
        except FileNotFoundError as e:
            menu.formatString(language.LANGUAGE['matchRecordsDoesntExist'], space=False)
            break
        except OSError as mnsj:
            utils.errorPrint(f"[{e}] in storage.getMatchesRecords().")
        finally:
            try:
                log.close()
            except NameError:
                pass
    
    return matchesObject

#Main program
if __name__ == "__main__":
    pass