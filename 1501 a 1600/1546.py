'''
Muitos alunos de diversas universidades conhecem o portal de programação IRU. Este portal possui milhares de problemas de programação disponíveis. Diariamente a equipe do IRU recebe diversos feedbacks (elogios, bugs, dúvidas, sugestões, ...) que precisam primeiramente ser atribuídos para membros da equipe resolver.

Como a equipe é muito ocupada e não tem tempo para classificar estes feedbacks, você foi convidado a escrever um programa que faça isso e mostre quem será o membro responsável por resolver e responder o feedback.

Os membros responsáveis em cada setor são:

Elogios: Rolien
Bugs: Naej
Dúvidas: Elehcim
Sugestões: Odranoel
Entrada
O primeiro valor a ser lido é o número de casos de teste N (1 < N < 100). Cada caso de teste representa um dia de trabalho respondendo feedbacks. Cada caso de teste inicia com K (1 < K < 50), indicando o número de feedbacks recebidos naquela data. Seguem K linhas indicando a categoria de cada um dos feedbacks, conforme mostrado acima (1, 2, 3 ou 4).

Saída
Para cada caso de teste você deve imprimir o nome do membro da equipe responsável por responder o feedback.
'''
n = int(input())

for i in range(n):
    m = int(input())
    for j in range(m):
        k = int(input())
        
        if k == 1:
            print('Rolien')
        elif k == 2:
            print('Naej')
        elif k == 3:
            print('Elehcim')
        else:
            print('Odranoel')
