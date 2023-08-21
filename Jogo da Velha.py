import os
import random
from colorama import Fore, Back, Style

jogarNovamente="s"
jogadas=0
quemJoga=2
maxJogadas=9
vit="n"
velha=[       
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
#matriz da velha
def tela():
    global velha
    os.system("cls")
    print("    0   1   2\n")
    print("0   "+ velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1   "+ velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2   "+ velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)
#verificar jogador jogar
def jogadorjoga():
    global jogadas
    global vit
    global maxJogadas
    global quemJoga
    if quemJoga==2 and jogadas<maxJogadas: 
        try:
            l=int(input("Linha: "))
            c=int(input("Coluna: "))
            while velha[l][c]!=" ":
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c] = "X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha ou coluna invalida")
            os.system("pause") 
#verificar cpu jogada   
def cpujoga():
    global jogadas
    global vit
    global maxJogadas
    global quemJoga
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!= " ":
           l=random.randrange(0,3)
           c=random.randrange(0,3) 
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2

#verificar vitoria
def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="n"):
            break
        #verificar colunas
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1

            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #verificar diagonal1
        soma=0
        idiag=0
        while idiag<3:
            if(velha[idiag][idiag]==s):
               soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break
        #diagonal 2
        soma=0
        idiagl=0
        idiagc=2
        while idiagc>=0:
            if(velha[idiagl][idiagc]==s):
               soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global  maxJogadas
    global quemJoga
    jogadas=0
    quemJoga=2
    maxJogadas=9
    vit="n"
    velha=[       
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

while(jogarNovamente=="s" or jogarNovamente=="S"):        
    while True:
        tela()
        jogadorjoga()
        cpujoga()
        tela()
        vit=verificarVitoria()
        if(vit!="n")or(jogadas>maxJogadas):
             break
        
    print(Fore.RED +"Fim de Jogo"+ Fore.YELLOW)
    if(vit=="X" or vit=="O"):
       print("Resultado: Jogador " + vit + " Venceu!")
    else:
        print("Resultado: Empate")
    jogarNovamente=input(Fore.BLUE + "Jogar Novamente?[s/n]:")
