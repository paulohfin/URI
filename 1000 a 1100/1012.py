'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
'''
a1, a2, a3 = map(float, input().split(' '))

print(f'TRIANGULO: %0.3f' %(a1 * a3 / 2))
print(f'CIRCULO: %0.3f' %(3.14159 * a3 * a3))
print(f'TRAPEZIO: %0.3f' %((a1 + a2) * a3 / 2))
print(f'QUADRADO: %0.3f' %(a2 * a2))
print(f'RETANGULO: %0.3f' %(a1 * a2))
