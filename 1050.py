'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.
'''
a = int(input())

if a == 61:
    print('Brasilia')
elif a == 71:
    print('Salvador')
elif a == 11:
    print('Sao Paulo')
elif a == 21:
    print('Rio de Janeiro')
elif a == 32:
    print('Juiz de Fora')
elif a == 19:
    print('Campinas')
elif a == 27:
    print('Vitoria')
elif a == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
