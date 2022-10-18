def ejercicio1():
  lista = ["P", "t"] 
  lista.append("h")
  lista.append("o")
  lista.append("n")
  lista.insert(1, "y")
  print("lista = ", lista)
  assert "".join(lista) == "Python"
