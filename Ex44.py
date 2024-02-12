def  esta_ordenada(a):
	b = a.copy()
	c = a.copy()
	b.sort()
	c.sort(reverse=True)
	if a == b:
            print("La llista {} està ordenada ascendentment {}".format(a, b))
        elif a==c:
    	    print("La llista {} està ordenada descendentment {}".format(a, c))

def llegir_llista():
	#Prec: Llegeix una llista de números
    #Post: Retorna la llista llegida.
    a = "a"
    b = [] 
while a != ".":
    a = input("Introdueixi el següent número: ")
if a != ".":
    b.append(int(a))

#Pprincipal
a = llegir_llista()
esta_ordenada(a)
