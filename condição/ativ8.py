numero_1= float(input("digite o primeiro numero: "))
numero_2 = float(input("digite o segundo numero: "))
numero_3 = float(input("digite terceiro numero: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"O numero {numero_1} é o maior")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"O numero {numero_2} é o maior")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(f"O numero {numero_3} é o maior")
else:
    print("tudo igual")    
