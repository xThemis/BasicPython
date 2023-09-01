#xThemis
import os
import sqlite3
from sqlite3 import Error

#Conexão
def ConexaoBanco():
    caminho="C:\\Users\\thais\\OneDrive\\Área de Trabalho\\RoadMap (Programação)\\SQLite\\HelloWorld"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

Vcon=ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com sucesso")
        #conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    #conexao.close()
    return res

def MenuPrincipal():
    os.system("cls")
    print("1. Inserir Novo Registro")
    print("2. Deletar Registro")
    print("3. Atualizar Registro")
    print("4. Consultar Registro por ID")
    print("5. Consultar Registro por Nome")
    print("6. Sair")

    Inicio=input("Digite uma opcao:")
    opc=int(Inicio) if Inicio.isdigit() else 0

    return opc

def menuInserir():
    os.system("cls")
    Nome=input("Digite o Nome: ")
    Tel=input("Digite o Telefone: ")
    Email=input("Digite o Email: ")
    Vsql="INSERT INTO Agenda (T_NOMECONTATO, T_TELCONTATO, T_EMAILCONTATO) VALUES ('"+Nome+"','"+Tel+"','"+Email+"')"
    query(Vcon,Vsql)

def menuDeletar():
    os.system("cls")
    dele=input("Digite o ID do Contato para excluir:")
    Vsql="DELETE FROM Agenda WHERE N_IDCONTATO="+dele
    query(Vcon,Vsql)

def menuAtualizar():
    os.system("cls")
    atual=input("Digite o ID do Contato para alterar: ")
    r=consultar(Vcon,"SELECT * FROM Agenda WHERE N_IDCONTATO="+atual)
    rnome=r[0][1]
    rtel=r[0][2]
    remail=r[0][3]
    Vnome=input("Digite o nome: ")
    Vtel=input("Digite o telefone: ")
    Vemail=input("Digite o email : ")
    if(len(Vnome)==0):
        Vnome=rnome
    if(len(Vtel)==0):
        Vtel=rtel
    if(len(Vemail)==0):
        Vemail=remail
    Vsql="UPDATE Agenda SET T_NOMECONTATO='"+Vnome+"',T_TELCONTATO='"+Vtel+"',T_EMAILCONTATO='"+Vemail+"'"
    query(Vcon,Vsql)

def menuConsultarID():
    Vsql="SELECT * FROM Agenda"
    res=consultar(Vcon,Vsql)
    Vlim=10
    Vcont=0
    for r in res:
        print("ID:{0:.<3} Nome:{1:.<30} Telefone:{2:.<14} E-mail:{3:.<30}".format(r[0],r[1],r[2],r[3]))
        Vcont+=1;
        if(Vcont>=Vlim):
            Vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")  

def menuConsultarNome():
    Vnome=input("Digite o nome: ")
    Vsql="SELECT * FROM Agenda WHERE T_NOMECONTATO LIKE '%"+Vnome+"%'"
    res=consultar(Vcon,Vsql)
    Vlim=10 
    Vcont=0
    for r in res:
        print("ID:{0:.<3} Nome:{1:.<30} Telefone:{2:.<14} E-mail:{3:.<30}".format(r[0],r[1],r[2],r[3]))
        Vcont+=1;
        if(Vcont>=Vlim):
            Vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")  

opc=0
while opc !=6:
    opc=MenuPrincipal()
    if opc==1:
        menuInserir()
    elif opc==2:
        menuDeletar()
    elif opc==3:
        menuAtualizar()
    elif opc==4:
        menuConsultarID()
    elif opc==5:
        menuConsultarNome()
    elif opc==6:
        os.system("cls")
        print("Programa Finalizado")
    else:
        print("Opcao invalida. Digite Novamente")
        os.system("pause")

Vcon.close()
os.system("pause")
