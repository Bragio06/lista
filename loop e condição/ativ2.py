numeros_da_lista = []


while True:
    try:
        numero_da_lista = float(input("Insira um número (ou qualquer letra para parar): "))
        numeros_da_lista.append(numero_da_lista)
    except ValueError:
        break

# Verifica o menor valor na lista
menor_valor_da_lista = None
for num in numeros_da_lista:
    if menor_valor_da_lista is None or num < menor_valor_da_lista:
        menor_valor_da_lista = num

# Exibe o menor valor encontrado
if menor_valor_da_lista is not None:
    print(f"O menor valor na lista é: {menor_valor_da_lista}")
else:
    print("Nenhum número foi inserido.")