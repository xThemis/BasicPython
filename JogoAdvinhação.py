#xTh3m1s
import random
import os

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite um numero: "))

while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("ERRO: O numero é maior")
    elif (sorteado<jogador):
        print("ERRO: o Numero é menor")
    erros+=1
    jogador=int(input("Digite um numero: "))

print ("Numero " + str(jogador) + ", Voce Acertou em " + str(erros+1)+ " Tentativas")