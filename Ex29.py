def noms_que_comencen_per(llista,lletra):
	comptador = 0
	llnom= []
	for e in llista:
    	    if e[0]==lletra:
        	    llnom.append(e)

print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format("lletra", "comptador", "nom"))

def llegir_llista():
	#Prec: Llegeix una llista de paraules, en el nostre cas de noms
	#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
            a = input("Introdueixi el següent nom: ")
        if a != ".":
        	b.append(a)
    
#Programa principal
noms = llegir_llista()
noms_que_comencen_per(noms,"a")
