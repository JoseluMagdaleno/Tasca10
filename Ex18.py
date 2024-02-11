def llegir_llista():
    #Prec: Llegeix una llista d’elements
    #Post: Retorna la llista llegida.
    b = []
    a = "a"
    while a != ".":
        a = input("Introdueixi la següent paraula: ")
        if a != ".":
            b.append(a)
        else:
            return b

def superposicio(a, b):
	n = 0 #Indica quants elements hi ha en comú
	for e in a:
            n += b.count(e)
        if n>0:
            return [n, True]
        else:
            return  [0, False]

#Programa Principal
a = llegir_llista()
b = llegir_llista()
c,d = superposicio(a,b)
if (c==0):
	print("Les dues llistes no tenen cap element en comú.")
else:
	print("Les llistes tenen ", c, " elements en comú")