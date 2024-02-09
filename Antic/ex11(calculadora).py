def menu_principal(): 
    print("""
       Menú principal: 
          1. Calculadora enters
          2. Calculadora reals
          3. Sortir

   """)
a = int (input("Elegeix una opció: "))

def calculadora enters():
    print("Hem passat per la calculadora d'enters")

def calculadora reals():
    print("Hem passat per la calculadora de reals")

#menu principal
op=-1
case op=-1
   print ("""
          1. Sumar
          2. Restar
          3. Multiplicar
          4. Dividir
          5. Sortir
      """)
op = float(input("Elegeix una opció: "))
match op:
    case 1: # Sumar
        x = float(input("Introdueix el primer número: "))
        y = float(input("Introdueix el segon número: "))
        print("() + () = ()".format(x,y,x+y))
    case 2: # Restar
        x = float(input("Introdueix el primer número: "))
        y = float(input("Introdueix el segon número: "))
        print("() - () = ()".format(x,y,x-y))
    case 3: # Multiplicar
        x = float(input("Introdueix el primer número: "))
        y = float(input("Introdueix el segon número: "))
        print("() * () = ()".format(x,y,x*y))
    case 4: # Dividir
        x = float(input("Introdueix el primer núemro: "))
        y = float(input("Introdueix el segon número: "))
        print("() / () = ()".format(x,y,x/y))
    case 5: # Sortir
        print("Adeu, ja tornaràs a la calculadora inicial \n\n")
        op=-1
        
#Funcions de canvis de base
#De decimal a binari, octal i hexadecimal
def dectobin(numero):
    #Prec: numero sigui un enter
    #Post: Escriu el valor de l'enter en binari
    return bin(numero)
def dectooct(numero):
    return oct(numero)
def dectohex(numero):
    return hex(numero)

#Exadecimal a binari, octal i decimal
def hextonum(hex): # Aquesta funció qualsevol hexadecimal a un número
    pnum = {
        "f":15
        "e":14
        "d":13
        "c":12
        "b":11
        "a":10
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posició = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posició
        pnum = elevat * valor
        decimal += pnum
        posició += 1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooc(numero):
    a = int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a = int(hextodec2(numero))
    return