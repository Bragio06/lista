quant_numeros = int(input("Me quantos numeros você que: "))
numeros = []

for i in range(0,quant_numeros):
    numeros.append(int(input("digite os numeros : ")))
maior = 0    
for m in numeros:
    if m > maior:
        maior = m    
print(f"O maior valor na lista é {maior}")        