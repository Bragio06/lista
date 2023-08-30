lado_1 = int(input("Digite o valor do lado 1: "))
lado_2 = int(input("Digite o valor do lado 2: "))
lado_3 = int(input("Digite o valor do lado 3: "))

if lado_1 == lado_2 == lado_3:
    print("Equilátero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_3 == lado_2:
    print("Isósceles")
else:
    print("Escaleno")