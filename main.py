import numpy as np


def randomize():
    return np.random.randint(10, 30)


def comandos():
    com_1 = b'\x00\x00\x00\x00'
    com_2 = b'\x00\x00\xBB\x00'
    com_3 = b'\xBB\x00\x00'
    com_4 = b'\x00\xBB\x00'
    com_5 = b'\x00\x00\xBB'
    com_6 = b'\x00\xAA'
    com_7 = b'\xBB\x00'
    com_8 = b'\x00'
    com_9 = b'\xBB'

    lista = [com_1, com_2, com_3, com_4, com_5, com_6, com_7, com_8, com_9]

    lista_comandos = []

    n = randomize()

    while n > 0:
        random_command = np.random.randint(0, 8)
        lista_comandos.append(lista[random_command])
        n -= 1
