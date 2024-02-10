def gran(a, b, c):
    if (a>=b):
        if(a>=c):
            return a
    else:
        return c
    if (b>=c):
        return b
    else:
        return c
        #Ús de la funció 
    x = input("Introdueixi el primer número a comparar: ")
    y = input("Introdueixi el segon número a comparar: ")
    z = input("Introdueixi el tercer número a comparar: ")
    c = gran(x, y, z)
    print("El més gran és: ", c)
