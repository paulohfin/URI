def fatorial(n):
    if n == 0:
        return 1
    else: return n * fatorial(n - 1)

while True:
    palavra = input()
    if palavra !='0':
        j = len(palavra)
        soma = 0
        for i in range(len(palavra)):
            soma += (ord(palavra[i]) - ord('0')) * fatorial(j)
            j-=1

        print(soma)
    else: break