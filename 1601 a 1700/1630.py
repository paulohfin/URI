'''
Marcos trabalha em uma empreiteira, sua tarefa é cercar com estacas os terrenos onde serão construidos prédios. Existem duas restrições para a distribuição destas estacas, elas devem ser colocadas de tal forma que a distância entre duas estacas seja sempre igual, e a segunda restrição é que Marcos deve usar o menor número possível de estacas. Marcos é seu amigo e pediu para que você desenvolva um programa para ajudá-lo.

Entrada
Haverão diversos casos de teste, cada caso de teste é descrito em uma linha por dois números X e Y (1 ≤ X, Y ≤ 100000000), os quais representam as dimensões do terreno. O final da entrada é indicado por final de arquivo.

Saída
Para cada caso de teste imprima uma linha com o número mínimo de estacas necessário para cercar o tereno.
'''
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
    try:
        a, b = map(int, input().split(' '))
        
        div = mdc(a, b)
        diva = a / div 
        divb = b / div
        
        print(int(diva * 2 + divb * 2))
    except EOFError:
        break
