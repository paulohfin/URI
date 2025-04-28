'''
Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

Entrada
A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 1032).

Saída
Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.
'''
contcaso = 0
while True:
    try:
        contcaso += 1
        s1 = input()
        s2 = input()
        cont = 0
        p = 0
        for i in range(len(s2)):
            k = False
            if s2[i] == s1[0]:
                for j in range(len(s1)):
                    if i + j < len(s2) and s1[j] == s2[i + j]:
                        k = True
                    else: k = False
                if k == True:
                    cont += 1 
                    p = i
        if cont > 0:
            print('Caso #' + str(contcaso) + ':')
            print('Qtd.Subsequencias:',cont)
            print('Pos:',p + 1)
        else:
            print('Caso #' + str(contcaso) + ':')
            print('Nao existe subsequencia')
        print()
    except EOFError:
        break