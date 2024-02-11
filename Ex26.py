def llegir_llista():
	#Prec: Llegeix una llista de números binaris
	#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
            a = input("Introdueixi el següent número binari: ")
        if a != ".":
        		b.append(a)

def bintodec (bin):
    return int(bin,2)
def llbintodec(llbin):
    lldec = []
    for e in llbin:
        lldec.append(bintodec(e))
    return lldec
#Programa principal
a = llegir_llista()
b = llbintodec(a)
for i, e in enumerate(b):
    print("El número binari : ", a[i], " es correspon amb el número decimal: ", e)
