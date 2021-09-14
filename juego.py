from collections import deque
from tablero import tablero

turno = deque(["0","X"])
tablero = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]


def rotar_turno():
    turno.rotate()
    return turno[0]

def mostra_tablero():
    print("")
    for fila in tablero:
        print(fila)

def procesar_posicion(posicion):
    fila,columna = posicion.split(',')
    return [int(fila)-1, int(columna)-1]

def posicion_correcta(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False

def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador

def ha_ganado(j):
    if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
        return True
    elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
        return True
    elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
        return True
    elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
        return True
    elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
        return True
    elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
        return True

def empate():
    for columna in range(3):
        for fila in range(3):
            if tablero[columna][fila] == " ":
                return False
    return True  
        


def juego():
    mostra_tablero()
    jugador = rotar_turno()
    while True:
        posicion = input(f"Juega {jugador}, elige una posicion fila,columna de  1 a 3: ")
        if posicion == 'Salir':
            break;
        
        try:
            posicion_l = procesar_posicion(posicion)
        except:
            print(f"Error, posicion {posicion} no es valido")
        if posicion_correcta(posicion_l):
            #Posisicon vacia
            actualizar_tablero(posicion_l,jugador)
            mostra_tablero()
            if ha_ganado(jugador):
                #Comprueba si ya gano
                print(f"Jugador {jugador} ha ganado!!!")
                break
            elif empate():
                #comprueba si hay empate
                print("Los jugadores han empatado")
                break
            jugador = rotar_turno()
        else:
            #posicion ocupada
            print(f"Posicion {posicion} no es correcta")

juego()