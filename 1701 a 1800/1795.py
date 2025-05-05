'''
O triângulo trinomial é um triângulo numérico de coeficientes trinomiais. Ele pode ser obtido com uma linha contendo um único "1", a próxima linha contendo três 1 e cada elemento das linhas seguintes sendo calculado como a soma do elemento acima à esquerda, imediatamente acima e acima à direita:



A primeira linha do triângulo trinomial é numerada com zero, a segunda linha é a de número 1 e assim sucessivamente.

Sua tarefa é, dado um número de linha R, escrever um programa que exiba a soma de seus elementos. Por exemplo, a soma dos elementos da linha 2 é 9 = 1 + 2 + 3 + 2 + 1.

Entrada
A entrada é o número de linha R (0 ≤ R ≤ 20).

Saída
A saída é a soma de todos os elementos da linha R. Não esqueça do caractere de fim-de-linha após exibir a soma.
'''
def pascal(n):
    pasc = []
    pasc.append(1)
    for i in range(2 * n):
        pasc.append(0)

    for i in range(n):
        temp = []
        for j in range(len(pasc)):
            if j == 0:
                temp.append(pasc[j])
            elif j == 1:
                temp.append(pasc[j] + pasc[j - 1])
            else:
                temp.append(pasc[j] + pasc[j - 1] + pasc[j - 2])
        pasc = temp
    soma = 0
    for i in pasc:
        soma += i
    return soma

while True:
    try:
        n = int(input())
        print(pascal(n))
    except EOFError:
        break;
