def canvi(l,m,n):
    print("1) {}{} \n {}".format(l, m, n))
    l='Adéu, '
    m='José Luis'
    n='Que vagi bé'
    print("2) {}{} \n {}".format(l, m, n))
    return l,m,n
#Programa principal
a="hola, "
b="Ramis. "
c="Com estàs?"
print("El valor de la variable abans de canviar és: {}{}\n {}".format(a, b, c))
a,b,c=canvi(a, b, c)
print("El valor de la variable després de canviar és: {}{}\n {}".format(a, b, c))


"""
def intercanvi(a,b):
    return b,a
x='a'
y='b'
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y = intercanvi(x,y)
print("Després de l'intercanvi, el valor d'x és {} i el valor d'y és {}".format(x,y))

def major(x,y)
    if x>y:
        return x
    else:
        return y
a = int (input("Intro el 1r número: "))
b = int (input("Intro el 2n número: "))
c = int (input("Intro el 3r número: "))
print("El major de {} i {} és {}".format(a,b,c))

def intercanvi(pepito,juanito):
    return juanito,pepito

#x='a'
#y='b'