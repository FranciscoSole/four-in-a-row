import time
import random

def create():
    return [[0 for _ in range(6)] for _ in range(7)]

def informacion(valor, matriz='', turno=1):
    if valor == "menu" or valor == "menu-prints":
        print("Bienvenido/a al 4 en raya\n".center(202))
        print("1) Jugar".center(192))
        print("2) Historial".center(196))
        print("3) Salir".center(192))
        print()
        if valor == "menu":
            opts(create())
    elif valor == "game":
        print(("\n"*6)+"0  1  2  3  4  5".rjust(109))
        print(("-"*16).rjust(109))
        for f in matriz:
            print("".rjust(91), end="")
            for c in f:
                print("%3d" %c, end="")
            print()
        print()
    elif valor == "win":
        print(("\n")*2+f"Felicidades jugador {turno}, ¡ganaste!".center(202))
    elif valor == "nuevaPartida":
        opt = input("¿Desea jugar otra partida? S/N: ".rjust(117))
        if choice(opt, "nuevaPartida") == "s":
            print("Comenzando nueva partida...".rjust(114))
            return True
        else:
            opt = input("¿Desea volver al menu principal? S/N: ".rjust(120))
            if choice(opt, "menu") == "s":
                print("\n"*10)
                informacion("menu")
            else:
                print()
                informacion("end")
    elif valor == "end":
        print("¡Gracias por jugar!".center(202))
        print("Autores: Grupo 4".center(201))
        
def opts(matriz):
    while True:
        try:
            opt = int(input("Ingrese una opción: ".rjust(111)))
            assert 1<=opt<=3
            break
        except AssertionError:
            print("\n"+("#"*57).center(205))
            print("#   Error: solo puede elegir las opciones del 1 al 3.   #".center(205))
            print(("#"*57).center(205)+("\n")*5)
            informacion("menu-prints")
        except ValueError:
            print("\n"+("#"*43).center(205))
            print("#   Error: solo puede ingresar números.   #".center(205))
            print(("#"*43).center(205)+("\n")*5)
            informacion("menu-prints")
            
    if opt == 1:
        print("\n"*2)
        main(matriz)
    elif opt == 2:
        cargarHistorial()
    elif opt == 3:
        informacion("end")
        
def main(matriz, fichas=0):
    turno = random.randint(1,2)
    while True:
        turno = 1 if turno == 2 else 2
        fichas += 1
        informacion("game", matriz)
        if insertarFicha(matriz, cargarFicha(matriz, turno), turno):
            if fichas > 6:
                if validar_vertical(matriz, turno) or validar_horizontal(matriz, turno) or validar_diag(matriz, turno) or validar_diag(matriz, turno, "izquierda"):
                    informacion("game", matriz)
                    informacion("win", '', turno)
                    guardar(matriz, turno)
                    if informacion("nuevaPartida"):
                        main(create())
                    break
        else:
            print("\n"*10)
            informacion("menu")
            break
                
def cargarFicha(matriz, turno):
    while True:
        try:
            pos = int(input(f"Jugador {turno}, ingrese una ficha o -1 para volver al menu principal: ".rjust(135)))
            assert -1<=pos<=5
            break
        except AssertionError:
            if pos == -1:
                break
            else:
                print("\n"+("#"*43).center(205))
                print("#   Error: ingrese una posición válida.   #".center(205))
                print(("#"*43).center(205))
                informacion("game", matriz)
        except ValueError:
            print("\n"+("#"*33).center(205))
            print("#   Error: ingrese un número.   #".center(205))
            print(("#"*33).center(205))
            informacion("game", matriz)
            
    return pos

def insertarFicha(matriz, pos, turno, vertical=6):
    if pos != -1:
        while vertical >= 0:
            if matriz[vertical][pos] == 1 or matriz[vertical][pos] == 2:
                vertical -= 1
            else:
                matriz[vertical][pos] = turno
                break
            
        return True

def validar_vertical(matriz, user, cant=0, fila=0, filaMinimo=0, columna=0):
    while cant != 4:
        fila -= 1
        if matriz[fila][columna] == user:
            cant += 1
        else:
            fila = filaMinimo
            cant = 0
            columna += 1
            if columna == len(matriz[fila]):
                columna = 0
                filaMinimo -= 1
                if -filaMinimo == 7:
                    break
            
    return True if cant == 4 else False

def validar_horizontal(matriz, user, cant=0, fila=-1, columna=0):
    while cant != 4:
        if matriz[fila].count(0) <= 2:
            if matriz[fila].count(user) >= 4 and not columna == len(matriz[fila]):
                if matriz[fila][columna] == user:
                    cant += 1
                else:
                    cant = 0
                columna += 1
            else:
                fila -= 1
                columna = cant = 0
        else:
            break
            
    return True if cant == 4 else False

def validar_diag(matriz, user, modo="derecha", cant=1, fila=-1, err=False):
    check = list(str(matriz[-1]).strip("[]").replace(", ", ""))
    fila, columna, check = magia(matriz, str(user), modo, check)
        
    if check != False:
        while cant != 4 and fila != "Error":
            if modo == "derecha":
                if matriz[fila][columna] == matriz[fila-1][columna+1]:
                    columna += 1
                    cant += 1
                    fila -= 1
                else:
                    err = True
            else:
                if matriz[fila][columna] == matriz[fila-1][columna-1]:
                    columna -= 1
                    cant += 1
                    fila -= 1
                else:
                    err = True
            if err:
                fila += cant - 1
                cant = 1
                fila, columna, check = magia(matriz, str(user), modo, check, fila)
                err = False
    
    return True if cant == 4 else False

def magia(matriz, user, modo, check, fila=-1, columna=0, posibilidad=False):
    while not posibilidad:
        if user in check:
            if modo == "derecha":
                columna = int(check.index(user))
            else:
                columna = buscarUltimo(check, user)
            check[columna] = "0"
            
            if (modo == "derecha" and columna <= 2) or (modo == "izquierda" and columna >= 3):
                posibilidad = True
        else:
            fila -= 1
            if not -fila == 5:
                check = list(str(matriz[fila]).strip("[]").replace(", ", ""))
            else:
                break
                
    if posibilidad:
        return fila, columna, check
    else:
        return "Error", None, False

def buscarUltimo(check, user):
    for columna in range(len(check) -1, -1, -1):
        if check[columna] == user:
            break

    return columna

def guardar(matriz, turno):
    while True:
        try:
            log = open("log.txt", "at")
            log.write(str(time.asctime())+";")
            for linea in matriz:
                log.write(str(linea).strip("[]").replace(", ", "")+";")
            log.write(str(turno)+"\n")
            break
        except FileNotFoundError as mnsj:
            print(mnsj)
        except OSError as mnsj:
            print(mnsj)
        finally:
            try:
                log.close()
            except NameError:
                pass

def cargarHistorial():
    while True:
        try:
            log = open("log.txt", "rt")
            partidas = [ ]
            for linea in log:
                partidas.append(linea.strip("\n").split(";")[0])
                
            n = seleccionarPartida(partidas, mostrarPartidas(partidas))
            if n == -1:
                break
            else:
                while n >= 0:
                    log.seek(0)
                    for i, linea in enumerate(log):
                        linea = linea.strip("\n").split(";")
                        if linea[0] == partidas[n]:
                            break
                        
                    imprimirPartida(linea)
                        
                    opt = input("¿Desean ver otra partida? S/N: ".rjust(117))  
                    if choice(opt, "partida").lower() == "s":
                        n = seleccionarPartida(partidas, mostrarPartidas(partidas))
                    else:
                        opt = input("¿Desean volver al menu principal? S/N: ".rjust(120))
                        if choice(opt, "menu").lower() == "s":
                            n = -1
                        else:
                            n = -2
            break
        except FileNotFoundError as mnsj:
            n = -3
            break
        except OSError as mnsj:
            print(mnsj)
        finally:
            try:
                log.close()
            except NameError:
                pass
    if n == -1:
        print("\n"*10)
        informacion("menu")
    else:
        print()
        if n == -2:
            informacion("end")
        else:
            print(("\n"*7) + ("#"*49).center(200))
            print("#   Error: no hay ningún registro de partida.   #".center(200))
            print(("#"*49).center(200) + ("\n"*3))
            informacion("menu")

def mostrarPartidas(partidas):
    print("\n"*11)
    for i, partida in enumerate(partidas):
        print(f"Partida {i} - {partida}".center(202))
    print()
    
    return i

def seleccionarPartida(partidas, i):
    while True:
        try:
            n = int(input("Ingrese la partida que quiera ver o -1 para volver al menu principal: ".rjust(135)))
            assert (0 <= n <= i) or n == -1
            break
        except ValueError:
            print(("\n"*10)+("#"*43).center(205))
            print("#   Error: solo puede ingresar números.   #".center(205))
            print(("#"*43).center(205))
            mostrarPartidas(partidas)
        except AssertionError:
            print(("\n"*8)+("#"*36).center(200))
            print("#   Error: la partida no existe.   #".center(200))
            print(("#"*36).center(200))
            mostrarPartidas(partidas)
                    
    return n

def imprimirPartida(linea):
    print(("\n"*2)+linea[0].rjust(113))
    print("\n"+" ".rjust(90)+"0  1  2  3  4  5".center(22))
    print(" ".rjust(91)+("-"*16).center(20))
    for fila in linea[1:8]:
        print("".rjust(91), end="")
        for c in fila:
            print("%3s" %c, end="")
        print()
    print("\n"+f"Ganador: {linea[8]}".rjust(107))

def choice(opt, modo):
    while not (opt.lower() == "s" or opt.lower() == "n"):
        print("\n"+("#"*50).center(202))
        print("#   Error: las opciones solo pueden ser S o N.   #".center(201))
        print(("#"*50).center(202)+"\n")
        if modo == "partida":
            opt = input("¿Desea ver otra partida? S/N: ".rjust(117))
        elif modo == "menu":
            opt = input("¿Desea volver al menu principal? S/N: ".rjust(120))
        else:
            opt = input("¿Desean jugar otra partida? S/N: ".rjust(117))
        
    return opt

#Programa principal
informacion("menu")