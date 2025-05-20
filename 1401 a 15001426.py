'''
Não, não é "mais um tijolo na parede", é apenas um problema sobre somar números.

Suponha que você tem uma parede com o formato de um triângulo, como a mostrada abaixo. A parede tem 9 linhas, e a i-ésima linha tem exatamente i tijolos, considerando que a linha mais acima é a 1ª e que a mais abaixo é a 9ª. Alguns tijolos são rotulados com um número, enquanto os demais estão em branco. Os tijolos rotulados aparecem apenas em linhas ímpares, e ocupam posições ímpares dentro das suas linhas.

​

O problema que você deve resolver consiste em rotular os tijolos em branco com números, de tal forma que a seguinte regra seja satisfeita: O número de um tijolo é igual à soma dos números dos dois tijolos abaixo dele. Obviamente, esta regra não é aplicada à 9ª linha. Todos os números devem ser inteiros.

Nota: O exemplo de entrada contém dois casos de teste. O primeiro dele corresponde à parede mostrada acima.

Entrada
A primeira linha da entrada contém um inteiro N, indicando o número de casos de teste. Esta linha é seguida pelos casos de teste. Cada caso é descrito por 5 linhas. Essas linhas correspondem às linhas ímpares da parede, de cima para baixo, como descrito acima. Cada linha contém os números nos tijolos já rotulados da linha correspondente na parede, da esquerda para a direita, separados por um espaço em branco.

Você pode assumir que todo caso de teste é correto, isto é, existe uma solução para o problema descrito.

Saída
Para cada caso de teste, a saída deve ser formada por 9 linhas descrevendo os números de todos os tijolos da parede. Assim, a i-ésima linha deve conter os números correspondentes aos i tijolos da i-ésima linha da parede, da esquerda para a direita, separados por um espaço.
'''
def linha1(li, lj):
    lista = []
    for i in range(len(lj)):
        lista.append(li[i])
        lista.append(int((lj[i] - (li[i] + li[i+1]))/2))
    lista.append(li[i+1])
    return lista
def linha2(l):
    lista = []
    for i in range(len(l)-1):
        lista.append(l[i]+l[i+1])
    return lista
def printar(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if j == len(lista[i])-1:
                print(lista[i][j])
            else:
                print(lista[i][j],end=' ')
n = int(input())

for i in range(n):
    l1 = list(map(int,input().split(' ')))
    l3 = list(map(int,input().split(' ')))
    l5 = list(map(int,input().split(' ')))
    l7 = list(map(int,input().split(' ')))
    l9 = list(map(int,input().split(' ')))
    
    lista=[]
    lista.append(linha1(l9,l7))
    lista.insert(0,linha2(lista[0]))
    lista.insert(0,linha1(l7,l5))
    lista.insert(0,linha2(lista[0]))
    lista.insert(0,linha1(l5,l3))
    lista.insert(0,linha2(lista[0]))
    lista.insert(0,linha1(l3,l1))
    lista.insert(0,linha2(lista[0]))
    lista.insert(0,l1)
    
    printar(lista)