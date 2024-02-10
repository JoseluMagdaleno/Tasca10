def	menor_edat():
	edat = input("Introdueixi la seva edat: ")
	if (edat <18):
			print("Ets menor d’edat")
	else:
			print("Ets major d’edat")
		
	edat = input("Introdueixi la seva edat: ")
	if (edat <18):
		print("Ets menor d’edat")
	elif (edat >18):
		print("Ets major d’edat")
	else:
		print("Tens 18 anys") 
	
def major_edat():
	edat = input("Introdueixi la seva edat: ")
	if (edat <18):
		print("Ets menor d’edat")
	elif (edat >18):
		print("Ets major d’edat")
	else:
		print("Tens 18 anys")
		#Ús de la funció
		major_edat()