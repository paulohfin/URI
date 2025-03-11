while True:
    try:
        n = int(input())
        linha = input().split(' ')
        if (linha[1] == '+' and int(linha[0]) + int(linha[2]) > n) or (linha[1] == '*' and int(linha[0]) * int(linha[2]) > n):
            print('OVERFLOW')
        else:
            print('OK')
    except EOFError: