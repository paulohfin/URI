'''
Neste Natal, Papai Noel designou alguns de seus mais dedicados elfos para enfeitar o quintal da fábrica de presentes no Polo Norte. No quintal haviam vários pinheiros, de tamanhos diversos.

Papai Noel orientou aos elfos que para enfeitar uma árvore com cordões luminosos, o tamanho dos mesmos deveria ser 5 vezes o tamanho da árvore.

Para descobrir a altura de cada árvore, Papai Noel deu a eles um teodolito velho (aparelho utilizado para medir ângulos) e mandou que utilizassem conceitos trigonométricos para descobrir a altura de cada árvore.

Sua tarefa é ajudar os elfos a descobrir uma forma de calcular a quantidade de cordões luminosos necessários para cada árvore.

Considere para este desafio que o teodolito fica posicionado na altura de cada elfo e que essa altura precisa ser computada. O teodolito informará valores em graus. Utilize neste problema PI = 3.141592654.

Entrada
A entrada possui vários casos de teste. Cada caso de teste é composto de um valor de ponto flutuante de dupla precisão A que é o ângulo calculado pelo teodolito (1.00 < A < 90.00), um valor de ponto flutuante de dupla precisão B (1 ≤ B ≤ 100) que corresponde à distância entre o teodolito e a árvore e um valor de ponto flutuante de dupla precisão C (0,50 ≤ C ≤ 1.50 ) que é a altura do elfo medidor. O final da entrada é determinado por EOF.

Saída
A saída deverá apresentar a quantidade de cordão luminoso necessário para adornar a árvore. Observação: Os valores deverão ser arredondados em 2 casas decimais.
'''
import math

while True:
    try:
        a, b, c = map(float, input().split(' '))
        print('%.2f' %(5 * (math.tan(a * 3.141592654 / 180) * b + c)))
    except EOFError:
        break
