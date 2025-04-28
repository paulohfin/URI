n = int(input())
S = 0
B = 0
A = 0
S1 = 0
B1 = 0
A1 = 0
for i in range(n):
    nome = input()
    s, b, a = map(int, input().split(' '))
    
    S += s 
    B += b 
    A += a 
    s1, b1, a1 = map(int, input().split(' '))
    
    S1 += s1 
    B1 += b1 
    A1 += a1  

print('Pontos de Saque: %.2f'%(100*S1/S),end='')
print('%')
print('Pontos de Bloqueio: %.2f'%(100*B1/B),end='')
print('%')
print('Pontos de Ataque: %.2f'%(100*A1/A),end='')
print('%')