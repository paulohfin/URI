import math

linha = input()
while linha != '0':
    A, B, C = linha.split(' ')
    
    area = int(A) * int(B)
    terreno = 100.0 * area / int(C)
    
    print(int(math.sqrt(terreno)))
    
    linha = input()