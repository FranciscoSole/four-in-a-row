import utils 

ENGLISH = {
    "mainError": "There was a critical error, the game will shudown. Contact with Francisco Solé to fix it.",
    "mainMenuWelcome": "Welcome to 4 in a row!\n",
    "mainMenuOpt1": "1) New game",
    "mainMenuOpt2": "2) Records",
    "mainMenuOpt3": "3) Change language",
    "mainMenuOpt4": "4) Exit",
    "selectCoinPos": "Player X, insert a coin or use -1 to go back to the main menu: ",
    "winner": "Congratz player number X, you won!",
    "fullTable": "Game ended, you tied! The game table is full.",
    "newMatch": "Do you want to play a new match?",
    "startingNewMatch": "Starting a new match...",
    "backToMainMenu": "Do you want to go back to the main menu?",
    "goingBack": "Okay, going back to the main menu...",
    "thank": "Thank you for playing!",
    "author": "Created by Francisco Solé",
    "checkString": "Y/N",
    "stringError": "#   Error: only Y and N are valid options.    #",
    "intChoose": "Choose an option: ",
    "intError": "#   Error: only numbers are valid answers in this question.   #",
    "intErrorBetween": "#   Error: choose a number between X and Y.   #",
    "matchSelection": "Choose a match number to see or -1 to go back to the main menu: ",
    "matchRecordsDoesntExist": "#   Error: there isn't any log.   #",
    "matchWinner": "Won by Player X",
    "wantToSeeAnotherMatch": "Do you want to see another match record?",
    "match": "Match"
}

ESPANOL = {
    "mainError": "Hubo un error crítico y se cortará la ejecución. Contactate con Francisco Solé para arreglarlo.",
    "mainMenuWelcome": "¡Bienvenido/a al 4 en raya!\n",
    "mainMenuOpt1": "1) Jugar",
    "mainMenuOpt2": "2) Historial",
    "mainMenuOpt3": "3) Cambiar idioma",
    "mainMenuOpt4": "4) Salir",
    "selectCoinPos": "Jugador X, ingrese una ficha o -1 para volver al menu principal: ",
    "winner": "Felicidades jugador X, ¡ganaste!",
    "fullTable": "Partida terminada, ¡empataron! El tablero se llenó.",
    "newMatch": "¿Desea jugar otra partida?",
    "startingNewMatch": "Comenzando nueva partida...",
    "backToMainMenu": "¿Desea volver al menu principal?",
    "goingBack": "Okay, volviendo al menu principal...",
    "thank": "¡Gracias por jugar!",
    "author": "Autor: Francisco Solé",
    "checkString": "S/N",
    "stringError": "#   Error: las opciones solo pueden ser S o N.   #",
    "intChoose": "Ingrese una opción: ",
    "intError": "#   Error: solo puede ingresar números.   #",
    "intErrorBetween": "#   Error: solo puede elegir las opciones del X al Y.   #",
    "matchSelection": "Ingrese la partida que quiera ver o -1 para volver al menu principal: ",
    "matchRecordsDoesntExist": "#   Error: no hay ningún registro de partida.   #",
    "matchWinner": "Ganador: Jugador X",
    "wantToSeeAnotherMatch": "¿Desea ver alguna otra partida del historial?",
    "match": "Partida"
}

def chooseLanguage() -> None:
    """
        Ask for a language and create a global variable named "LANGUAGE" with all messages in the chosen language
    """
    try:
        msg = "[ENG] Hi, which language do you prefer to play?\n[ESP] Hola, ¿con qué idioma preferís jugar?\n"
        cover = "#"*54
        print(cover)
        opt = input(f"{msg}ESP/ENG: ").lower()

        while not (opt == "esp" or opt == "eng"):
            print()
            print(cover)
            print("#   Error: only ESP or ENG are valid options.        #")
            print("#   Error: las opciones solo pueden ser ESP o ENG.   #")
            print(cover)
            print()
            opt = input(f"{msg}ESP/ENG: ").lower()

        global LANGUAGE
        if(opt == "esp"):
            LANGUAGE = ESPANOL
        else:
            LANGUAGE = ENGLISH
        
        print(cover)
        print()
        
    except Exception as e:
        utils.errorPrint(f"[{e}] in language.chooseLanguage()")

#Main program
if __name__ == "__main__":
    pass