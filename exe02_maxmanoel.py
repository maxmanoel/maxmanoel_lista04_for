#2-faça um programa que solicite ao usuário para digitar seu nome e um numero qualquer, e em seguida exiba seu nome varias vezes de acordo com numero que ele digitou 

nome = str(input("Digite seu nome: "))
numero = int(input("Digite um numero qualquer: "))
for i in range(numero):
    print(nome)
else:
    print("MAX MANOEL")