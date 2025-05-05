'''
A internet já não é tão segura quanto ela já foi. Um dos sinais disso é o aumento de ataque de hackers a diversos sites. Para piorar, quando um hacker rouba a senha de um usuário em um determinado site, ele tem também acesso a todas as outras contas deste usuário em outros sites, pois a maioria dos usuários hoje em dia usa a mesma senha em todos os sites que acessa.

Uma das soluções propostas para resolver este problema é usar diferentes senhas para cada site, ou até mesmo diferentes variações da mesma senha. Por exemplo, para variar a senha “batata”, é possível usar a senha “bAtaTa”, “B4tat4”, “baTATA”, etc. Ou seja, para cada caractere do alfabeto, é possível formar uma variação colocando tal caractere em maiúsculo ou minúsculo. Inclusive, para aumentar o número total de variações, para os caracteres A, E, I, O e S é possível usar também os números 4, 3, 1, 0 e 5, respectivamente.

Seu amigo precisa aumentar o número de variações de sua senha, e pediu sua ajuda. Dada a senha que ele escolheu, diga o número de diferentes variações que é possível montar.

Entrada
A primeira linha contém um inteiro T, indicando o número de casos de teste a seguir.

Cada caso de teste contém uma sequência de caracteres S, indicando a senha de seu amigo. Para cada senha, haverá no mínimo 1 e no máximo 16 caracteres, os quais podem ser uma das 26 letras do alfabeto, minúsculas ou maiúsculas.

Saída
Para cada caso de teste imprima uma linha contendo um inteiro, indicando o número de diferentes variações que é possível montar com a senha dada, incluindo ela mesma.
'''
while True:
    try:
        n = int(input())
        
        for i in range(n):
            for j in range(n):
                if i + j == n-1:
                    print(2, end='')
                elif i == j:
                    print(1, end='')
                else:
                    print(3, end='')
            print()
    except EOFError:
        break
