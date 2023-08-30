ano = int(input("Digite qual o ano você quer saber se e bissexto : "))

if (ano % 4 ==0 and ano % 100 != 0) or (ano % 400 == 0) :
    print("O ano nao é bissexto ")
else:
    print("O ano é bissexto ")
