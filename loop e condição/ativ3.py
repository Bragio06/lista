import random


numero_aleatorio= random.randint(1, 100)


while True:
    
    tentativa_do_usuario = int(input("Digite um número: "))
    
    
    if tentativa_do_usuario == numero_aleatorio:
        print("Parabéns, você acertou!")
        break
    elif tentativa_do_usuario < numero_aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")