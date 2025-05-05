'''
É dado na entrada uma string A e outra B. Em uma operação você pode escolher uma letra da primeira string e avançar esta letra. Avançar uma letra significa transformá-la na próxima letra do alfabeto, veja que a próxima letra depois de z vem a letra a novamente!

Por exemplo, podemos transformar a string ab em bd em no mínimo 3 operações: ab -> bb -> bc -> bd. Podemos aplicar operações nas letras em qualquer ordem, outra possibilidade seria: ab -> ac -> bc -> bd.

Dadas as duas strings, calcule o mínimo número de operações necessárias para transformar a primeira na segunda.

Entrada
Na primeira linha terá um inteiro T (T ≤ 100) indicando o número de casos de teste.

Para cada caso, na única linha teremos as duas strings A (1 ≤ |A| ≤ 100* ou 1 ≤ |A| ≤ 104** - sendo que |A| significa o tamanho da string A) e B (|B| = |A|* ou |B| = |A​|**) separadas por um espaço. Ambas as strings são compostas por letras do alfabeto minúsculas apenas e são do mesmo tamanho.

*Ocorre em aproximadamente 90% dos casos de teste;

**Ocorre nos demais casos de teste.

Saída
Para cada caso imprima o número mínimo de operações.
'''
n = int(input())
for i in range(n):
    soma = 0
    a, b = input().split(' ')
    for i in range(len(a)):
        soma += (ord(b[i]) - ord(a[i])) % 26
    print(soma)
