loop = 1
fim = 0
def perg_num(x):
    #Perguntar o numero e transforma-lo em string
    #
    global  nume, expoente, num
    num = input(f"""Digite um número {x}\n "Se não for respeitado a regra de numero podem haver erros" """)
    nume = num
    expoente=len(num)-1

def continuar_loop():
    #Pegunta se quer continuar o looping
    #
    global loop
    fim = int(input("""deseja continuar???
    [ 1 ] SIM 
    [ 2 ] NÃO """))
    if fim == 2:
        loop =2
        return 
    else:
         loop = 1 

def Redefinir_variaveis():
    #Serve para redefinir as variaveis pro 0. Pra que elas nao acumulem valores
    #
    global posit_num,expoente, soma
    posit_num = 0
    expoente =len(num)-1
    soma = 0

while loop == 1: #comeco loop
    print("\033c")
    print('''
    ---------------------------------
    | [ 1 ] BINARIO - DECIMAL;      |
    | [ 2 ] OCTAL - DECIMAL;        |
    | [ 3 ] HEXADECIMAL - DECIMAL;  |
    | [ 4 ] SOBRE                   |
    | [ 5 ] SAIR                    |
    ---------------------------------''')
    opcao = int(input("SUA OPCAO: "))

#### Binario/Octal/Hexadecimal para decimal ####

#Binario para decimal

    if opcao == 1:#Binario para decimal comeco
        perg_num("(0 e 1):")
        Redefinir_variaveis()
        while posit_num<len(num):
            numa=int(num[posit_num])*2**expoente
            expoente-=1
            soma+=numa
            posit_num+=1
        else:
            print(f"Seu numero {nume} em binario é {soma} em decimal\n")
            continuar_loop()#Binario to decimal final
            
#Octal para decimal
            
    elif opcao == 2: #Octal to decimal comeco
        perg_num("(Entre 0 a 7):")
        Redefinir_variaveis()
        while posit_num<len(num):
            numa=int(num[posit_num])*8**expoente
            expoente-=1
            soma+=numa
            posit_num+=1
        else:
            print(f"Seu numero {nume} em octal é {soma} em decimal\n")
            continuar_loop()#Octal to decimal final

#Hexadecimal para decimal            
       
    elif opcao == 3: #Hexadecimal to decimal comeco
        perg_num("(Entre 0 a 9 , A a F):")
        Redefinir_variaveis()
        while posit_num<len(num):
            if num[posit_num]=="0" or num[posit_num]=="1" or num[posit_num]=="2" or num[posit_num]=="3" or num[posit_num]=="4" or num[posit_num]=="5" or num[posit_num]=="6" or num[posit_num]=="7" or num[posit_num]=="8" or num[posit_num]=="9":
                numa=int(num[posit_num])*16**expoente
            else:
                cc=num[posit_num]
                if num[posit_num]=="A" or num[posit_num]=="a":
                    cc=10
                elif num[posit_num]=="B" or num[posit_num]=="b":
                    cc=11
                elif num[posit_num]=="C" or num[posit_num]=="c":
                    cc=12
                elif num[posit_num]=="D" or num[posit_num]=="d":
                    cc=13
                elif num[posit_num]=="E" or num[posit_num]=="e":
                    cc=14
                elif num[posit_num]=="F" or num[posit_num]=="f":
                    cc=15
                numa=int(cc)*16**expoente
            soma+=numa
            expoente-=1
            posit_num+=1
        else:
            print(f"Seu numero {nume} em hexadecimal é {soma} em decimal \n")
            continuar_loop()#Hexadecimal to decimal final

    elif opcao == 4:#Sobre o trabalho
        print("\033c")
        print("""
        Projeto Interdisciplinar
        Feito por :
        Nome: Peterson Maranho Santos RGM: 29810078 Turma:1 O ;
        Nome: Victor Goya Pinto RGM: 30249414 Turma: 1 D;
        Nome: Lucas Marques Russi RGM: 29712343 Turma: 1 O;
        Nome: Lucas da Silva Trindade RGM: 29978751 Turma:1 D
        2022""")
        continuar_loop()

    elif opcao == 5:#Sair do programa
        break

    else:#Final das opcaoes
        print("ERROR")
        
else:
    print("PROGRAMA ENCERRADO")#final loop
