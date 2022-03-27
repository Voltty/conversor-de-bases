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
    if opcao == 1:#binario to decimal comeco
        while i<len(num):
            numa=int(num[i])*2**bb
            bb-=1
            aa+=numa
            i+=1
        else:#binario to decimal meio
            print(f"Seu numero {num} em binario eh {aa} em decimal")
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
            print(f"Seu numero {num} em octal eh {aa} em decimal")
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
            numa=int(num[i])*16**bb
            bb-=1
            aa+=numa
            i+=1
        else:#hexadecimal to decimal meio
            print(f"Seu numero {num} em hexadecimal eh {aa} em decimal")
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
                print(f"Seu numero {num} em decimal eh {dd} em binario")
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
                print(f"Seu numero {num} em decimal eh {dd} em octal")
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
        while num > 0:
            resto = num % 16
            num = num // 16
            aa += str(resto)
        else:
            bb = len(aa)-1
            dd = ""
            while bb>=0: #decimal to hexadecimal meio
                cc = (aa[bb])
                dd += str(cc)
                bb -= 1
            else:
                print(f"Seu numero {num} em decimal eh {dd} em hexadecimal")
                fim = int(input("""deseja continuar???
                [ 1 ] SIM 
                [ 2 ] NAO """))
                if fim == 2:
                    break
                else:
                    loop = 1#decimal to hexadecimal final
                    print("\033c")
    else:#final
        print("ERROR")
#final loop
