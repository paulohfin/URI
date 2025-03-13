n = int(input())
for i in range(n):
    num = []
    hame = input()
    v = False
    k = 0
    for j in hame:
        if ord(j) >= ord('0') and ord(j) <= ord('9'):
            if v == False:
                v = True
                k = int(j)
            else:
                k = k * 10 + int(j)
        else:
            if v == True:
                v = False
                num.append(k)
                k = 0
    if v == True:
        num.append(k)
    soma = 0 
    for j in num:
        soma += j 
    print(soma)