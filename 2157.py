n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    palavra = ''
    palavra2 = ''
    for i in range(a, b + 1):
        palavra += str(i)
    
    print(palavra, end='')
    for i in range(len(palavra)):
        print(palavra[len(palavra) - i - 1], end='')
    print()