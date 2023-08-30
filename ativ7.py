valor_de_x = float(input("digite uma coordenada x:"))
valor_de_y = float(input("digite uma coordenada y:"))

if valor_de_x > 0 and valor_de_y > 0 :
    print("O ponto tá no primeiro quadrante")
elif valor_de_x < 0 and valor_de_y > 0:
    print("O ponto tá no segundo quadrante")
elif valor_de_x < 0 and valor_de_y < 0:
    print("O ponto tá no terceiro  quadrante")
elif valor_de_x > 0 and valor_de_y < 0: 
    print("O ponto tá no quarto  quadrante")
else:
    print("O ponto tá no centro ")
