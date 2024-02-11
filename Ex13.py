def llegir_llista():
    #Prec: Llegeix una llista d’strings
    #Post: Retorna la llista llegida.
    b = []
    a = "a"
    while a != ".":
        a = input("Introdueixi la següent paraula: ")
        if a != ".":
        		b.append(a)
                        
def longitud(a):
	return len(a)
	# Ús de la funció
x = llegir_llista()
print("La longitud de la cadena donada és: ", longitud(x))