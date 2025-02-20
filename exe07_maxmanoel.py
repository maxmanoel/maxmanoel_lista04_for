#7-peça ao usuário para inserir seu nome e  um numero.  Se o numero for menor que 10 ,
#  exiba o nome dele esse numero de vezes, caso contrario,  exiba a mensagem “numero muito alto 3 vezes”
nome = (input("Digite seu nome:"))
n1 = int(input("Digite um numero: "))
if n1 < 10: 
    for i in range (n1):

        print(nome)
    else:
        print("max manoel")
else:
        if n1 >= 10:
            for _ in range (3):
                print("numero muito alto")