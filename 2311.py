def menor(a, b):
    if a < b: return a 
    else: return b 
def maior(a, b):
    if a > b: return a 
    else: return b 
n = int(input())
atleta = []
for i in range(n):
    nome = input()
    grau = float(input())
    n1, n2, n3, n4, n5, n6, n7 = map(float, input().split(' '))
    
    nota = (n1 + n2 + n3 + n4 + n5 + n6 + n7 - menor(menor(menor(menor(menor(menor(n1, n2), n3), n4), n5), n6), n7) - maior(maior(maior(maior(maior(maior(n1, n2), n3), n4), n5), n6), n7)) * grau
    
    atleta.append((nota, nome))

for i in atleta:
    print(i[1] + ' %.2f' %i[0])