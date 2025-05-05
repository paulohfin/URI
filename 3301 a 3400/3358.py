'''
A região sul do Brasil é caracterizada pela ascendência multicultural de seus habitantes, sendo principalmente europeus e sobretudo italianos, alemães e poloneses. Uma consequência interessante disso é a variação na dificuldade na pronúncia dos sobrenomes da população, o que as vezes dificulta a vida dos professores na realização da chamada de sua turma, gerando até situações constrangedoras. Dada a possibilidade de constrangimento em suas aulas, a professora Jiraiya decidiu pesquisar os sobrenomes em sua lista de chamadas. Na concepção de Jiraiya, um sobrenome é difícil se tiver três ou mais consoantes consecutivas.

Entrada
A entrada contém vários casos de teste. A primeira linha possui um inteiro N que indica o número de casos de teste. Cada caso de teste consiste em um sobrenome. A string contém letras do alfabeto sem acentos, a primeira letra está sempre em maiúscula e o sobrenome pode ter no máximo 42 caracteres.

Saída
Para cada caso de entrada, imprima o sobrenome e se é fácil ou não, conforme mostra o exemplo abaixo.
'''
n = int(input())

for m in range(n):
    sobre = input()
    cont = 0
    for i in sobre:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and  i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U': 
            cont += 1
        else:
            cont = 0
        if cont > 2:
            print(sobre,'nao eh facil')
            break
    if cont <= 2:
        print(sobre,'eh facil')
