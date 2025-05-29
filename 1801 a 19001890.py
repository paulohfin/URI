'''
Na Tailândia, um tipo popular de transporte público é o chamado tuk-tuk (ตุ๊กตุ๊ก), também conhecido como auto-riquixá. O governo de Phuket decidiu criar um novo sistema de placas para os tuk-tuks, com a finalidade de diferenciá-los dos outros tipos de veículos. Devido ao turismo, que é uma das principais atividades econômicas da província, a frota de tuk-tuks vem crescendo rapidamente. Espera-se que com o novo sistema de placas seja possível criar uma quantidade suficiente de placas distintas para atender à demanda pelos próximos 42 anos.

Um sistema de placas é definido por dois números, C e D. Uma placa nesse sistema é uma cadeia com C consoantes seguidas por D dígitos. Uma placa não pode ser vazia (sem consoantes e sem dígitos).

No alfabeto tailandês existem 44 consoantes e 10 dígitos. No entanto, como os símbolos de algumas consoantes são parecidos com os de outras, o governo decidiu que serão utilizadas somente 26 consoantes, cujos símbolos foram considerados suficientemente diferentes.

Para garantir que existirão tuk-tuks suficientes para os competidores da Final Mundial da Maratona de Programação em 2016, o governo de Phuket quer saber qual o número de placas distintas é possível gerar com um determinado sistema de placas.

Entrada
A primeira linha da entrada contém um inteiro T indicando o número de instâncias.

Cada instância consiste em uma linha contendo os números inteiros C (0 ≤ C ≤ 6) e D (0 ≤ D ≤ 9) representando as quantidades de consoantes e dígitos, respectivamente, em um sistema de placas.

Saída
Para cada instância, imprima uma linha com a quantidade de placas distintas que podem ser geradas pelo sistema correspondente. É garantido que a resposta sempre será menor que 231.
'''
n = int(input())

for i in range(n):
    c, d = map(int, input().split(' '))
    if c != 0 or d != 0:
        print(26 ** c * 10 ** d)
    else:
        print(0)