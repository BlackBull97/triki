from typing import Tuple

coordenadas_del_tablero = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

def validar_entrada_input():
    entrada = ''

    while entrada != 'x' and entrada != 'o':
        entrada = input('\nelije una letra  entre "x" o "O" que quieres jugar: ')
        entrada = entrada.lower()
        if entrada == 'x':
            return 'x', 'o'
        elif entrada == 'o':
            return 'o', 'x'
        else:
            print('intenta utlizar x y o')


def pintar_tablero():
    print(coordenadas_del_tablero.get(1), '|', coordenadas_del_tablero.get(2), '|', coordenadas_del_tablero.get(3))
    print('-   -   -')
    print(coordenadas_del_tablero.get(4), '|', coordenadas_del_tablero.get(5), '|', coordenadas_del_tablero.get(6))
    print('-   -   -')
    print(coordenadas_del_tablero.get(7), '|', coordenadas_del_tablero.get(8), '|', coordenadas_del_tablero.get(9))


def turno_del_juego():
    print('\nelije la posicion en la que quieres jugar  ')
    posicion_del_tablero = ''

    while posicion_del_tablero not in coordenadas_del_tablero:
        try:
            posicion_del_tablero = int(input('aqui puedes poner numeros del 1 al 9 : '))
        except ValueError:
            print('valor incorrecto , ingresa un numero entre el 1 y el 9')
            continue

        if posicion_del_tablero in coordenadas_del_tablero:
            if coordenadas_del_tablero[posicion_del_tablero] == 'x' or coordenadas_del_tablero[posicion_del_tablero] == 'o':
                print('Ya no puedes remplazar esta posicion en el tablero ')
                return turno_del_juego()
            else:
                print('posicion disponible! ')
                return posicion_del_tablero


def reemplazar(entrada, posicion_del_tablero):
    coordenadas_del_tablero[posicion_del_tablero] = entrada


def verificar_finalizar_fin_de_juego():
    fin_de_juego = False
    matriz_verificadora = [
        [coordenadas_del_tablero.get(1), coordenadas_del_tablero.get(2), coordenadas_del_tablero.get(3)],
        [coordenadas_del_tablero.get(4), coordenadas_del_tablero.get(5), coordenadas_del_tablero.get(6)],
        [coordenadas_del_tablero.get(7), coordenadas_del_tablero.get(8), coordenadas_del_tablero.get(9)],
        [coordenadas_del_tablero.get(1), coordenadas_del_tablero.get(4), coordenadas_del_tablero.get(7)],
        [coordenadas_del_tablero.get(2), coordenadas_del_tablero.get(5), coordenadas_del_tablero.get(8)],
        [coordenadas_del_tablero.get(3), coordenadas_del_tablero.get(6), coordenadas_del_tablero.get(9)],
        [coordenadas_del_tablero.get(1), coordenadas_del_tablero.get(5), coordenadas_del_tablero.get(9)],
        [coordenadas_del_tablero.get(3), coordenadas_del_tablero.get(5), coordenadas_del_tablero.get(7)]]

    for lista in matriz_verificadora:
        if lista.count('x') == 3:
            print('el jugador |x| gana ')
            fin_de_juego = True
            if fin_de_juego == True:
                break
        elif lista.count('o') == 3:
            print('el jugador |o| gana ')
            fin_de_juego = True
            if fin_de_juego == True:
                break


    return fin_de_juego


def iniciar_juego():
    j1, j2 = validar_entrada_input()
    pintar_tablero()
    for n in coordenadas_del_tablero:
        if n % 2 != 0:
            jugador_actual = j1
            print('\nTurno del jugador 1')
        else:
            jugador_actual = j2
            print('\nTurno del jugador 2')
        posicion_del_tablero = turno_del_juego()
        reemplazar(jugador_actual, posicion_del_tablero)
        pintar_tablero()
        fin_de_juego = verificar_finalizar_fin_de_juego()

        if fin_de_juego:
            return 'juego finalizado'
    else:
        print('\nEsto es empate señores !')


iniciar_juego()