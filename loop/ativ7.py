numero = int(input("qual numero você quer fatorar: "))
aux = numero
i = numero
while i > 1 :
    i -= 1

    numero = numero * i

    
print(f"a fatorial de {aux} é {numero}")