def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#PPrincipal
numerosprimers=0
b=[]
for num in range(1, 101):
    if es_primo(num):
        b.append(num)
        numerosprimers+=1
print("Hi ha {} números primers i són {}".format(numerosprimers, b))
