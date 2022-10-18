def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    del lista[1]
    del lista[2]
    del lista[2]
    del lista[2]
    lista.remove("7")
    lista.remove("8")
    lista.remove("9")
    lista.append("6")
    print("lista = ", lista)
    assert lista == list(range(1, 6))