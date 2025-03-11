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