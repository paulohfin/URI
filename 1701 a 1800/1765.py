'''
Jorge era um cara muito determinado a criar trapézios doces de Natal. Os trapézios são feitos de fios de balas puxa-puxa e recheados com sorvete. Após assados eles assumem uma perfeita forma bidimensional de um trapézio. Por padrão, todos os trapézios possuem a mesma altura, 5cm, mas as suas bases podem alterar de tamanho dependendo da disponibilidade de balas puxa-puxa que Jorge possui. Um dia Jorge estava curioso para saber quanto de sorvete ele estava ocupando para cada tamanho de trapézio que fazia, então ele chamou você para ajudá-lo.

Você deve fazer um programa que dados quantos tamanhos diferentes de trapézios vão ser feitos, quantos trapézios daquele tamanho serão produzidos e as medidas das bases de puxa-puxa, você diga quantos cm2 de soverte serão ocupados por cada tamanho.

Entrada
A entrada é composta por diversos casos de teste. A primeira linha de cada caso de teste começa com um inteiro T (0 ≤ T ≤ 50) indicando quantos tamanhos diferentes haverá nessa fornada. As T linhas seguintes contém 3 valores, um inteiro Q (0 ≤ Q ≤ 50) indicando a quantidade de trapézios feitos com as medidas A e B (0 ≤ A,B ≤ 50) ambos de dupla precisão antecedidos por Q. A entrada termina quando T for zero.

Saída
Para cada caso de teste apresente o valor de sorvete usado, em cm2, para cada um dos tamanhos. Após cada caso de teste, imprima uma linha em branco.
'''
n = int(input())
while n != 0:
    for i in range(n):
        q, a, b = map(float, input().split(' '))
        print('Size #' + str(i+1) + ':')
        print('Ice Cream Used: %.2f' %(q*(a+b)*5/2) + ' cm2')
    print()
    n = int(input())
