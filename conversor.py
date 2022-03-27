loop = 1
fim = 0 
while loop == 1: #comeco loop
    print("\033c")
    num = input('Digite um número: ')
    i=0
    aa=0
    bb=len(num)-1
    print('''Tipo do seu numero: 
    [ 1 ] BINARIO - DECIMAL;
    [ 2 ] OCTAL - DECIMAL;
    [ 3 ] HEXADECIMAL - DECIMAL;
    [ 4 ] DECIMAL - BINARIO;
    [ 5 ] DECIMAL - OCTAL;
    [ 6 ] DECIMAL - HEXADECIMAL.''')
    opcao = int(input("SUA OPCAO: "))\
#### Binario/Octal/Hexadecimal para decimal ####
    nume = num
    if opcao == 1:#binario to decimal comeco
        while i<len(num):
            numa=int(num[i])*2**bb
            bb-=1
            aa+=numa
            i+=1
        else:#binario to decimal meio
            print(f"Seu numero {nume} em binario eh {aa} em decimal\n")
            fim = int(input("""deseja continuar???
            [ 1 ] SIM 
            [ 2 ] NAO """))
            if fim == 2:
                break
            else:
                loop = 1 #binario to decimal final
                print("\033c")
    elif opcao == 2: #Octal to decimal comeco
        while i<len(num):
            numa=int(num[i])*8**bb
            bb-=1
            aa+=numa
            i+=1
        else:#Octal to decimal meio
            print(f"Seu numero {nume} em octal eh {aa} em decimal\n")
            fim = int(input("""deseja continuar???
            [ 1 ] SIM 
            [ 2 ] NAO """))
            if fim == 2:
                break
            else:
                loop = 1 #Octal to decimal final
                print("\033c")
    elif opcao == 3: #hexadecimal to decimal comeco
        while i<len(num):
            if num[i]=="0" or num[i]=="1" or num[i]=="2" or num[i]=="3" or num[i]=="4" or num[i]=="5" or num[i]=="6" or num[i]=="7" or num[i]=="8" or num[i]=="9":
                numa=int(num[i])*16**bb
            else:
                cc=num[i]
                if num[i]=="A" or num[i]=="a":
                    cc=10
                elif num[i]=="B" or num[i]=="b":
                    cc=11
                elif num[i]=="C" or num[i]=="c":
                    cc=12
                elif num[i]=="D" or num[i]=="d":
                    cc=13
                elif num[i]=="E" or num[i]=="e":
                    cc=14
                elif num[i]=="F" or num[i]=="f":
                    cc=15
                numa=int(cc)*16**bb
            aa+=numa
            bb-=1
            i+=1
        else:#hexadecimal to decimal meio
            print(f"Seu numero {nume} em hexadecimal eh {aa} em decimal \n")
            fim = int(input("""deseja continuar???
            [ 1 ] SIM 
            [ 2 ] NAO """))
            if fim == 2:
                 break
            else:
                loop = 1#hexadecimal to decimal final
                print("\033c")
#### Decimal para binario/octal/hexadecimal ####
    elif opcao == 4: #decimal to binario comeco
        aa = ""
        num = int(num)
        while num > 0:
            resto = num % 2
            num = num // 2
            aa += str(resto)
        else:
            bb = len(aa)-1
            dd = ""
            while bb>=0: #decimal to binario meio
                cc = (aa[bb])
                dd += str(cc)
                bb -= 1
            else:
                print(f"Seu numero {nume} em decimal eh {dd} em binario\n")
                fim = int(input("""deseja continuar???
                [ 1 ] SIM 
                [ 2 ] NAO """))
                if fim == 2:
                    break
                else:
                    loop = 1#decimal to binario final
                    print("\033c")
    elif opcao == 5: #decimal to octal comeco
        aa = ""
        num = int(num)
        while num > 0:
            resto = num % 8
            num = num // 8
            aa += str(resto)
        else:
            bb = len(aa)-1
            dd = ""
            while bb>=0: #decimal to octal meio
                cc = (aa[bb])
                dd += str(cc)
                bb -= 1
            else:
                print(f"Seu numero {nume} em decimal eh {dd} em octal\n")
                fim = int(input("""deseja continuar???
                [ 1 ] SIM 
                [ 2 ] NAO """))
                if fim == 2:
                    break
                else:
                    loop = 1#octal to decimal final
                    print("\033c")
    elif opcao == 6: #decimal to hexadecimal comeco
        aa = ""
        num = int(num)
        while num>0:
            str(num)
            resto=num%16
            if resto==10:
                resto="A"
            elif resto==11:
                resto="B"
            elif resto==12:
                resto="C"
            elif resto==13:
                resto="D"
            elif resto==14:
                resto="E"
            elif resto==15:
                resto="F"
            num=num//16
            aa+=str(resto)
        else: #decimal to hexadecimal meio
            bb=len(aa)-1
            dd=""
            while bb>=0:
                cc=(aa[bb])
                dd+=str(cc)
                bb-=1
            else:
                print(f"Seu numero {nume} em decimal eh {dd} em hexadecimal\n")
                fim = int(input("""deseja continuar???
                [ 1 ] SIM 
                [ 2 ] NAO """))
                if fim == 2:
                    break
                else:
                    loop = 1 #decimal to hexadecimal final
                    print("\033c")
    else:#final
        print("ERROR")
#final loop
