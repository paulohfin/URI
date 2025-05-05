'''
Atualmente, no ano de 2114, o conhecimento de que não estamos sozinhos no universo não é novidade, porém um século atrás isto ainda era um mistério. Diversas civilizações na Via Láctea já emitiram algum tipo de sinal provando sua existência, e outras até estabeleceram um contato aberto com a Terra em busca de informações sobre a tal Árvore Hexagonária (afinal, estamos em 2114).

Rafael tem muito interesse pelo assunto, e em um trabalho para a escola se encarregou de descobrir qual foi a civilização mais antiga que enviou um Hello Galaxy para toda a galáxia. Hello Galaxy nada mais é que o primeiro dos passos do Protocolo de Iniciação na Sociedade Via Láctea, PISVL, garantindo que a nova civilização possa entrar em contato com as demais caso necessário.

A mensagem Hello Galaxy traz consigo duas informações básicas: o texto “Hello Galaxy”, que faz parte da tradição, e o nome do planeta da civilização que enviou a mensagem. O CMSVL, Centro de Monitoramento da Sociedade Via Láctea, instalado, por algum motivo, na Terra, recebe tais mensagens, armazenando em um registro o ano em que foi recebida a mensagem e a quantidade de anos que tal mensagem levou para chegar até ali.

A tarefa de Rafael é simples: descobrir quem foi a primeira civilização a enviar a mensagem Hello Galaxy.

Entrada
Haverá diversos casos de teste.

Cada caso de teste inicia com um inteiro N (1 ≤ N ≤ 100), que indica quantas mensagens Hello Galaxy foram coletados por Rafael em sua pesquisa.

Em seguida haverão N linhas, cada uma representando uma mensagem. Cada mensagem é representada pelo nome do planeta da civilização, contendo entre 1 e 50 caracteres (somente letras), e dois inteiros A e T (2014 ≤ A ≤ 2113, 1 ≤ T ≤ 1000), representando, respectivamente, o ano em que a mensagem foi recebida no planeta Terra, e a quantidade de anos que tal mensagem levou para chegar do planeta de origem até o planeta Terra.

O último caso de teste é indicado quando N = 0, o qual não deverá ser processado.

Saída
Para cada caso de teste, deverá ser impressa uma linha, contendo o nome do planeta da primeira civilização a enviar a mensagem Hello Galaxy. Pode-se supor que não haverá empates.
'''
n = int(input())
 
while n != 0:
    antigo = 100000000000000000000000000000000
    nome = ''
    for i in range(n):
        leitura = input()
        nome2, ano, tempo = leitura.split(' ')
        if antigo > int(ano) - int(tempo):
            nome = nome2
            antigo = int(ano) - int(tempo)
            
    print(nome)
    
    n = int(input())
