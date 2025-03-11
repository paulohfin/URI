while True:
    try:
        linha1 = input()
        linha2 = input()
        linha3 = input()
        linha4 = input()
        
        num1 = int(linha1[0]) * 1000 + int(linha2[0]) * 100 + int(linha3[0]) * 10 + int(linha4[0])
        tam = len(linha1)
        num2 = int(linha1[tam - 1]) * 1000 + int(linha2[tam - 1]) * 100 + int(linha3[tam - 1]) * 10 + int(linha4[tam - 1])
        
        for i in range(1, len(linha1) - 1):
            p = int(linha1[i]) * 1000 + int(linha2[i]) * 100 + int(linha3[i]) * 10 + int(linha4[i])
            print(chr((num1 * p + num2)%257), end='')
        print()
    except EOFError:
        break