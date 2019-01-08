def doble(x):
    return x+x


lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)

listaDobles1 = map(doble, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)