loop = 1
fim = 0  
while loop == 1: #comeco loop
    num = input('Digite um número: ')
    i=0
    aa=0
    bb=len(num)-1
    print('''Tipo do seu numero: 
    [ 1 ] BINARIO;
    [ 2 ] OCTAL;
    [ 3 ] HEXADECIMAL;
    [ 4 ] DECIMAL.''')
    opcao = int(input("SUA OPCAO: "))# ? to ?
    if opcao == 1:#binario to decimal comeco
        while i<len(num):
            numa=int(num[i])*2**bb
            bb-=1
            aa+=numa
            i+=1
        else:#binario to decimal meio
            print(aa)
            fim = int(input("""deseja continuar???
            [ 1 ] SIM 
            [ 2 ] NAO """))
            if fim == 2:
                break
            else:
                loop = 1 #binario to decimal final
    elif opcao == 2: #Octal to decimal comeco
        while i<len(num):
            numa=int(num[i])*8**bb
            bb-=1
            aa+=numa
            i+=1
        else:#Octal to decimal meio
            print(aa)
            fim = int(input("""deseja continuar???
            [ 1 ] SIM 
            [ 2 ] NAO """))
            if fim == 2:
                break
            else:
                loop = 1 #Octal to decimal final
    elif opcao == 3: #hexadecimal to decimal comeco
        while i<len(num):
            numa=int(num[i])*16**bb
            bb-=1
            aa+=numa
            i+=1
        else:#hexadecimal to decimal meio
            print(aa)
            fim = int(input("""deseja continuar???
            [ 1 ] SIM 
            [ 2 ] NAO """))
            if fim == 2:
                 break
            else:
                loop = 1#hexadecimal to decimal final
    elif opcao == 4: #decimal to ?
        print('''Para qual tipo de numero voce quer converter seu decimal:
        [ 1 ] BINARIO;
        [ 2 ] OCTAL;
        [ 3 ] HEXADECIMAL;''')
        nt = int(input("SUA OPCAO: "))
        if nt == 1: #decimal to binario comeco
            while:
            else:#decimal to binario meio

                #decimal to binario final
        elif nt == 2:#decimal to octal comeco
            while:
            else:#decimal to octal meio

                #decimal to octal final
        elif nt == 3:#decimal to hexadecimal comeco
            while:
            else:#decimal to hexadecimal meio

                #decimal to hexadecimal final
    else:#final
        print("ERROR")
#final loop
