quantidade_de_numero = int(input("quantos numeros você que: "))
quantidade_par = 0
quantidade_impar = 0
for numeros_pedidos in range(1,quantidade_de_numero):
    if numeros_pedidos % 2 == 0:
        quantidade_par = quantidade_par + 1 
    else:
        quantidade_impar = quantidade_par + 1

print(f"A quantidade de par é {quantidade_par} é a de impar é {quantidade_impar} ")