import language
import menu
import storage
import utils
from random import randint

def createMatrix() -> list:
    """
        Generates and returns a comprehension matrix 
    """
    try:
        return [["." for _ in range(6)] for _ in range(7)]
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.createMatrix()")

def gameTable() -> int:
    try:
        matrix = createMatrix()
        player = str(randint(1, 2)) #Start as random player
        coins = 0 #Set a counter
        winner = False
        mustReturn = -1 #Used in main.main(). If mustReturn == -1 -> program will go back to the main menu, but if it's 0, it will create another match
        toDo = ""

        while not winner:
            player = "1" if player == "2" else "2" #Switches actual turn
            menu.showTable(matrix) #Shows actual match table
            position = selectCoinPosition(player, matrix) #Get where must to be added the coin or if some player wants to go back to the main menu

            if(position != -1): #If the player doesn't want to go to the main menu
                if insertCoin(matrix, position, player): #If the coin was added properly
                    coins += 1 #Add one coin to the counter
                    
                    if(coins >= 7): #Start checking after 7 moves just because since it some player could win
                        winner = checkWinner(matrix, player)

                        if((winner) or (coins >= 42 and not winner)): #If actual player won or match table is full
                            menu.showTable(matrix)
                            
                            if(winner):
                                print(language.LANGUAGE["winner"].replace("X", player))
                            else:
                                print(language.LANGUAGE["fullTable"])

                            storage.saveMatch(matrix, player) #Saves actual match

                            if(utils.validateStringOption(language.LANGUAGE["newMatch"])):
                                mustReturn = 0
                            else:
                                print(language.LANGUAGE["goingBack"])
            else:
                print("\n")
                break
        
        print("#"*54)
        print()
        return mustReturn
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.gameTable()")

def selectCoinPosition(player:str, matrix:list) -> int:
    """
        Gets: 
            player = actual player to validate if want to insert a coin between columns numer 0 and 5, or go back to the main menu
            matrix = just for printing if user joins a bad answer

        Returns chosen int value 
    """
    try:
        return utils.validateIntOption(-1, 5, language.LANGUAGE["selectCoinPos"], player, matrix)
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.selectCoinPosition()")

def insertCoin(matrix:list, pos:int, player:str) -> bool:
    """
        Try to add a coin in the match table

        Gets:
            matrix = actual matrix
            pos = desired column position
            player = actual player
    """
    try:
        maxHeight = 6
        added = False

        while maxHeight >= 0:
            if matrix[maxHeight][pos] in ["1", "2"]: #If actual row is occupied
                maxHeight -= 1 #Try again with the previous row
            else:
                matrix[maxHeight][pos] = player 
                added = True
                break
                
        return added
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.insertCoin()")

def checkWinner(matrix: list, player:str) -> bool:
    """
        Check if the player won in any possible way

        Return True if it
    """
    try:
        if(checkVertical(matrix, player)):
            return True
        
        if(checkHorizontal(matrix, player)):
            return True

        if(checkDiagonals(matrix, player)):
            return True

        return False
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.checkWinner()")

def checkVertical(matrix: list, player:str) -> bool:
    """
        Gets:
            matrix = actual matrix
            player = actual player
        
        Firstly checks if actual value and the value 3 rows ahead are equal, then checks between those rows also
        Return True if all of them are equals
    """
    try:
        winner = False

        for column in range(6): #For all columns
            for row in range(4): #And just in the first 3 rows (for efficiency) of each
                if((matrix[row][column] == player) and (matrix[row+3][column] == player)): #Only check start and end at first for efficiency
                    if((matrix[row+1][column] == player) and (matrix[row+2][column] == player)): #Check between
                        winner = True
                        break #Ends rows' for
            if(winner): #If true, ends columns' for
                break

        return winner
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.checkVertical()")

def checkHorizontal(matrix: list, player: str) -> bool:
    """
        Gets:
            matrix = actual matrix
            player = actual player
        
        Firstly checks if actual value and the value 3 columns ahead are equals, then checks between those columns also
        Return True if all of them are equals
    """
    try:
        winner = False

        for row in range(7): #For all rows
            for column in range(3): #And just in the first 3 columns (for efficiency) of each
                if((matrix[row][column] == player) and (matrix[row][column+3] == player)): #Only check start and end at first for efficiency
                    if((matrix[row][column+1] == player) and (matrix[row][column+2] == player)): #Check between
                        winner = True
                        break #Ends columns' for
            if(winner): #If true, ends rows' for
                break

        return winner
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.checkHorizontal()")

def checkDiagonals(matrix: list, player: str) -> bool:
    """
        Gets:
            matrix = actual matrix
            player = actual player
        
        Firstly checks if actual value and the value in 3 columns and 3 rows ahead are equals or
        if last row value and the value 3 columns ahead and 3 rows before are equals, then checks between those columns also

        Return True if all of them (in right or left way) are equals
    """
    try:
        winner = False
        length = len(matrix[0]) - 1
        checkMatrix = reverseMatrix(matrix)

        for column in range(3): #For all column
            for row in range(4): #And just in the first 3 rows (for efficiency) of each
                check = ""
                #Only check start and end at first for efficiency
                if((checkMatrix[row][column] == player) and (checkMatrix[row+3][column+3] == player)):
                    check = "right"
                elif((checkMatrix[row][length] == player) and (checkMatrix[row+3][length-3] == player)):
                    check = "left"

                if(check): #If some coincidence was found
                    if( 
                        ((check == "right") and ((checkMatrix[row+1][column+1] == player) and (checkMatrix[row+2][column+2] == player))) or
                        ((check == "left") and ((checkMatrix[row+1][length-1] == player) and (checkMatrix[row+2][length-2] == player)))
                    ): #Check between
                        winner = True
                        break #Ends rows' for
            if(winner): #If true, ends columns' for
                break

        return winner
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.checkHorizontal()")

def reverseMatrix(matrix: list) -> list:
    """
        Gets:
            matrix: actual matrix
        
        Creates and returns a reversed matrix copy 
    """
    try:
        return [row for row in matrix[::-1]]
    except Exception as e:
        utils.errorPrint(f"[{e}] in matrix.reverseMatrix()")

#Main program
if __name__ == "__main__":
    pass