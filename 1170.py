n = int(input())

for i in range(n):
    k = float(input())
    cont = 0
    while k > 1:
        cont += 1
        k /= 2
    print(cont,'dias')