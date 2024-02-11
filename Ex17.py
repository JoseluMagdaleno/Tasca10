def es_palindrom(a):
    if a == a[::-1]:
        return True
    else:
        return False

    #Programa Principal
x = input("Introdueix una paraula per a veure si és palíndrom o no: ")
if es_palindrom(x):
	print("La paraula ", x, " a l'inrevés ", invertir(x), " és un palíndrom.")
else:
	print("La paraula ", x, " a l'inrevés ", invertir(x), " no és un palíndrom.")