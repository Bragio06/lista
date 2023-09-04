notas_da_prova = []
continuar = True

while continuar:
    nota_da_prova = float(input("digite a nota do estudante ou se quiser parar digite -1"))
    if nota_da_prova == -1:
        continuar = False
    else:
        notas_da_prova.appen(nota_da_prova)

if len(notas_da_prova) < 0:
    media_das_provas = sum(notas_da_prova) / len(notas_da_prova)
    print(f"A media da prova é {media_das_provas}")
else:
    print("Nenhuma nota foi encontrado")    
